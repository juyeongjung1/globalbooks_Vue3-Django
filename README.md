# 書籍管理システム (Global Books Vue3-Django) - スターターキット

これは、Vue.js 3 と Django REST Framework を使用して書籍管理システムを構築するためのスターターキットです。
基本的なプロジェクト構成や設定は完了していますが、主要な機能は未実装です。
以下の手順に従って、開発を進めてください。

## 機能要件 (実装目標)
- 書籍一覧表示（画像付き）
- 書籍詳細表示
- 新規書籍登録
- 書籍編集
- 書籍削除

## 技術スタック
- **Frontend**: Vue.js 3, Vite, Bootstrap 5
- **Backend**: Django 5, Django REST Framework
- **Database**: SQLite3

## セットアップ & 開発手順

### 前提条件
- Python 3.10+
- Node.js 16+

### 1. バックエンド (Django) のセットアップ

Djangoプロジェクトは初期化済みですが、アプリケーションロジックは実装されていません。
`rest_framework` と `corsheaders` の設定は `settings.py` に記述済みです。

1. **ディレクトリ移動とパッケージインストール**
   ```bash
   cd backend-django
   pip install -r requirements.txt
   ```

2. **アプリケーションの作成**
   まず、書籍管理用のアプリ `books` を作成します。
   ```bash
   python manage.py startapp books
   ```

3. **アプリの登録**
   `myproject/settings.py` の `INSTALLED_APPS` に `'books'` を追加してください。

4. **データベースのマイグレーション**
   ```bash
   python manage.py migrate
   ```

5. **サーバー起動**
   ```bash
   python manage.py runserver 8001
   ```

### 2. フロントエンド (Vue) のセットアップ

フロントエンドは、必要な画面やコンポーネントのファイル（枠組み）のみ用意されています。

1. **ディレクトリ移動とインストール**
   ```bash
   cd frontend
   npm install
   ```

2. **開発サーバー起動**
   ```bash
   npm run dev
   ```

3. **ブラウザで確認**
   アクセス: http://localhost:5173

   画面に表示される指示（コメント）に従って、実装を進めてください。

## 補足
- 完成版のコードは `globalbooks_Vue3-Django` リポジトリ（または解答フォルダ）を参照してください。
- APIの仕様や画面設計については、別途配布される設計書を確認してください。
