# 書籍管理システム (Global Books Vue3-Django) - スターターキット

これは、Vue.js 3とDjango REST Frameworkを使用して書籍管理システムを構築するためのスターターキットです。
フロントエンドの基本的なプロジェクト構成や設定は完了していますが、主要な機能は未実装です。
以下の手順に従って、開発を進めてください。

## 機能要件（実装目標）

- 書籍一覧表示（画像付き）
- 書籍詳細表示
- 新規書籍登録
- 書籍編集
- 書籍削除

基本課題の完成後、[基本設計書の第7章「追加機能」](docs/基本設計/基本設計書_v1.1.0.md#7-追加機能)の並び替え・いいね・画像ファイル添付に任意で取り組めます。

## 技術スタック

- Frontend：Vue.js 3、Vite 7、Bootstrap 5
- Backend：Django 5、Django REST Framework
- Database：SQLite3

## セットアップ & 開発手順

### 前提条件

- Python 3.10以上（演習環境は3.13）
- Node.js 20.19以上の20系、または22.12以上（Vite 7の必要条件）
- Django 5.2系、Django REST Framework 3.16.1、django-cors-headers 4.9.0をインストール済みであること
- SQLite3コマンドラインツールをインストールし、`sqlite3` コマンドを実行できること

### 1. バックエンド (Django) のセットアップ

バックエンド用の `backend-django` ディレクトリと、初期データ投入用の `initial_data.sql` だけを準備してあります。
以下の手順に従い、プロジェクトの作成からセットアップを行ってください。

#### 1. ディレクトリ移動

このREADMEのあるフォルダから実行します。

```powershell
cd backend-django
```

以降、バックエンドのコマンドはこのフォルダで実行します。

#### 2. Djangoプロジェクトの作成

Djangoプロジェクト `config` を作成します。

```powershell
django-admin startproject config .
```

#### 3. アプリケーションの作成

書籍管理用のアプリ `books` を作成します。

```powershell
python manage.py startapp books
```

#### 4. ディレクトリ構成 (Backend)

以下のディレクトリ構成になっていることを確認してください。
実行結果は一部省略しています。

```powershell
tree /f ./
```

```text
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

#### 5. 設定の追加

`config/settings.py` に必要な情報を追加してください。

- `INSTALLED_APPS` に `'rest_framework'`（REST API用）、`'corsheaders'`（CORS用）、`'books'`（書籍管理アプリ）を追加する。
- `MIDDLEWARE` の先頭に `'corsheaders.middleware.CorsMiddleware'` を追加する。
- `CORS_ALLOWED_ORIGINS` を定義し、以下のオリジンを追加する。

```python
CORS_ALLOWED_ORIGINS = [
    'http://localhost:5173',
    'http://localhost:5174',
    'http://localhost:5175',
]
```

#### 6. モデルの作成

設計書のテーブル定義を基にモデルを作成してください。以下に注意して作成します。

- ID列は自動生成とし、フィールド定義は不要です。
- nullableとはnullを許可する設定で、`null=True, blank=True` の設定で実現します。
- テーブル名は `books` とします。モデル内の `class Meta` に `db_table = 'books'` を指定し、アプリケーション名が付かないようにしてください。Djangoのデフォルトは「アプリ名_モデル名」です。

いいね数の列は、オプションに取り組むかどうかにかかわらず最初から用意します。`Book` モデル内に、次の定義をそのまま追加してください。初期SQLでも0が設定されるため、後から列を追加する作業は不要です。

```python
like_count = models.PositiveIntegerField(default=0)
```

`BookSerializer` の `class Meta` には `read_only_fields = ['like_count']` を指定します。登録・編集フォームにいいね数の入力欄は作りません。

#### 7. データベースのマイグレーション

モデルを実装した後に実行します。

```powershell
python manage.py makemigrations
python manage.py migrate
```

#### 8. 初期データの投入 (SQL)

`backend-django` フォルダに `initial_data.sql` が用意されています。
書籍テーブルが空の状態で、SQLite3コマンドラインツールを使って初回だけ投入してください。
SQLの末尾にあるSELECTにより、投入した10件のレコードが表示されます。

```text
sqlite3 db.sqlite3
.read initial_data.sql
.quit
```

`.read` と `.quit` は、`sqlite3 db.sqlite3` で開いたSQLiteのプロンプト内で入力します。

#### 9. サーバー起動

```powershell
python manage.py runserver
```

Djangoの標準ポート8000で起動します。
APIの実装は設計書に従い、`books/serializers.py`、`books/views.py`、`config/urls.py` に追加してください。
実装後の確認先は `http://localhost:8000/api/books/` です。

### 2. フロントエンド (Vue) のセットアップ

フロントエンドは、必要な画面やコンポーネントのファイル（枠組み）のみ用意されています。

#### 1. ディレクトリ移動とインストール

別のターミナルを開き、このREADMEのあるフォルダから実行します。

```powershell
cd frontend
npm install
```

#### 2. 開発サーバー起動

```powershell
npm run dev
```

#### 3. ブラウザで確認

アクセス先：`http://localhost:5173`

画面の案内と各Vueファイル内のコメントに従って、実装を進めてください。
一覧画面の初期案内は、書籍一覧を実装する際に置き換えます。

## 補足

APIの仕様や画面設計については、設計書を確認してください。
実装時は、学習済みの参考用 `ch05-crud` の書き方に合わせます。

- [要件定義書](docs/要件定義/要件定義書_v1.1.0.md)
- [基本設計書](docs/基本設計/基本設計書_v1.1.0.md)
- [基本設計書PDF](docs/基本設計/基本設計書_v1.1.0.pdf)
- [追加機能（基本設計書 第7章・任意課題）](docs/基本設計/基本設計書_v1.1.0.md#7-追加機能)
