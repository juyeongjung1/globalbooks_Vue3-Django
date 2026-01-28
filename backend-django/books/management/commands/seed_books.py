from django.core.management.base import BaseCommand
from books.models import Book

class Command(BaseCommand):
    help = 'Seed database with initial book data'

    def handle(self, *args, **kwargs):
        # 既存データのクリア
        Book.objects.all().delete()
        self.stdout.write('Cleared existing books.')

        # サンプルデータ作成
        books = [
            {'id': 1, 'title': 'Pythonの教科書', 'author': '山田 太郎', 'price': 2500, 'publisher': '技術書院', 'image_path': '/images/1.png'},
            {'id': 2, 'title': 'Vue.js入門', 'author': '山田 太郎', 'price': 3000, 'publisher': '技術評論社', 'image_path': '/images/2.png'},
            {'id': 3, 'title': 'Django開発', 'author': '佐藤 健一', 'price': 2800, 'publisher': '技術評論社', 'image_path': '/images/3.png'},
            {'id': 4, 'title': 'JavaScript完全', 'author': '山田 太郎', 'price': 3200, 'publisher': '技術評論社', 'image_path': '/images/4.png'},
            {'id': 5, 'title': 'AIの基礎', 'author': '田中 未来', 'price': 3500, 'publisher': '未来技術社', 'image_path': '/images/5.png'},
            {'id': 6, 'title': 'React実践', 'author': '伊藤 さくら', 'price': 3100, 'publisher': '技術評論社', 'image_path': '/images/6.png'},
            {'id': 7, 'title': 'Go言語', 'author': '渡辺 剛', 'price': 3400, 'publisher': '技術評論社', 'image_path': '/images/7.png'},
            {'id': 8, 'title': 'Docker活用', 'author': '山田 太郎', 'price': 2900, 'publisher': 'クラウド書房', 'image_path': '/images/8.png'},
            {'id': 9, 'title': 'AWS構築', 'author': '山田 太郎', 'price': 3800, 'publisher': 'インフラ技術社', 'image_path': '/images/9.png'},
            {'id': 10, 'title': 'アジャイル', 'author': '吉田 チーム', 'price': 2600, 'publisher': 'J-TECH', 'image_path': '/images/10.png'},
        ]

        for book_data in books:
            Book.objects.create(**book_data)
        
        self.stdout.write(self.style.SUCCESS(f'Successfully created {len(books)} books with starting ID 1.'))
