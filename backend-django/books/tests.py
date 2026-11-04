from io import BytesIO, StringIO
from pathlib import Path
from tempfile import TemporaryDirectory

from django.core.management import call_command
from django.core.management.base import CommandError
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import override_settings
from PIL import Image
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

    def test_sorting_and_search_use_the_same_results(self):
        second = Book.objects.create(title='Vue応用', author='佐藤', price=500)
        third = Book.objects.create(title='Python入門', author='田中', price=500)
        cases = {
            'id': [self.book.id, second.id, third.id],
            '-id': [third.id, second.id, self.book.id],
            'price': [second.id, third.id, self.book.id],
            '-price': [self.book.id, second.id, third.id],
            'title': [third.id, self.book.id, second.id],
            '-title': [second.id, self.book.id, third.id],
        }
        for ordering, expected in cases.items():
            with self.subTest(ordering=ordering):
                response = self.client.get('/api/books/', {'ordering': ordering})
                self.assertEqual([row['id'] for row in response.data], expected)
        response = self.client.get('/api/books/', {'keyword': 'Vue', 'ordering': 'price'})
        self.assertEqual([row['id'] for row in response.data], [second.id, self.book.id])
        response = self.client.get('/api/books/', {'ordering': 'unknown'})
        self.assertEqual([row['id'] for row in response.data], cases['id'])

    def test_likes_accumulate_and_survive_normal_edits(self):
        self.assertEqual(self.client.get(self.url).data['like_count'], 0)
        for expected in [1, 2, 3]:
            response = self.client.post(self.url + 'like/', {}, format='json')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.data['like_count'], expected)
        self.client.patch(self.url, {'title': '改訂版', 'like_count': 100}, format='json')
        self.assertEqual(self.client.get(self.url).data['like_count'], 3)
        response = self.client.post('/api/books/', {'title': '新刊', 'author': '著者', 'price': 100, 'like_count': 100}, format='json')
        self.assertEqual(response.data['like_count'], 0)
        response = self.client.get('/api/books/', {'ordering': '-like_count'})
        self.assertEqual(response.data[0]['id'], self.book.id)
        self.assertEqual(self.client.post('/api/books/999999/like/').status_code, 404)

    def test_sort_ties_and_empty_or_invalid_ordering(self):
        second = Book.objects.create(title='Vue入門', author='佐藤', price=1000)
        expected = [self.book.id, second.id]
        for ordering in ['price', '-price', 'title', '-title', '-like_count', '', 'author', 'price,-id']:
            with self.subTest(ordering=ordering):
                response = self.client.get('/api/books/', {'ordering': ordering})
                self.assertEqual(response.status_code, 200)
                self.assertEqual([row['id'] for row in response.data], expected)
        response = self.client.get('/api/books/', {'keyword': '該当なし', 'ordering': '-price'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, [])

    def test_like_ignores_client_count_and_survives_put(self):
        self.assertEqual(self.client.get(self.url + 'like/').status_code, 405)
        response = self.client.post(self.url + 'like/', {'like_count': 999}, format='json')
        self.assertEqual(response.data['like_count'], 1)
        response = self.client.put(self.url, {
            'title': '改訂版', 'author': '山田', 'price': 1000,
            'publisher': '', 'image_path': '', 'like_count': 999,
        }, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['like_count'], 1)

    def test_image_upload_and_book_registration(self):
        with TemporaryDirectory() as folder, override_settings(MEDIA_ROOT=folder):
            for image_format, content_type in [('PNG', 'image/png'), ('PNG', 'image/png'), ('JPEG', 'image/jpeg')]:
                content = BytesIO()
                Image.new('RGB', (4, 4), 'blue').save(content, format=image_format)
                upload = SimpleUploadedFile('cover.' + image_format.lower(), content.getvalue(), content_type=content_type)
                response = self.client.post('/api/books/upload-image/', {'image': upload}, format='multipart')
                self.assertEqual(response.status_code, 201)
                image_path = response.data['image_path']
                self.assertTrue(image_path.startswith('http://testserver/media/books/'))
                stored = Path(folder) / 'books' / image_path.rsplit('/', 1)[1]
                self.assertEqual(stored.read_bytes(), content.getvalue())
                response = self.client.post('/api/books/', {'title': '画像付き', 'author': '著者', 'price': 100, 'image_path': image_path}, format='json')
                self.assertEqual(response.status_code, 201)
                self.assertEqual(response.data['image_path'], image_path)
                self.assertEqual(self.client.patch(self.url, {'image_path': image_path}, format='json').status_code, 200)
            self.assertEqual(len(list(Path(folder).rglob('*.*'))), 3)

    def test_invalid_uploads_do_not_create_files_or_books(self):
        with TemporaryDirectory() as folder, override_settings(MEDIA_ROOT=folder):
            uploads = [SimpleUploadedFile('fake.png', b'not an image', content_type='image/png')]
            gif = BytesIO()
            Image.new('RGB', (4, 4)).save(gif, format='GIF')
            uploads.append(SimpleUploadedFile('cover.gif', gif.getvalue(), content_type='image/gif'))
            large = BytesIO()
            Image.new('RGB', (4, 4)).save(large, format='PNG')
            uploads.append(SimpleUploadedFile('large.png', large.getvalue() + b'0' * (5 * 1024 * 1024), content_type='image/png'))
            for upload in uploads:
                with self.subTest(filename=upload.name):
                    self.assertEqual(self.client.post('/api/books/upload-image/', {'image': upload}, format='multipart').status_code, 400)
            self.assertEqual(self.client.post('/api/books/upload-image/', {}, format='multipart').status_code, 400)
            self.assertEqual(list(Path(folder).rglob('*')), [])
            self.assertEqual(Book.objects.count(), 1)

    def test_upload_size_boundary_and_actual_image_format(self):
        with TemporaryDirectory() as folder, override_settings(MEDIA_ROOT=folder):
            content = BytesIO()
            Image.new('RGB', (4, 4), 'blue').save(content, format='PNG')
            # 5MBちょうどと1バイト超過を比較する。拡張子より実際の画像形式を優先する。
            data = content.getvalue().ljust(5 * 1024 * 1024, b'0')
            upload = SimpleUploadedFile('cover.jpg', data, content_type='image/jpeg')
            response = self.client.post('/api/books/upload-image/', {'image': upload}, format='multipart')
            self.assertEqual(response.status_code, 201)
            self.assertTrue(response.data['image_path'].endswith('.png'))
            upload = SimpleUploadedFile('large.png', data + b'0', content_type='image/png')
            self.assertEqual(self.client.post('/api/books/upload-image/', {'image': upload}, format='multipart').status_code, 400)
            self.assertEqual(self.client.post('/api/books/upload-image/', {'image': 'fake'}, format='json').status_code, 415)
            self.assertEqual(self.client.get('/api/books/upload-image/').status_code, 405)
            self.assertEqual(len(list(Path(folder).rglob('*.*'))), 1)
            self.assertEqual(Book.objects.count(), 1)
