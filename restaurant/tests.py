from django.test import TestCase
from restaurant.models import MenuItem

class MenuItemTest(TestCase):
    def test_get_item(self):
        item=MenuItem.objects.create(title="Pizza",price=55,inventory=80)
        itemstr=item.get_item()
        self.assertEqual(itemstr,"Pizza : 55")

