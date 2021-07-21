from math import log, sqrt, exp, pi
from scipy.stats import norm

from options.black_scholes import BlackScholes


class Call:

    @classmethod
    def delta(cls, d1, maturity, dividend=0):
        return exp(-dividend * maturity) * norm.cdf(d1)

    @classmethod
    def gamma(cls, d1, price, sigma, maturity, dividend=0):
        return exp((-d1 ** 2) / 2 - dividend * maturity) / (price * sigma * sqrt(2 * maturity * pi))

    @classmethod
    def vega(cls, d1, price, maturity, dividend=0):
        return price * sqrt(maturity) * exp(-(d1 ** 2) / 2) * exp(-dividend * maturity) / sqrt(2 * pi)

    @classmethod
    def rho(cls, d2, strike, interest, maturity):
        return strike * maturity * exp(-interest * maturity) * norm.cdf(d2)


    @classmethod
    def theta(cls, d1, d2, price, strike, interest, sigma, maturity, dividend=0):
        return -price * exp(-(d1 ** 2) / 2 - dividend * maturity) * sigma / sqrt(8 * maturity * pi) + dividend * price * exp(-dividend * maturity) * norm.cdf(d1) - interest * strike * exp(-interest * maturity) * norm.cdf(d2)


class Put:

    @classmethod
    def delta(cls, d1, maturity, dividend=0):
        return exp(-dividend * maturity) * norm.cdf(-d1)

    @classmethod
    def gamma(cls, d1, price, sigma, maturity, dividend=0):
        return exp(-(d1 ** 2) / 2 - dividend * maturity) / ( price * sigma * sqrt(2 * maturity * pi))

    @classmethod
    def vega(cls, d1, price, maturity, dividend=0):
        return price * exp(-(d1 ** 2) / 2 - dividend * maturity) * sqrt(maturity)/sqrt(2 * pi)

    @classmethod
    def rho(cls, d2, strike, interest, maturity):
        return -strike * maturity * exp(-interest * maturity) * norm.cdf(-d2)

    @classmethod
    def theta(cls, d1, d2, price, strike, interest, sigma, maturity, dividend=0):
        return -price * exp(-(d1 ** 2) / 2 - dividend * maturity) * sigma / sqrt(8 * maturity * pi) - dividend * price * exp(-dividend * maturity) * (1 - norm.cdf(d1)) + interest * strike * exp(-interest * maturity) * (1-norm.cdf(d2))

