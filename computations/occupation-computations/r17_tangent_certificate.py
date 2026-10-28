"""Validated exclusion of every coincident two-Townes tangent direction.

Uses the R15 directed binary64 interval ODE implementation and its proved
shooting bracket. No floating quadrature or numerical eigenvalue solver is
used. All integrands are enclosed on whole Picard tubes. Exponential tail
integrals are evaluated by rational polynomial moments, not exp().
"""
import json
import math
from fractions import Fraction as F
from r15_validated_townes import I, origin, step, power, up

def nonnegative_square(x):
    if x.lo >= 0 or x.hi <= 0:
        z = x*x
        return I(max(0, z.lo), z.hi)
    return I(0, up(max(x.lo*x.lo, x.hi*x.hi)))

def radial_integrands(r, q, p):
    q2 = nonnegative_square(q)
    p2 = nonnegative_square(p)
    h2 = nonnegative_square(q+r*p)
    return [r*z for z in [q2, h2, q2*h2, q2*p2,
                         h2*h2, p2*p2, h2*p2]]

def tail_moment(n, rate):
    # Integral from 0 to infinity (s+6)*(s+8)^n exp(-rate*s) ds.
    result = I(0)
    for k in range(n+1):
        coefficient = math.comb(n, k)*8**(n-k)
        result += coefficient*(I(math.factorial(k+1))/power(rate, k+2)
                               + 6*I(math.factorial(k))/power(rate, k+1))
    return result

def certify():
    # These exact dyadic endpoints were independently shot to opposite sides
    # of the Townes separatrix in r15_validated_townes.py --certificate.
    r, y = origin(I(2.20620086, 2.20620087))
    r0 = r
    # On [0,r0], Q<=2.21 and |Q'|<=7r, hence |Lambda Q|<=2.21+7r0^2.
    q0 = I(221)/100
    h0 = q0+7*I(r0)*r0
    p0 = 7*I(r0)
    origin_bounds = [q0*q0, h0*h0, q0*q0*h0*h0,
                     q0*q0*p0*p0, power(h0, 4), power(p0, 4),
                     h0*h0*p0*p0]
    integrals = [I(0, (z*I(r0)*r0/2).hi) for z in origin_bounds]
    steps = 0
    while r < 6:
        h = 2.**math.floor(math.log2(min(1/64, r/8, 6-r)))
        end = r+h
        assert end-r == h and end <= 6
        yn, tube = step(r, y, h)
        whole = radial_integrands(I(r,end), tube[0], tube[1])
        integrals = [old+h*part for old,part in zip(integrals,whole)]
        r, y = end, yn
        steps += 1
    q6 = I(y[0].hi)
    assert q6.hi < 1/200
    c = I(99)/100
    # Q(r)<=Q(6)e^{-c(r-6)} by the maximum principle, since
    # c^2<=1-Q(6)^2. Also |Q'|<=Q(6)e^{-c(r-6)}(1/c+1/(c^2 r)).
    assert (c*c+q6*q6).hi < 1
    derivative_factor = I(1)/c+I(1)/(6*c*c)
    tails = [
        q6*q6*tail_moment(0,2*c),
        q6*q6/power(c,4)*tail_moment(2,2*c),
        power(q6,4)/power(c,4)*tail_moment(2,4*c),
        power(q6,4)*power(derivative_factor,2)*tail_moment(0,4*c),
        power(q6,4)/power(c,8)*tail_moment(4,4*c),
        power(q6,4)*power(derivative_factor,4)*tail_moment(0,4*c),
        power(q6,4)*power(derivative_factor,2)/power(c,4)*tail_moment(2,4*c),
    ]
    integrals = [z+I(0,t.hi) for z,t in zip(integrals,tails)]
    m,h,j,k,a,b,d = integrals
    coefficient_40 = a-(2*h/m)*(2*j-h)
    coefficient_04 = 3*b/4-(2*k-m)
    coefficient_22 = 6*d-4*h*k/m-4*j+4*h
    assert coefficient_40.hi < 0
    assert coefficient_04.hi < 0
    assert coefficient_22.hi < 0
    # Coarse rational consequences used for the uniform 1/20 deficit.
    assert F(m.hi) < F(77,40) and F(h.hi) < F(6,5)
    assert F(m.lo) > F(9,5) and F(h.lo) > 1
    assert F(j.hi) < F(7,4) and F(k.hi) < F(8,3)
    assert F(coefficient_40.hi) < -F(1,2)
    assert F(coefficient_04.hi) < -F(3,4)
    assert F(coefficient_22.hi) < -F(3,2)
    pi_upper = F(22,7)
    assert F(1,20)*4*pi_upper*F(6,5)**2 < 1
    assert F(1,20)*pi_upper*F(77,40)**2 < F(3,4)
    assert F(1,10)*2*pi_upper*F(6,5)*F(77,40) < F(3,2)
    return {
        'arithmetic':'outward binary64 intervals; whole Picard tubes and analytic tails',
        'steps':steps,
        'radial_integrals':dict(zip(['m','h','j','k','a','b','d'],
                                   [[x.lo,x.hi] for x in integrals])),
        'radial_tail_upper_bounds':dict(zip(['m','h','j','k','a','b','d'],
                                          [x.hi for x in tails])),
        'coefficients_divided_by_2pi_pi_pi':
            [[x.lo,x.hi] for x in [coefficient_40,coefficient_04,coefficient_22]],
        'certificate_passed':True,
    }

if __name__ == '__main__':
    print(json.dumps(certify(), indent=2))
