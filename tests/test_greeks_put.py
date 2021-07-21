import unittest
import options.greeks as sut
import options.black_scholes as bs

class TestPut(unittest.TestCase):
    def test_put_delta(self):
        d1 = bs.BlackScholes.d1(100, 90, 0.06, 0.35, 0.5, 0.02)
        self.assertEqual(0.2616273956282161, sut.Put.delta(d1, 0.5, 0.02))

    def test_put_gamma(self):
        d1 = bs.BlackScholes.d1(100, 90, 0.06, 0.35, 0.5, 0.02)
        self.assertEqual(0.013084364125226582, sut.Put.gamma(d1, 100, 0.35, 0.5, 0.02))

    def test_put_vega(self):
        d1 = bs.BlackScholes.d1(100, 90, 0.06, 0.35, 0.5, 0.02)
        self.assertEqual(22.897637219146517, sut.Put.vega(d1, 100, 0.5, 0.02))

    def test_put_rho(self):
        d1 = bs.BlackScholes.d1(100, 90, 0.06, 0.35, 0.5, 0.02)
        d2 = bs.BlackScholes.d2(d1, 0.35, 0.5)
        self.assertEqual(-15.32547974721431, sut.Put.rho(d2, 90, 0.06, 0.5))

    def test_put_theta(self):
        d1 = bs.BlackScholes.d1(100, 90, 0.06, 0.35, 0.5, 0.02)
        d2 = bs.BlackScholes.d2(d1, 0.35, 0.5)
        self.assertEqual(-6.6983702482919965, sut.Put.theta(d1, d2, 100, 90, 0.06, 0.35, 0.5, 0.02))