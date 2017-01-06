import unittest
from pashtoCardinals.pashtoCardinals import *

class PashtocardinalsTestCase(unittest.TestCase):

    # def test_less_than_thousands(self):
    #     self.assertTrue(less_than_thousnds("21"))
    #
    # def test_greater_than_thousand(self):
    #     self.assertTrue(greater_than_thousand(4353))

    def test_convert(self):
        self.assertFalse(convert("21"))


if __name__ == '__main__':
    unittest.main()
