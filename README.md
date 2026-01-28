# 書籍管理システム (Global Books Vue3-Django)

Vue.js 3 と Django REST Framework を使用した書籍管理システムです。

## 機能
- 書籍一覧表示（画像付き）
- 書籍詳細表示
- 新規書籍登録
- 書籍編集
- 書籍削除

## 技術スタック
- **Frontend**: Vue.js 3, Vite, Bootstrap 5
- **Backend**: Django 5, Django REST Framework
- **Database**: SQLite3

## セットアップ手順

### 前提条件
- Python 3.10+
- Node.js 16+

### バックエンド (Django)
```bash
cd backend-django
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_books  # 初期データ投入
python manage.py runserver 8001
```

### フロントエンド (Vue)
```bash
cd frontend
npm install
npm run dev
```

アクセス: http://localhost:5173 (または表示されるポート)
