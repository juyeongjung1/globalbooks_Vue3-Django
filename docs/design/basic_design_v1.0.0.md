# 書籍管理システム 基本設計書

**バージョン**: v1.0.0  
**作成日**: 2026/01/27

## 1. アーキテクチャ構成
本システムは、FrontendとBackendを分離したSPA（Single Page Application）構成とする。

```mermaid
graph LR
    User[ユーザー] --> Frontend[Frontend (Vue 3)]
    Frontend -- API Request (JSON) --> Backend[Backend (Django REST Framework)]
    Backend -- Query --> DB[(Database (SQLite))]
```

## 2. データベース設計

### 2.1 テーブル定義: books
`db_table` は `books` とする（旧 `employees`）。

| カラム名 | 論理名 | データ型 | 制約 | 説明 |
| --- | --- | --- | --- | --- |
| id | ID | Integer | PK, AutoIncrement | 自動採番 |
| title | 書籍名 | CharField | max_length=255, Not Null | 旧: name |
| author | 著者名 | CharField | max_length=255, Not Null | 旧: password |
| price | 価格 | Integer | Not Null | 旧: salary |
| publisher | 出版社 | CharField | max_length=255, Nullable | 旧: location_name |
| image_path | 画像パス | CharField | max_length=255, Nullable | 旧: image_path |
| created_at | 作成日時 | DateTime | AutoNowAdd | (新規追加検討) |
| updated_at | 更新日時 | DateTime | AutoNow | (新規追加検討) |

※ `created_at`, `updated_at` は既存になければ追加を推奨するが、既存流用を最優先する場合は省略可能とする。（今回は要件に「ほぼ100%同じ」とあるため、既存にない場合は必須ではないが、管理上あると望ましい。一旦既存項目のみで構成する）

## 3. API設計 (RESTful API)

| メソッド | エンドポイント | 概要 | リクエストパラメータ | レスポンス |
| --- | --- | --- | --- | --- |
| GET | `/api/books/` | 書籍一覧取得 | `keyword` (optional): タイトル検索用 | 書籍オブジェクト配列 |
| POST | `/api/books/` | 書籍新規登録 | `title`, `author`, `price`, `publisher`, `image_path` | 作成された書籍オブジェクト |
| GET | `/api/books/{id}/` | 書籍詳細取得 | - | 書籍オブジェクト |
| PUT/PATCH | `/api/books/{id}/` | 書籍更新 | (変更項目) | 更新後の書籍オブジェクト |
| DELETE | `/api/books/{id}/` | 書籍削除 | - | 204 No Content |

## 4. Frontend画面設計

### 4.1 画面一覧
1. **書籍一覧画面 (BookListView)**
   - 既存の `EmployeeListView.vue` を改修。
   - 検索フォーム（タイトル検索）。
   - 一覧テーブル（タイトル, 著者, 価格, 出版社）。
   - 「新規登録」ボタン。

2. **書籍詳細画面 (BookDetailView)**
   - 既存の `EmployeeDetailView.vue` を改修。
   - 書籍情報の表示。
   - 「編集」「削除」ボタン。

3. **書籍登録・編集画面 (BookEditView / NewBookView)**
   - 既存の `EmployeeEditView.vue`, `NewEmployeeView.vue` を改修。
   - 入力フォーム（タイトル, 著者, 価格, 出版社, 画像パス）。

### 4.2 ディレクトリ構成変更案
```
frontend/src/views/
  ├── BookListView.vue      (旧 EmployeeListView.vue)
  ├── BookDetailView.vue    (旧 EmployeeDetailView.vue)
  ├── BookEditView.vue      (旧 EmployeeEditView.vue)
  └── NewBookView.vue       (旧 NewEmployeeView.vue)
```
※ ファイル名もリファクタリングを行うことが望ましい。
