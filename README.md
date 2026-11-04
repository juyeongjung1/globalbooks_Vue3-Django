# 書籍管理システム (Global Books Vue3-Django)

[読みやすいPDF版を開く](README.pdf)（このMarkdownは更新用の原稿です）

Vue 3とDjango REST Frameworkを使用した、総合演習の解答例です。
学習済みテキストの `ref`、`onMounted`、Axios、Vue Routerを使った書き方に合わせています。

## 機能

- 書籍一覧・書籍名での部分一致検索・詳細表示
- 書籍の登録・編集・削除
- 価格は1以上の整数。入力不備や通信エラーは画面内に表示
- 表紙画像は任意。未指定の場合は「画像なし」と表示

解答には、[基本設計書の第7章「追加機能」](docs/基本設計/基本設計書_v1.1.0.pdf)で扱う3つの任意課題も含みます。基本課題の完成後に選択して取り組みます。

- ID・価格・書籍名・いいね数の並び替え
- 書籍ごとのいいね（何回でも追加可能）
- JPEG・PNGの画像ファイル添付（5MB以下）

`like_count` は追加機能専用の列です。基本機能では使用せず、後から列を追加する作業を避けるため初期状態から0で用意します。画像はDjangoが `backend-django/media/books/` に保存し、URLを既存の `image_path` に保持します。画像用テーブル・列は追加しません。

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
受講者がプロジェクト作成から進める手順は、[スターターREADME（PDF）](globalbooks_Vue3-Django_starter/README.pdf)を参照してください。

### バックエンド

```powershell
cd backend-django
python -m pip install -r requirements.txt
python manage.py migrate
```

既存環境もこの `migrate` でいいね数の列を追加できます。書籍データは保持されます。画像添付の検証に必要なPillowは `requirements.txt` に含まれています。

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

Djangoのサーバーは起動したままにします。VS Codeのエクスプローラーで、解答側の `frontend` フォルダを右クリックし、「統合ターミナルで開く」を選びます。開いたターミナルで次を実行します。

```powershell
npm install
```

インストール完了後、解答側の `frontend/package.json` を開きます。エクスプローラー下部の「NPM スクリプト」で、そのファイルにある `dev` の再生ボタンをクリックすると、Viteの開発サーバーが起動します。

「NPM スクリプト」が見えない場合は、`Ctrl+Shift+P` →「表示: ビューを開く」→「NPM スクリプト」で表示します。

補足：コマンドで操作する場合は、別のターミナルで、このREADMEのあるフォルダから次を実行します。画面操作で起動済みの場合は、重ねて実行する必要はありません。

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

テストではCRUD、検索、入力検証、PUTとPATCH、並び替え、いいね、画像アップロードの正常・異常入力を確認します。

## 教材

- [要件定義書（PDF）](docs/要件定義/要件定義書_v1.1.0.pdf)
- [基本設計書（PDF）](docs/基本設計/基本設計書_v1.1.0.pdf)
- [基本設計書（編集用Markdown）](docs/基本設計/基本設計書_v1.1.0.md)
- [追加機能（基本設計書 第7章・任意課題）](docs/基本設計/基本設計書_v1.1.0.pdf)
- [受講者用セットアップ手順（PDF）](globalbooks_Vue3-Django_starter/README.pdf)

受講者へはスターターだけを配布します。リポジトリ全体には解答が含まれます。
配布用ZIPは、このREADMEのあるフォルダで `python scripts/package_starter.py` を実行すると作成できます。
Git履歴、仮想環境、依存パッケージ、ビルド生成物、DB、アップロード画像、確認用の原本PDFは含めません。

本教材はローカル環境での演習用です。
