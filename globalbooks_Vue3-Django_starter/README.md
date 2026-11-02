# 書籍管理システム - スターターキット

Vue 3とDjango REST Frameworkで書籍管理システムを作る総合演習です。
プロジェクト設定・画面ファイル・ルーター・表紙画像を用意しています。
書籍のCRUD・検索、共通メニューなどの処理は、受講者が実装してください。

## 使用する資料と書き方

- [要件定義書 v1.1.0](docs/要件定義/要件定義書_v1.1.0.md)
- [基本設計書 v1.1.0](docs/基本設計/基本設計書_v1.1.0.md)
- [基本設計書PDF](docs/基本設計/基本設計書_v1.1.0.pdf)
- 学習済みテキストの `ch05-crud` のソースコード

Vueはテキストと同じ `<script setup lang="ts">`、項目ごとの `ref`、`onMounted`、Axios、`try/catch`、Vue Routerを使用します。
エラーメッセージは `error` に保持し、`v-if` で画面内に表示します。
APIの成功時は `alert()`、削除確認は `confirm()` を使います。

テキストのExpressサーバーは、この演習ではDjango REST Frameworkに置き換えます。

| Django側のファイル | 担当する処理 |
| --- | --- |
| `books/models.py` | 書籍テーブルの項目・型・テーブル名 |
| `books/serializers.py` | JSONへの変換と入力値の検証 |
| `books/views.py` | CRUDと書籍名の部分一致検索 |
| `myproject/urls.py` | APIのURL登録 |

## 前提条件

- Python 3.13
- Node.js 22.12以上の22系、または24系を推奨
- Vite 7の最低要件はNode.js 20.19以上の20系、または22.12以上。Node.js 16・18は使用できません
- Backend：Django 5.2系、Django REST Framework 3.16.1、django-cors-headers 4.9.0
- DB：SQLite3

以下はWindowsのPowerShell用です。仮想環境のPythonを直接実行するため、実行ポリシーの変更は不要です。
macOS/Linuxでは `.venv/Scripts/python.exe` の代わりに `.venv/bin/python` を使い、パス区切りをスラッシュにしてください。

## 1. バックエンドの準備と実装

### 1.1 仮想環境とパッケージ

このREADMEのあるフォルダから実行します。

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r backend-django\requirements.txt
cd backend-django
```

以降、バックエンドのコマンドは `backend-django` フォルダで実行します。

### 1.2 booksアプリの作成・登録

```powershell
..\.venv\Scripts\python.exe manage.py startapp books
```

`myproject/settings.py` の `INSTALLED_APPS` に `'books'` を追加します。
`rest_framework` と `corsheaders` は登録済みです。

### 1.3 Bookモデルの実装

基本設計書のテーブル定義に従って、`books/models.py` に `Book` モデルを実装します。
タイトル・著者名・価格・出版社・画像パスを定義し、任意項目には `null=True, blank=True` を指定します。
テーブル名を初期SQLと合わせるため、モデル内の `class Meta` に `db_table = 'books'` を指定してください。

**モデルを実装した後**に、マイグレーションの作成・適用を行います。

```powershell
..\.venv\Scripts\python.exe manage.py makemigrations books
..\.venv\Scripts\python.exe manage.py migrate
```

`startapp` と `migrate` だけでは書籍テーブルは作成されません。

### 1.4 初期データの投入

書籍テーブルができてから、付属のスクリプトで `initial_data.sql` を実行します。
Python標準のSQLite機能を使うため、sqlite3コマンドの別途インストールは不要です。

```powershell
..\.venv\Scripts\python.exe import_initial_data.py
```

初期書籍10件が登録されます。書籍が登録済みの場合は停止し、既存データは変更しません。
`no such table: books` の場合は、モデル・`db_table`・マイグレーションを確認してください。

### 1.5 APIの実装

次の順序で実装します。

1. `books/serializers.py` を作成し、`ModelSerializer` を継承する `BookSerializer` を定義する。対象モデルは `Book`、項目は全項目。`Meta.extra_kwargs` で価格の `min_value` を1に設定する。
2. `books/views.py` で `ModelViewSet` を継承する `BookViewSet` を定義する。全書籍のQuerySetとSerializerを指定する。
3. `get_queryset()` で `keyword` を受け取り、指定されている場合は `title__icontains` で絞り込む。未指定・空文字は全件取得する。
4. `myproject/urls.py` で `BookViewSet` をインポートし、用意された `router.register` のコメントを外して登録する。

### 1.6 APIの起動・確認

```powershell
..\.venv\Scripts\python.exe manage.py check
..\.venv\Scripts\python.exe manage.py runserver 8000
```

- `http://localhost:8000/api/books/`：書籍10件を確認
- `http://localhost:8000/api/books/?keyword=Vue`：書籍名で絞り込み
- `http://localhost:8000/api/books/1/`：1件の詳細を確認

