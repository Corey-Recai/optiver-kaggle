from math import log, sqrt, exp, pi
from scipy.stats import norm


class BlackScholes:

    @classmethod
    def d1(cls, price, strike, interest, sigma, maturity, dividend=0):
        return (log(price / strike) + (interest - dividend + (sigma ** 2) / 2) * maturity) / (sigma * (sqrt(maturity)))

    @classmethod
    def d2(cls, d1, sigma, maturity):
        return d1 - sigma * (sqrt(maturity))

    @classmethod
    def call_price(cls, d1, d2, price, strike, interest, maturity):
        return price * norm.cdf(d1) - strike * exp(-interest * maturity) * norm.cdf(d2)

    @classmethod
    def put_price(cls, d1, d2, price, strike, interest, maturity):
        return BlackScholes.call_price(d1, d2, price, strike, interest, maturity) - price + strike * exp(-interest * maturity)


class GreeksCall:

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


class GreeksPut:

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

