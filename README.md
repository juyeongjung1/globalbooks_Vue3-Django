# 書籍管理システム (Global Books Vue3-Django)

Vue 3とDjango REST Frameworkを使用した、総合演習の解答例です。
学習済みテキストの `ref`、`onMounted`、Axios、Vue Routerを使った書き方に合わせています。

## 機能

- 書籍一覧・書籍名での部分一致検索・詳細表示
- 書籍の登録・編集・削除
- 価格は1以上の整数。入力不備や通信エラーは画面内に表示
- 表紙画像は任意。未指定の場合は「画像なし」と表示

## 構成

- `frontend/`：Vue 3 + TypeScript + Vite 7 + Bootstrap 5の解答
- `backend-django/`：Django 5.2系 + Django REST Framework 3.16.1の解答。プロジェクト名は `config`、アプリ名は `books`
- `docs/`：要件定義書・基本設計書（v1.1.0）
- `globalbooks_Vue3-Django_starter/`：受講者用の未実装キット。バックエンドはフォルダと初期SQLのみ

## 前提条件

- Python 3.10以上（演習環境は3.13）
- Node.js 20.19以上の20系、または22.12以上（Vite 7の必要条件）
- SQLite3コマンドラインツール（初期SQLを投入する場合）

## セットアップ

以下はこのREADMEのあるフォルダから実行します。
解答には `config` プロジェクトと `books` アプリが含まれています。
受講者がプロジェクト作成から進める手順は、[スターターREADME](globalbooks_Vue3-Django_starter/README.md)を参照してください。

### バックエンド

```powershell
cd backend-django
python -m pip install -r requirements.txt
python manage.py migrate
```

同梱の `db.sqlite3` にはサンプル書籍が入っています。
新しい空のDBを使用する場合だけ、SQLite3コマンドラインツールで初期データを投入します。
`.read` と `.quit` は、SQLiteのプロンプト内で入力します。投入後に10件のレコードが表示されます。

```text
sqlite3 db.sqlite3
.read initial_data.sql
.quit
```

APIサーバーを起動します。

```powershell
python manage.py runserver
```

標準ポート8000で起動します。APIの確認先：`http://localhost:8000/api/books/`

### フロントエンド

別のターミナルを開き、このREADMEのあるフォルダから実行します。

```powershell
cd frontend
npm install
npm run dev
```

アクセス先：`http://localhost:5173/books`。5173番ポートが使用中の場合は、先に使用中の開発サーバーを終了してください。

## 検証

バックエンドは `backend-django`、フロントエンドは `frontend` フォルダで、それぞれ実行します。

```powershell
python manage.py test books
```

```powershell
npm run build
```

テストではCRUD、検索、価格・必須項目・文字数、PUTとPATCHの違い、既存の初期データコマンドの動作を確認します。

## 教材

- [要件定義書](docs/要件定義/要件定義書_v1.1.0.md)
- [基本設計書](docs/基本設計/基本設計書_v1.1.0.md)
- [基本設計書PDF](docs/基本設計/基本設計書_v1.1.0.pdf)
- [受講者用セットアップ手順](globalbooks_Vue3-Django_starter/README.md)

受講者へはスターターだけを配布します。リポジトリ全体には解答が含まれます。
配布用ZIPは、このREADMEのあるフォルダで `python scripts/package_starter.py` を実行すると作成できます。
Git履歴、仮想環境、依存パッケージ、生成物、DB、確認用の原本PDFは含めません。

本教材はローカル環境での演習用です。
