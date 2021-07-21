import unittest
import src.options as sut

class TestOptions(unittest.TestCase):

    def test_d1(self):
        self.assertEqual(0.6509066782522832, sut.BlackScholes.d1(50., 45., 0.04, 0.3, 0.75))

    def test_d2(self):
        d1 = sut.BlackScholes.d1(50., 45., 0.04, 0.3, 0.75)
        self.assertEqual(0.39109905711695164, sut.BlackScholes.d2(d1, 0.3, 0.75))

    def test_call_price(self):
        self.assertEqual(8.643433707115669, sut.BlackScholes.call_price(50., 45., 0.04, 0.3, 0.75))

    def test_put_price(self):
        self.assertEqual(2.3134827167985392, sut.BlackScholes.put_price(50., 45., 0.04, 0.3, 0.75))