import unittest

import os, sys
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))

class CompactDisc(object):
    def __init__(self, initial_stock):
        self._stock_count = initial_stock

    def get_stock_count(self):
        return self._stock_count

    def buy(self, quantity):
        if quantity > self._stock_count:
            raise Exception('Sorry, there is not such quantity in stock')
        else:
            self._stock_count -= quantity


class BuyCdTest(unittest.TestCase):
    def setUp(self):
        self.cd = CompactDisc(10)

    def test_buy_cd_in_stock(self):
        self.cd.buy(5)
        self.assertEqual(5, self.cd.get_stock_count())

    def test_buy_cd_insufficient_stock(self):
        with self.assertRaises(Exception) as context:
            self.cd.buy(20)
        self.assertTrue('Sorry, there is not such quantity in stock', context.exception)

        


if __name__ == '__main__':
    unittest.main()
