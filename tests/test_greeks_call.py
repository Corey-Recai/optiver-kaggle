import unittest
import options.black_scholes as bs
import options.greeks as sut

class TestCall(unittest.TestCase):
    def test_call_delta(self):
        d1 = bs.BlackScholes.d1(100, 90, 0.06, 0.35, 0.5, 0.02)
        self.assertEqual(0.728422438120952, sut.Call.delta(d1, 0.5, 0.02))

    def test_call_gamma(self):
        d1 = bs.BlackScholes.d1(100, 90, 0.06, 0.35, 0.5, 0.02)
        self.assertEqual(0.013084364125226582, sut.Call.gamma(d1, 100, 0.35, 0.5, 0.02))

    def test_call_vega(self):
        d1 = bs.BlackScholes.d1(100, 90, 0.06, 0.35, 0.5, 0.02)
        self.assertEqual(22.897637219146517, sut.Call.vega(d1, 100, 0.5, 0.02))

    def test_call_rho(self):
        d1 = bs.BlackScholes.d1(100, 90, 0.06, 0.35, 0.5, 0.02)
        d2 = bs.BlackScholes.d2(d1, 0.35, 0.5)
        self.assertEqual(28.34456926246856, sut.Call.rho(d2, 90, 0.06, 0.5))

    def test_call_theta(self):
        d1 = bs.BlackScholes.d1(100, 90, 0.06, 0.35, 0.5, 0.02)
        d2 = bs.BlackScholes.d2(d1, 0.35, 0.5)
        self.assertEqual(-9.958676461955603, sut.Call.theta(d1, d2, 100, 90, 0.06, 0.35, 0.5, 0.02))
