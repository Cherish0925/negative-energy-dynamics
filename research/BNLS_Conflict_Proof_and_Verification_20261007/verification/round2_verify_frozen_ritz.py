#!/usr/bin/env python3
"""Verify frozen compact-profile and Ritz inequalities using exact rationals.

No NumPy, SciPy, NPZ, numerical solver, or regenerated floating-point samples.
Inputs are a frozen hexadecimal-jet profile and frozen rational Ritz jets.
Every decision is a Fraction comparison. Printed decimal approximations are
intentionally omitted. This verifies the stated finite certificate components,
not an entire nonlinear existence theorem.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import re
import sys
import time
from fractions import Fraction as F
from pathlib import Path
import round2_radial_exact_common as common

add, mul, scale, deriv = common.add, common.mul, common.scale, common.deriv
hermite, bernstein = common.hermite, common.bernstein


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def parse_hex_rational(value: str) -> F:
    """Parse the exact hexadecimal real, without converting through float."""
    require(isinstance(value, str) and bool(re.fullmatch(
        r'[+-]?0x[0-9a-fA-F]+(?:\.[0-9a-fA-F]*)?p[+-]?\d+', value)),
        'Invalid finite hexadecimal rational')
    sign = -1 if value.startswith('-') else 1
    value = value.lstrip('+-')
    mantissa, exponent = value[2:].split('p')
    whole, _, frac = mantissa.partition('.')
    coefficient = F(sign * int(whole + frac, 16), 16 ** len(frac))
    exponent = int(exponent)
    return coefficient * (2 ** exponent if exponent >= 0 else F(1, 2 ** -exponent))


def power(p: list[F], n: int) -> list[F]:
    result = [F(1)]
    for _ in range(n):
        result = mul(result, p)
    return result


def integral01(p: list[F]) -> F:
    return sum((value / (degree + 1) for degree, value in enumerate(p)), F(0))


def positive_definite(matrix: list[list[F]]) -> bool:
    require(len(matrix) in (1, 2), 'Only 1x1 and 2x2 certificates are used')
    require(all(len(row) == len(matrix) for row in matrix), 'Nonsquare matrix')
    require(all(matrix[i][j] == matrix[j][i] for i in range(len(matrix))
                for j in range(len(matrix))), 'Nonsymmetric rational matrix')
    return matrix[0][0] > 0 and (len(matrix) == 1 or
        matrix[0][0] * matrix[1][1] - matrix[0][1] ** 2 > 0)


def split_bernstein(coefficients: list[F]) -> tuple[list[F], list[F]]:
    left, right = [coefficients[0]], [coefficients[-1]]
    while len(coefficients) > 1:
        coefficients = [(coefficients[j] + coefficients[j + 1]) / 2
                        for j in range(len(coefficients) - 1)]
        left.append(coefficients[0])
        right.append(coefficients[-1])
    return left, right[::-1]


def residual_cell_bound(b: list[F], a: F, h: F, origin: bool, depth: int) -> F:
    """Integrate an exact Bernstein sup bound with its exact radial weight."""
    if depth:
        left, right = split_bernstein(b)
        return (residual_cell_bound(left, a, h / 2, origin, depth - 1) +
                residual_cell_bound(right, a + h / 2, h / 2, origin, depth - 1))
    upper = max(abs(v) for v in b)
    weight = (((a + h) ** 4 - a ** 4) / 4 if origin else
              (1 / a ** 2 - 1 / (a + h) ** 2) / 2)
    require(weight >= 0, 'Negative radial integration weight')
    return upper ** 2 * weight


def atan_bounds(denominator: int, terms: int = 32) -> tuple[F, F]:
    require(terms % 2 == 0, 'An even alternating partial sum is required')
    x = F(1, denominator)
    lower = sum(((-1) ** k * x ** (2 * k + 1) / (2 * k + 1)
                 for k in range(terms)), F(0))
    return lower, lower + x ** (2 * terms + 1) / (2 * terms + 1)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_jets(path: Path) -> tuple[list[F], list[list[F]]]:
    data = json.loads(path.read_text())
    nodes = [F(*item) for item in data['nodes']]
    jets = [[parse_hex_rational(value) for value in row] for row in data['jets_hex']]
    require(len(nodes) == len(jets) >= 2, 'Invalid profile mesh/jet lengths')
    require(nodes[0] == 0 and all(a < b for a, b in zip(nodes, nodes[1:])),
            'Profile nodes must start at zero and strictly increase')
    require(all(len(row) == 4 for row in jets), 'Four jets are required at each node')
    require(jets[0][1] == jets[0][3] == 0, 'Radial origin odd jets must vanish')
    require(all(value == 0 for value in jets[-1]), 'Compact endpoint jets must vanish')
    return nodes, jets


def verify(profile_path: Path, ritz_path: Path) -> dict:
    started = time.monotonic()
    nodes, qjets = load_jets(profile_path)
    qpolys = [hermite(qjets[j], qjets[j + 1], nodes[j + 1] - nodes[j])
              for j in range(len(nodes) - 1)]
    ritz = json.loads(ritz_path.read_text())
    require([F(*item) for item in ritz['nodes']] == nodes,
            'Frozen Ritz and canonical profile meshes differ')
    require(set(ritz['channels']) == {'0', '1', '2'}, 'Unexpected angular channels')

    # Machin identity pi=16 atan(1/5)-4 atan(1/239), with alternating bounds.
    alo, ahi = atan_bounds(5)
    blo, bhi = atan_bounds(239)
    pi_lo, pi_hi = 16 * alo - 4 * bhi, 16 * ahi - 4 * blo
    require(F(3) < pi_lo < pi_hi < F(355, 113), 'Rational pi enclosure failed')
    surface_upper = 2 * F(355, 113) ** 2

    radial_residual_squared_bound = F(0)
    for j, q in enumerate(qpolys):
        a, h = nodes[j], nodes[j + 1] - nodes[j]
        rr = [a, h]
        r2, r3 = power(rr, 2), power(rr, 3)
        numerator = add(scale(mul(r3, deriv(q, 4)), h ** -4),
                        scale(mul(r2, deriv(q, 3)), 6 * h ** -3))
        numerator = add(numerator, scale(mul(rr, deriv(q, 2)), 3 * h ** -2))
        numerator = add(numerator, scale(deriv(q), -3 / h))
        numerator = add(numerator, mul(r3, add(q, scale(power(q, 3), -1))))
        if a == 0:
            require(all(v == 0 for v in numerator[:3]), 'Origin cancellation failed')
            coefficients = bernstein(scale(numerator[3:], h ** -3))
            bound = residual_cell_bound(coefficients, a, h, True, 3)
        else:
            bound = residual_cell_bound(bernstein(numerator), a, h, False, 3)
        radial_residual_squared_bound += bound
    residual_squared_upper = surface_upper * radial_residual_squared_bound
    checks = {'canonical_q_residual_lt_0.000242':
              residual_squared_upper < F(121, 500000) ** 2}

    records = []
    exact_integrals = {}
    q_z_squared_upper = None
    for ell, coefficient in ((0, 3), (2, 3), (1, 1)):
        frozen = ritz['channels'][str(ell)]
        trial = [[F(value) for value in row] for row in frozen['trial_jets']]
        require(len(trial) == len(nodes) and all(len(row) == 4 for row in trial),
                'Invalid frozen trial jet dimensions')
        require(trial[0][1] == trial[0][3] == 0, 'Trial origin odd jets must vanish')
        require(all(value == 0 for value in trial[-1]), 'Trial endpoint jets must vanish')
        trials = [trial, qjets] if ell == 0 else [trial]
        dimension, count = 4 + 2 * ell, len(trials)
        mass = [[F(0)] * count for _ in range(count)]
        kinetic = [[F(0)] * count for _ in range(count)]
        potential = [[F(0)] * count for _ in range(count)]
        for cell, q in enumerate(qpolys):
            a, h = nodes[cell], nodes[cell + 1] - nodes[cell]
            rr = [a, h]
            mass_weight, kinetic_weight = power(rr, dimension - 1), power(rr, dimension - 3)
            q2 = mul(q, q)
            fs = [hermite(jets[cell], jets[cell + 1], h) for jets in trials]
            nums = [add(mul(rr, scale(deriv(f, 2), h ** -2)),
                        scale(deriv(f), F(dimension - 1) / h)) for f in fs]
            for i in range(count):
                for j in range(i, count):
                    product = mul(fs[i], fs[j])
                    mass[i][j] += h * integral01(mul(mass_weight, product))
                    kinetic[i][j] += h * integral01(mul(kinetic_weight, mul(nums[i], nums[j])))
                    potential[i][j] += coefficient * h * integral01(mul(mass_weight, mul(q2, product)))
        for matrix in (mass, kinetic, potential):
            for i in range(count):
                for j in range(i):
                    matrix[i][j] = matrix[j][i]
        gram = [[mass[i][j] + kinetic[i][j] for j in range(count)] for i in range(count)]
        for label, computed in (('A', gram), ('M', mass), ('V', potential)):
            require(computed == [[F(value) for value in row] for row in frozen[label]],
                    f'Recomputed frozen {label} matrix differs in angular channel {ell}')
        require(positive_definite(gram), f'Nonpositive trial Gram matrix in channel {ell}')
        def excess(mu: F) -> list[list[F]]:
            return [[potential[i][j] - mu * gram[i][j] for j in range(count)]
                    for i in range(count)]
        channel_checks = {}
        if ell == 0:
            channel_checks['top_eigenvalue_ge_5.395'] = potential[0][0] >= F(1079, 200) * gram[0][0]
            channel_checks['second_eigenvalue_gt_2.999'] = positive_definite(excess(F(2999, 1000)))
            q_z_squared_upper = surface_upper * gram[1][1]
            checks['canonical_q_Z_le_104'] = q_z_squared_upper <= 104 ** 2
        elif ell == 2:
            channel_checks['top_eigenvalue_gt_2.11'] = positive_definite(excess(F(211, 100)))
        else:
            channel_checks['top_eigenvalue_gt_1.04'] = positive_definite(excess(F(26, 25)))
            channel_checks['gamma_half_top_ge_1.5'] = potential[0][0] >= F(3, 2) * (kinetic[0][0] + mass[0][0] / 2)
        checks.update({f'ell_{ell}_{key}': value for key, value in channel_checks.items()})
        records.append({'ell': ell, 'potential_coefficient': coefficient,
                        'checks': channel_checks, 'frozen_matrices_match_exactly': True})
        exact_integrals[str(ell)] = {
            'A': [[str(v) for v in row] for row in gram],
            'M': [[str(v) for v in row] for row in mass],
            'V': [[str(v) for v in row] for row in potential]}
    require(all(checks.values()), 'At least one exact certificate inequality failed')
    return {
        'verified': True,
        'scope': 'Canonical residual and Z bound; recomputed frozen Ritz variational inequalities only.',
        'arithmetic': 'Exact rational polynomial integration and Bernstein subdivision; no floating-point decisions.',
        'sha256': {'profile': sha256(profile_path), 'ritz_data': sha256(ritz_path),
                   'polynomial_helpers': sha256(Path(common.__file__)),
                   'verifier': sha256(Path(__file__))},
        'profile': profile_path.name, 'ritz_data': ritz_path.name,
        'mesh_cells': len(nodes) - 1, 'compact_support_radius': str(nodes[-1]),
        'checks': checks, 'channels': records,
        'exact_bounds': {'sphere_area_upper': str(surface_upper),
                         'residual_squared_upper': str(residual_squared_upper),
                         'residual_norm_threshold': '121/500000',
                         'q_Z_squared_upper': str(q_z_squared_upper)},
        'recomputed_integrals': exact_integrals,
        'elapsed_seconds_diagnostic': time.monotonic() - started}


def main() -> None:
    if hasattr(sys, 'set_int_max_str_digits'):
        sys.set_int_max_str_digits(0)
    directory = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--profile', type=Path, default=directory / 'round2_radial_H4_exact_h1_16.json')
    parser.add_argument('--ritz', type=Path, default=directory / 'round2_ritz_exact_data.json')
    parser.add_argument('--output', type=Path, default=directory / 'round2_verify_frozen_ritz_results.json')
    arguments = parser.parse_args()
    result = verify(arguments.profile, arguments.ritz)
    arguments.output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({key: result[key] for key in ('verified', 'scope', 'sha256', 'checks', 'elapsed_seconds_diagnostic')}, indent=2))


if __name__ == '__main__':
    main()
