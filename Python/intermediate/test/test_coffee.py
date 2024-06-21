import unittest, coffee

class TestCoffeeMenu(unittest.TestCase):
    def setUp(self):
        self.coffee_menu = coffee.CoffeeMenu()

    def tearDown(self):
        self.coffee_menu = None

    def test_get_price_existing_item(self):
        self.assertIn('latte', self.coffee_menu.menu)

    def test_get_price_non_existing_item(self):
        self.assertFalse('frappe' in self.coffee_menu.menu)

    def test_add_item(self):
        new_item_name = 'frappe'
        new_item_price = 2.80

        self.assertFalse(new_item_name in self.coffee_menu.menu)
        self.assertTrue(new_item_price > 0)

if __name__ == '__main__':
    unittest.main()
