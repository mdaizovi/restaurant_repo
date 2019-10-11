import json
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from ..models import MenuItem
from ..api.serializers import MenuItemSerializer


class MenuItemListViewTest(APITestCase):
    """ Test module for MenuItem List View """

    def setUp(self):
        # Unnecessary, default objects are made via data migration
        pass

    def test_get_all_menu_items(self):
        response = self.client.get(reverse("menu-list-view"))
        menu_items = MenuItem.objects.all()
        serializer = MenuItemSerializer(menu_items, many=True)
        # Assert all items from data migration are getting made
        self.assertEqual(menu_items.count(), 6)
        # Assert endpoint returns ok
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # assert data is correct
        self.assertEqual(response.data, serializer.data)

    def test_menu_items_search(self):
        search_query = "enchilada"
        response = self.client.get(reverse("menu-list-view"), {"search": search_query})
        menu_items = MenuItem.objects.filter(name__icontains=search_query)
        serializer = MenuItemSerializer(menu_items, many=True)
        # Assert correct number of items are being returned
        self.assertEqual(menu_items.count(), 2)
        # Assert endpoint returns ok
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # assert data is correct
        self.assertEqual(response.data, serializer.data)

    def test_menu_items_ordering(self):
        ordering = ["name", "-name", "price", "-price"]
        for o in ordering:
            response = self.client.get(reverse("menu-list-view"), {"ordering": o})
            menu_items = MenuItem.objects.all().order_by(o)
            serializer = MenuItemSerializer(menu_items, many=True)
            # Assert correct number of items are being returned
            self.assertEqual(menu_items.count(), 6)
            # Assert endpoint returns ok
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            # assert data is correct
            self.assertEqual(response.data, serializer.data)
