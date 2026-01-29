import { createRouter, createWebHistory } from 'vue-router'
import BookListView from '../views/BookListView.vue'
import BookDetailView from '../views/BookDetailView.vue'
import NewBookView from '../views/NewBookView.vue'
import BookEditView from '../views/BookEditView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      redirect: '/books'
    },
    {
      path: '/books',
      name: 'books',
      component: BookListView
    },
    {
      path: '/books/new',
      name: 'book-new',
      component: NewBookView
    },
    {
      path: '/books/edit/:id',
      name: 'book-edit',
      component: BookEditView
    },
    {
      path: '/books/:id',
      name: 'book-detail',
      component: BookDetailView
    }
  ]
})

export default router