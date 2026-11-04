# 書籍管理システム - フロントエンド（スターター）

[読みやすいPDF版を開く](README.pdf)（このMarkdownは更新用の原稿です）

Vue.js 3、TypeScript、Vite 7、Bootstrap 5を使用します。
画面・コンポーネントの枠組みを用意しています。画面の案内とソースコード内のコメントに従って実装してください。

セットアップ全体は[プロジェクトのREADME（PDF）](../README.pdf)を参照してください。
Node.jsは20.19以上の20系、または22.12以上が必要です。

VS Codeのエクスプローラーで、この `frontend` フォルダを右クリックし、「統合ターミナルで開く」を選びます。開いたターミナルで次を実行します。

```powershell
npm install
```

インストール完了後、このフォルダの `package.json` を開きます。エクスプローラー下部の「NPM スクリプト」で、そのファイルにある `dev` の再生ボタンをクリックすると、Viteの開発サーバーが起動します。

「NPM スクリプト」が見えない場合は、`Ctrl+Shift+P` →「表示: ビューを開く」→「NPM スクリプト」で表示します。

補足：コマンドで操作する場合は、このフォルダのターミナルで次を実行します。画面操作で起動済みの場合は、重ねて実行する必要はありません。

```powershell
npm install
npm run dev
```

アクセス先：`http://localhost:5173`

APIの接続先：`http://localhost:8000/api/books/`

ビルドの確認は `npm run build` で行います。
