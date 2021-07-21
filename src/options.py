from math import log, sqrt, exp, pi
from scipy.stats import norm

class BlackScholes:

    @classmethod
    def d1(cls, s, x, r, sig, t, k=0):
        return (log(s / x) + (r - k + (sig ** 2) / 2) * t) / (sig * (sqrt(t)))

    @classmethod
    def d2(cls, d1, sig, t):
        return d1 - sig * (sqrt(t))

    @classmethod
    def call_price(cls, d1, d2, s, x, r, t):
        return s * norm.cdf(d1) - x * exp(-r * t) * norm.cdf(d2)

    @classmethod
    def put_price(cls, d1, d2, s, x, r, t):
        return BlackScholes.call_price(d1, d2, s, x, r, t) - s + x * exp(-r * t)


class GreeksCall:

    @classmethod
    def delta(cls, d1, t, k=0):
        return exp(-k * t) * norm.cdf(d1)

    @classmethod
    def gamma(cls, d1, s, sig, t, k=0):
        return exp((-d1 ** 2) / 2 - k * t) / (s * sig * sqrt(2 * t * pi))

    @classmethod
    def vega(cls, d1, s, t, k=0):
        return s * sqrt(t) * exp(-(d1 ** 2) / 2) * exp(-k * t) / sqrt(2 * pi)

    @classmethod
    def rho(cls, d2, x, r, t):
        return x * t * exp(-r * t) * norm.cdf(d2)


    @classmethod
    def theta(cls, d1, d2, s, x, r, sig, t, k):
        return -s * exp(-(d1 ** 2) / 2 - k * t) * sig / sqrt(8 * t * pi) + k * s * exp(-k * t) * norm.cdf(d1) - r * x * exp(-r * t) * norm.cdf(d2)



class GreeksPut:

    @classmethod
    def delta(cls, d1, t, k=0):
        return exp(-k * t) * norm.cdf(-d1)

    @classmethod
    def gamma(cls, d1, s, sig, t, k=0):
        return exp(-(d1 ** 2) / 2 - k * t) / ( s * sig * sqrt(2 * t * pi))

    @classmethod
    def vega(cls, d1, s, t, k=0):
        return s * exp(-(d1 ** 2) / 2 - k * t) * sqrt(t)/sqrt(2 * pi)

    @classmethod
    def rho(cls, d2, s, x, r, t):
        return -x * t * exp(-r * t) * norm.cdf(-d2)

    @classmethod
    def theta(cls, d1, d2, s, x, r, sig, t, k):
        return -s * exp(-(d1 ** 2) / 2 - k * t) * sig / sqrt(8 * t* pi) - k * s * exp(-k * t) * (1 - norm.cdf(d1)) + r * x * exp(-r * t) * (1-norm.cdf(d2))

