"""Non-rigorous quadrature check of an analytically proved kernel identity.

The theorem in r16_dual_search.md does not depend on this script.
"""
import json
from pathlib import Path
import numpy as np
from scipy.integrate import quad

def kernel_norm_squared(eta):
    if eta == 0:
        return 1/(4*np.pi)
    return np.arcsin(eta)/(4*np.pi*eta*np.sqrt(1-eta*eta))

def main():
    results = []
    for eta in [0, 0.2, 0.5, 0.8, 0.9, 0.99]:
        direct, err = quad(lambda theta: 1/(1-4*eta*eta*theta*(1-theta)),
                           0, 1, epsabs=1e-11, epsrel=1e-11)
        direct /= 4*np.pi
        exact = kernel_norm_squared(eta)
        factor = 1 if eta == 0 else np.sqrt(1-eta*eta)*np.arcsin(eta)/eta
        results.append(dict(eta=eta, quadrature=direct, formula=exact,
                            abs_difference=abs(direct-exact),
                            weighted_factor=factor))
    output = {'status':'numerical check only; analytic proof is in companion note',
              'results':results}
    path = Path(__file__).with_name('r16_yukawa_check.json')
    path.write_text(json.dumps(output, indent=2)+'\n')
    print(json.dumps(output, indent=2))

if __name__ == '__main__':
    main()
