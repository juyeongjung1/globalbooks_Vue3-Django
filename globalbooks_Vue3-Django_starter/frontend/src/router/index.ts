import { createRouter, createWebHistory } from 'vue-router'
import BookListView from '../views/BookListView.vue'
import BookDetailView from '../views/BookDetailView.vue'
import NewBookView from '../views/NewBookView.vue'
import BookEditView from '../views/BookEditView.vue'

/**
 * ルーティング設定 (Vue Router)
 * 
 * 画面遷移の定義を行います。
 * URLパスと、そのパスで表示すべきVueコンポーネントを紐付けています。
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
    },
    {
      // 新規書籍登録画面
      // URL: /books/new
      // 新規登録フォーム (NewBookView) を表示します。
      path: '/books/new',
      name: 'book-new',
      component: NewBookView
    },
    {
      // 書籍編集画面
      // URL: /books/edit/:id
      // :id は「動的ルートパラメータ」です。
      // URLのこの部分に入力された値（書籍ID）は、コンポーネント内で route.params.id として取得できます。
      // 例: /books/edit/3 -> id=3 の書籍を編集
      path: '/books/edit/:id',
      name: 'book-edit',
      component: BookEditView
    },
    {
      // 書籍詳細画面
      // URL: /books/:id
      // 詳細確認用の画面 (BookDetailView) を表示します。
      // 編集画面と同様に、:id 部分で書籍IDを受け取ります。
      // 例: /books/5 -> id=5 の書籍詳細を表示
      path: '/books/:id',
      name: 'book-detail',
      component: BookDetailView
    }
  ]
})

export default router