import { createRouter, createWebHistory } from 'vue-router'
import BookListView from '../views/BookListView.vue'
// TODO: 追加する画面のコンポーネントをimportしてください。

/**
 * ルーティング設定 (Vue Router)
 * 
 * 画面遷移の定義を行います。
 * URLパスと、そのパスで表示すべきVueコンポーネントを紐付けています。
 * 一覧画面をサンプルとして用意しています。他の画面は設計書を確認して追加してください。
 * 
 * historyモード: createWebHistory() を使用して、通常のURL形式 (例: /books/1) をサポートします。
 */
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      // ルートパス ('/') へのアクセス設定
      // アプリケーションのトップページにアクセスされた際、
      // 自動的に書籍一覧ページ ('/books') へ転送（リダイレクト）します。
      path: '/',
      redirect: '/books'
    },
    {
      // 書籍一覧画面
      // URL: /books
      // 一覧画面コンポーネント (BookListView) を表示します。
      path: '/books',
      name: 'books',
      component: BookListView
    }
    // TODO: 新規登録・編集・詳細のルートをここに追加してください。
    // 一覧画面の例を参考に、path・name・componentを設定します。
    // 編集・詳細で書籍IDを受け取る方法も、設計書と学習済みテキストを確認してください。
  ]
})

export default router
