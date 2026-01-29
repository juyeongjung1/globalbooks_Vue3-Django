import { createRouter, createWebHistory } from 'vue-router'
// ビューコンポーネントのインポート
import BookListView from '../views/BookListView.vue'
import BookDetailView from '../views/BookDetailView.vue'
import NewBookView from '../views/NewBookView.vue'
import BookEditView from '../views/BookEditView.vue'

// 【ルーティング設定】
// 各パスと表示するコンポーネントを紐付けています。
// 受講者はこの設定を変更する必要は基本的にありませんが、
// 新しいページを追加する場合はここに追記します。
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      // ルートパス ('/') へのアクセス時は、書籍一覧 ('/books') へリダイレクト
      path: '/',
      redirect: '/books'
    },
    {
      // 書籍一覧画面
      path: '/books',
      name: 'books',
      component: BookListView
    },
    {
      // 新規登録画面
      path: '/books/new',
      name: 'book-new',
      component: NewBookView
    },
    {
      // 編集画面 (:id は動的なパラメータです)
      path: '/books/edit/:id',
      name: 'book-edit',
      component: BookEditView
    },
    {
      // 詳細画面 (:id は動的なパラメータです)
      path: '/books/:id',
      name: 'book-detail',
      component: BookDetailView
    }
  ]
})

export default router