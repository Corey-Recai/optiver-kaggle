import unittest
import options.black_scholes as sut


class TestBlackScholes(unittest.TestCase):

    def test_d1_nodiv(self):
        self.assertEqual(0.6509066782522832, sut.BlackScholes.d1(50., 45., 0.04, 0.3, 0.75))

    def test_d1_div(self):
        self.assertEqual(0.630276662220168, sut.BlackScholes.d1(100, 90, 0.06, 0.35, 0.5, 0.02))

    def test_d2(self):
        d1 = sut.BlackScholes.d1(50., 45., 0.04, 0.3, 0.75)
        self.assertEqual(0.39109905711695164, sut.BlackScholes.d2(d1, 0.3, 0.75))

    def test_call_price(self):
        d1 = sut.BlackScholes.d1(50., 45., 0.04, 0.3, 0.75)
        d2 = sut.BlackScholes.d2(d1, 0.3, 0.75)
        self.assertEqual(8.643433707115669, sut.BlackScholes.call_price(d1, d2, 50., 45., 0.04, 0.75))

    def test_put_price(self):
        d1 = sut.BlackScholes.d1(50., 45., 0.04, 0.3, 0.75)
        d2 = sut.BlackScholes.d2(d1, 0.3, 0.75)
        self.assertEqual(2.3134827167985392, sut.BlackScholes.put_price(d1, d2, 50., 45., 0.04, 0.75))