from math import log, sqrt, exp
from scipy.stats import norm

class BlackScholes:

    @classmethod
    def d1(cls, s, x, r, sig, t):
        return (log(s / x) + (r + (sig ** 2) / 2) * t) / (sig * (sqrt(t)))

    @classmethod
    def d2(cls, d1, sig, t):
        return d1 - sig * (sqrt(t))

    @classmethod
    def call_price(cls, s, x, r, sig, t):
        d1 = BlackScholes.d1(s, x, r, sig, t)
        return s * norm.cdf(d1) - x * exp(-r * t) * norm.cdf(BlackScholes.d2(d1, sig, t))

    @classmethod
    def put_price(cls, s, x, r, sig, t):
        return BlackScholes.call_price(s, x, r, sig, t) - s + x * exp(-r * t)
