from django.test import TestCase
from restaurant.models import MenuItem, Booking

class MenuItemTest(TestCase):
    # def setUp(self):
    #     MenuItem.objects.create(title="Pasta", price=12.99, inventory=10)

    def test_get_item(self):
        item = MenuItem.objects.create(title="Pasta", price=12.99, inventory=10)

        itemstr = item.get_item()
        self.assertEqual(itemstr, "Pasta : $12.99")
        # self.assertEqual(item.price, 12.99)
        # self.assertEqual(item.inventory, 10)
        # self.assertEqual(item.get_item(), "Pasta : $12.99")