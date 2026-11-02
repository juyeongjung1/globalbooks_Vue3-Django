from io import StringIO

from django.core.management import call_command
from django.core.management.base import CommandError
from rest_framework.test import APITestCase

from .models import Book


class BookAPITests(APITestCase):
    def setUp(self):
        self.book = Book.objects.create(title='Vue入門', author='山田', price=1000)
        self.url = f'/api/books/{self.book.id}/'

    def test_crud_and_search(self):
        response = self.client.get('/api/books/', {'keyword': 'Vue'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual([book['id'] for book in response.data], [self.book.id])
        self.assertEqual(self.client.get('/api/books/', {'keyword': '該当なし'}).data, [])
        self.assertEqual(self.client.get(self.url).data['title'], 'Vue入門')

        response = self.client.post('/api/books/', {'title': '新刊', 'author': '佐藤', 'price': 1}, format='json')
        self.assertEqual(response.status_code, 201)
        url = f"/api/books/{response.data['id']}/"
        response = self.client.put(url, {'title': '改訂版', 'author': '佐藤', 'price': 2000}, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], '改訂版')
        self.assertEqual(self.client.delete(url).status_code, 204)
        self.assertEqual(self.client.get(url).status_code, 404)

    def test_invalid_prices_are_rejected_on_create_and_update(self):
        for price in [0, -1, 1.5, None, '', 'abc']:
            with self.subTest(price=price):
                data = {'title': '書籍', 'author': '著者', 'price': price}
                self.assertEqual(self.client.post('/api/books/', data, format='json').status_code, 400)
                self.assertEqual(self.client.put(self.url, data, format='json').status_code, 400)
                self.assertEqual(self.client.patch(self.url, {'price': price}, format='json').status_code, 400)
        self.book.refresh_from_db()
        self.assertEqual(self.book.price, 1000)
        self.assertEqual(Book.objects.count(), 1)

    def test_required_fields_and_length(self):
        for field in ['title', 'author']:
            for value in ['', '   ', 'あ' * 256]:
                with self.subTest(field=field, value=value):
                    data = {'title': '書籍', 'author': '著者', 'price': 100}
                    data[field] = value
                    self.assertEqual(self.client.post('/api/books/', data, format='json').status_code, 400)

    def test_optional_fields_accept_empty_or_null(self):
        for value in ['', None]:
            with self.subTest(value=value):
                response = self.client.post('/api/books/', {
                    'title': '書籍', 'author': '著者', 'price': 100,
                    'publisher': value, 'image_path': value,
                }, format='json')
                self.assertEqual(response.status_code, 201)
                self.assertEqual(response.data['image_path'], value)

    def test_put_requires_required_fields_but_patch_accepts_changes_only(self):
        self.assertEqual(self.client.put(self.url, {'price': 1200}, format='json').status_code, 400)
        response = self.client.patch(self.url, {'price': 1200}, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], 'Vue入門')

    def test_seed_does_not_delete_existing_books(self):
        with self.assertRaises(CommandError):
            call_command('seed_books', stdout=StringIO())
        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(Book.objects.get(pk=self.book.pk).title, 'Vue入門')

    def test_seed_inserts_ten_books_into_empty_database(self):
        self.book.delete()
        call_command('seed_books', stdout=StringIO())
        self.assertEqual(Book.objects.count(), 10)
        self.assertEqual(Book.objects.get(pk=1).image_path, '/images/1.png')
