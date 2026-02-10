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

バックエンド用のDjangoディレクトリと、DB作成用sqlだけ準備してあります。
以下の手順に従いセットアップを行ってください。

1. **ディレクトリ移動**

   ```bash
   cd backend-django
   ```

2. **Djangoプロジェクトの作成**  
   Djangoプロジェクトを作成します。

   ```bash
   django-admin startproject config .
   ```

3. **アプリケーションの作成**  
   書籍管理用のアプリ `books` を作成します。

   ```bash
   python manage.py startapp books
   ```

4. **ディレクトリ構成 (Backend)**  
   以下のディレクトリ構成になっていることを確認してください。
   (実行結果は一部省略して表示しています)

   ```bash
   tree /f ./
   ```

   ```bash
   backend-django
   │  initial_data.sql
   │  manage.py
   │
   ├─books
   │  │  models.py
   │  │  views.py
   │  │
   │  └─migrations
   │
   └─config
      │  settings.py
      └─ urls.py
   ```

5. **設定の追加**  
   `config/settings.py` に必要な情報を追加してください。  

   - `INSTALLED_APPS`にアプリを追加
     - `rest_framework`  # 追加: REST API用
     - `corsheaders`     # 追加: CORS用
     - `books`           # 新規: 書籍管理アプリ

   - `MIDDLEWARE`にCORSの設定を先頭に追加
     - `corsheaders.middleware.CorsMiddleware`

   - `CORS_ALLOWED_ORIGINS`を定義して、オリジンサーバを追加
     - `http://localhost:5173`
     - `http://localhost:5174`
     - `http://localhost:5175`

6. **モデルの作成**  
   テーブル定義を基にモデルを作成してください。以下に注意して作成します。
   - ID列は自動生成とし、フィールド定義は不要です。
   - nullableとはNullを許可する設定で、「null=True, blank=True」の設定で実現します。
   - テーブル名は'books'とします。アプリケーション名がつかないように注意してください。(Djangoのデフォルトは「アプリ名_テーブル名」で生成)  

7. **データベースのマイグレーション**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

8. **初期データの投入 (SQL)**  
   `backend-django` フォルダに `initial_data.sql` が用意されています。
   SQLite3 コマンドラインツールでデータを投入してください。
   データ投入後、テーブルのレコードが表示されるため、確認してください。

   ```bash
   sqlite3 db.sqlite3
   .read initial_data.sql
   .quit
   ```

9. **サーバー起動**

   ```bash
   python manage.py runserver
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
   アクセス: <http://localhost:5173>

   画面に表示される指示（コメント）に従って、実装を進めてください。

## 補足

- APIの仕様や画面設計については、別途配布される設計書を確認してください。
