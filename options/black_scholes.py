from math import log, sqrt, exp
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