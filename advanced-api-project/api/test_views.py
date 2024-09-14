from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Book, Author

class BookTests(APITestCase):
    def test_create_book(self):
        url = reverse('book-list')
        data = {'title': 'Test Book', 'publication_year': 2023, 'author': 1}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

["response.data"]
["self.client.login"]
