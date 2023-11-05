import unittest

from pizza_recommendation_app import pizza_main


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(10, pizza_main.get_pizza_slice("big"))

    def test_price(self):
        self.assertEqual(1200, pizza_main.get_pizza_price("small"))

    def test_for_size_of_stomach(self):
        self.assertEqual(2, pizza_main.get_size_of_stomach("hungry"))

    def test_pizza_recommendation(self):
        box_size = "big"
        hungry = 10
        super_hungry = 10
        classic = 5
        expected = f'number of slice needed: {65} number of boxes: {7} number of slice left: {5} total: {35000}'
        self.assertEqual(expected, pizza_main.pizza_recommendation_app(box_size, hungry, super_hungry, classic))


if __name__ == '__main__':
    unittest.main()
