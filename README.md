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
- `backend-django/`：Django 5.2系 + Django REST Framework 3.16.1の解答
- `docs/`：要件定義書・基本設計書（v1.1.0）
- `globalbooks_Vue3-Django_starter/`：受講者用の未実装キット

## 前提条件

- Python 3.12推奨（Django 5.2の対応範囲は3.10～3.14）
- Node.js 22.12以上の22系、または24系を推奨
- Vite 7の最低要件はNode.js 20.19以上の20系、または22.12以上。Node.js 16・18は対象外

## セットアップ（Windows / PowerShell）

以下はこのREADMEのあるフォルダから実行します。
仮想環境のPythonを直接指定するため、PowerShellの実行ポリシー変更は不要です。

### バックエンド

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r backend-django\requirements.txt
.\.venv\Scripts\python.exe backend-django\manage.py migrate
```

同梱の `db.sqlite3` にはサンプル書籍が入っています。
新しい空のDBを使用する場合だけ、次のコマンドで10件の初期データを投入します。
書籍が登録済みの場合、コマンドは停止し、既存データを変更しません。

```powershell
.\.venv\Scripts\python.exe backend-django\manage.py seed_books
```

APIサーバーを起動します。

```powershell
.\.venv\Scripts\python.exe backend-django\manage.py runserver 8001
```

APIの確認先：`http://localhost:8001/api/books/`

### フロントエンド

別のターミナルを開き、このREADMEのあるフォルダから実行します。

```powershell
cd frontend
npm ci
npm run dev
```

アクセス先：`http://localhost:5173/books`。5173番ポートが使用中の場合は、先に使用中の開発サーバーを終了してください。

macOS/Linuxでは `.venv/bin/python` を使用します。各コマンドのパス区切りをスラッシュに置き換えて実行してください。

## 検証

```powershell
.\.venv\Scripts\python.exe backend-django\manage.py test books
cd frontend
npm run build
```

テストではCRUD、検索、価格・必須項目・文字数、PUTとPATCHの違い、初期データ再投入時の既存データ保護を確認します。

## 教材

- [要件定義書](docs/要件定義/要件定義書_v1.1.0.md)
- [基本設計書](docs/基本設計/基本設計書_v1.1.0.md)
- [基本設計書PDF](docs/基本設計/基本設計書_v1.1.0.pdf)
- [受講者用セットアップ手順](globalbooks_Vue3-Django_starter/README.md)

受講者へはスターターだけを配布します。リポジトリ全体には解答が含まれます。
配布用ZIPは `python scripts/package_starter.py` で作成できます。Git履歴、仮想環境、依存パッケージ、生成物、DBは含めません。

本教材はローカル環境での演習用です。