APIのURL末尾には `/` を付けます。API実装前の `/api/books/` は404で正常です。

## 2. フロントエンドの準備と実装

### 2.1 起動確認

別のターミナルを開き、このREADMEのあるフォルダから実行します。

```powershell
cd frontend
npm ci
npm run dev
```

`http://localhost:5173` を開き、「スターターキット」の案内が表示されれば起動成功です。
5173番ポートが使用中の場合は、先に使用中の開発サーバーを終了してください。
各ファイルの実装ヒントは画面ではなく、ソースコード内のコメントに記載しています。

### 2.2 実装の順序

| 順序 | 実装対象 | 参考にするテキストのソース |
| --- | --- | --- |
| 1 | `HeaderMenu.vue`、`SideMenu.vue`、`FooterInfo.vue` | 同名の共通コンポーネント |
| 2 | `BookListView.vue` の一覧取得 | `ProductListView.vue` |
| 3 | `BookListView.vue` の検索・0件表示 | `ProductListView2.vue` |
| 4 | `BookDetailView.vue` の詳細表示 | `ProductDetailView.vue` |
| 5 | `NewBookView.vue` の登録 | `NewProductView.vue` |
| 6 | `BookEditView.vue` の取得・更新 | `ProductEditView.vue` |
| 7 | `BookDetailView.vue` の削除 | `ProductDetailView.vue` |

`App.vue` とルーターは設定済みです。編集画面のURLは `/books/edit/:id` を使います。
一覧の初期案内は、実装した一覧に置き換えてください。

### 2.3 入力・表示の注意点

- 商品の `name` を書籍の `title` に読み替え、`author`、`publisher`、`image_path` を追加する。
- APIは `http://localhost:8000/api/books/` を使う。参考用の3000番ポートではない。
- 価格は登録・編集とも1以上の整数。`min="1"`、`step="1"` と送信前チェックを使う。
- 書籍名・著者名は必須で、空白だけの入力も拒否する。文字列項目は最大255文字。
- `public/images/1.png` の画像は `/images/1.png` と入力する。画像URLも利用できる。未指定の場合は `v-if` / `v-else` で「画像なし」と表示する。
- 編集のPUTではタイトル・著者名・価格を含む5項目を送信する。変更項目だけの更新はPATCHであり、本演習の画面では使用しない。
- 登録後は一覧、更新後は詳細、削除後は一覧へ遷移する。キャンセルは新規登録では一覧、編集では詳細へ戻る。

## 3. 完成時の確認

- 一覧・検索・詳細・登録・編集・削除が動作する
- 検索0件、画像未指定、取得中、通信エラーを表示できる
- 価格0・負数・小数、必須項目未入力は保存できない
- 削除確認でキャンセルした場合は削除しない
- `npm run build` が成功する

このキットは未実装の演習用です。解答コードやGit履歴は配布物に含めません。
