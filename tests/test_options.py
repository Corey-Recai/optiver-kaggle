import unittest
import src.options as sut

class TestOptions(unittest.TestCase):

    def test_d1_nodiv(self):
        self.assertEqual(0.6509066782522832, sut.BlackScholes.d1(50., 45., 0.04, 0.3, 0.75))

    def test_d1_div(self):
        self.assertEqual(0.630276662220168, sut.BlackScholes.d1(100, 90, 0.06, 0.35, 0.5, 0.02))

    def test_d2(self):
        d1 = sut.BlackScholes.d1(50., 45., 0.04, 0.3, 0.75)
        self.assertEqual(0.39109905711695164, sut.BlackScholes.d2(d1, 0.3, 0.75))

    def test_call_price(self):
        self.assertEqual(8.643433707115669, sut.BlackScholes.call_price(50., 45., 0.04, 0.3, 0.75))

    def test_put_price(self):
        self.assertEqual(2.3134827167985392, sut.BlackScholes.put_price(50., 45., 0.04, 0.3, 0.75))

    def test_delta(self):
        d1 = sut.BlackScholes.d1(100, 90, 0.06, 0.35, 0.5, 0.02)
        self.assertEqual(0.728422438120952, sut.BlackScholes.delta(d1, 0.5, 0.02))

    def test_gamma(self):
        d1 = sut.BlackScholes.d1(100, 90, 0.06, 0.35, 0.5, 0.02)
        self.assertEqual(0.013084364125226582, sut.BlackScholes.gamma(d1, 100, 0.35, 0.5, 0.02))

    def test_vega(self):
        d1 = sut.BlackScholes.d1(100, 90, 0.06, 0.35, 0.5, 0.02)
        self.assertEqual(22.897637219146517, sut.BlackScholes.vega(d1, 100, 0.5, 0.02))

    def test_rho(self):
        d1 = sut.BlackScholes.d1(100, 90, 0.06, 0.35, 0.5, 0.02)
        d2 = sut.BlackScholes.d2(d1, 0.35, 0.5)
        self.assertEqual(28.34456926246856, sut.BlackScholes.rho(d2, 100, 90, 0.06, 0.5))

    def test_theta(self):
        d1 = sut.BlackScholes.d1(100, 90, 0.06, 0.35, 0.5, 0.02)
        d2 = sut.BlackScholes.d2(d1, 0.35, 0.5)
        self.assertEqual(-9.958676461955603, sut.BlackScholes.theta(d1, d2, 100, 90, 0.06, 0.35, 0.5, 0.02))