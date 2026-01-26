# Django Backend (Non-Virtual Environment)

このプロジェクトは、Python の仮想環境 (venv) を使用せずに、システム環境で直接実行するように構成されています。

## セットアップと実行方法

1.  **依存ライブラリのインストール**
    以下のコマンドを実行して、必要なパッケージをユーザー環境にインストールします（管理者権限不要）。
    ```bash
    pip install --user -r requirements.txt
    ```

2.  **サーバーの起動**
    以下のコマンドでサーバーを起動します。ポートは `8001` を使用するように設定されています（Expressサーバーとの競合を避けるため）。
    ```bash
    python manage.py runserver 8001
    ```
    または、同梱の `run_django.bat` をダブルクリックして実行することも可能です。

## 注意事項
- フロントエンドからこの Django API を利用する場合は、フロントエンド側の API エンドポイント URL を `http://localhost:8001/api/employees/` に変更する必要があります。
- 現在の Vue のソースコードはデフォルトで Express バックエンド (`http://localhost:3000`) を参照しています。
