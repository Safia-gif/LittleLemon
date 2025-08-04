from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        # Create test data
        self.menu1 = Menu.objects.create(title="Pizza", price=9.99, inventory=10)
        self.menu2 = Menu.objects.create(title="Burger", price=5.49, inventory=15)
        self.menu3 = Menu.objects.create(title="Salad", price=4.99, inventory=20)

        self.client = APIClient()

    def test_getall(self):
        response = self.client.get('/restaurant/menu/items/') 

        # Get all Menu items from the database
        menus = Menu.objects.all()
        serialized_menus = MenuSerializer(menus, many=True)

        # Check response
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serialized_menus.data)