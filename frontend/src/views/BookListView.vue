<script setup lang="ts">
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { RouterLink } from 'vue-router'

// 書籍の型定義
type Book = {
  id: number
  title: string
  author: string
  price: number
  publisher: string | null
  image_path: string | null
  like_count: number
}

const books = ref<Book[]>([])
const loading = ref(true)
const error = ref<string | null>(null)
const searchMessage = ref<string | null>(null)
const keyword = ref('')
const ordering = ref('id')
const actionError = ref<string | null>(null)
const liking = ref(false)
const sortButtons = [
  { value: 'id', label: 'IDが小さい順' },
  { value: '-id', label: 'IDが大きい順' },
  { value: 'price', label: '価格が安い順' },
  { value: '-price', label: '価格が高い順' },
  { value: 'title', label: '書籍名の昇順' },
  { value: '-title', label: '書籍名の降順' },
  { value: '-like_count', label: 'いいねが多い順' }
]

// 検索・一覧取得関数
const fetchBooks = async () => {
  loading.value = true
  error.value = null
  searchMessage.value = null
  try {
    const res = await axios.get<Book[]>('http://localhost:8000/api/books/', {
      params: { keyword: keyword.value, ordering: ordering.value }
    })
    books.value = res.data
    if (books.value.length === 0) {
      searchMessage.value = '該当する書籍がありません。'
    }
  } catch (err) {
    console.error(err)
    error.value = '書籍情報の取得に失敗しました。'
  } finally {
    loading.value = false
  }
}

// オプション1: 選択した順序で、現在の検索結果を取得する。
const changeOrder = (value: string) => {
  ordering.value = value
  fetchBooks()
}

// オプション2: 成功したら一覧を取得し直し、回数と並び順を更新する。
const likeBook = async (id: number) => {
  actionError.value = null
  liking.value = true
  try {
    await axios.post(`http://localhost:8000/api/books/${id}/like/`)
    await fetchBooks()
  } catch (err) {
    console.error(err)
    actionError.value = 'いいねに失敗しました。'
  } finally {
    liking.value = false
  }
}

onMounted(() => {
  fetchBooks()
})
</script>

<template>
  <div class="container mt-4">
    <h2>書籍管理システム - 書籍一覧</h2>
    
    <!-- 検索フォームと新規登録ボタン -->
    <div class="d-flex justify-content-between mb-3">
      <div class="input-group w-50">
        <input type="text" class="form-control" v-model="keyword" placeholder="書籍名で検索">
        <button class="btn btn-primary" @click="fetchBooks"><i class="bi bi-search me-1"></i>検索</button>
      </div>
      <RouterLink to="/books/new" class="btn btn-success"><i class="bi bi-plus-lg me-1"></i>新規登録</RouterLink>
    </div>

    <div class="mb-3">
      <p class="mb-2">並び替え</p>
      <div class="d-flex flex-wrap gap-2">
        <button v-for="sort in sortButtons" :key="sort.value" type="button"
          class="btn btn-sm" :class="ordering === sort.value ? 'btn-primary' : 'btn-outline-primary'"
          :aria-pressed="ordering === sort.value" :disabled="loading || liking" @click="changeOrder(sort.value)">
          {{ sort.label }}
        </button>
      </div>
    </div>
    <div v-if="actionError" class="alert alert-danger" role="alert">{{ actionError }}</div>

    <!-- ローディング・エラー表示 -->
    <div v-if="loading">読み込み中...</div>
    <div v-else-if="error" class="text-danger"><i class="bi bi-exclamation-triangle me-1"></i>{{ error }}</div>
    <div v-else-if="searchMessage" class="text-muted">{{ searchMessage }}</div>

    <!-- 書籍一覧テーブル -->
    <table v-else class="table table-striped align-middle">
      <thead>
        <tr>
          <th>画像</th>
          <th>ID</th>
          <th>書籍名</th>
          <th>著者名</th>
          <th>価格</th>
          <th>いいね</th>
          <th>アクション</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="book in books" :key="book.id">
          <td>
            <img v-if="book.image_path" :src="book.image_path" alt="表紙" style="width: 50px; height: auto;">
            <span v-else class="text-muted small">画像なし</span>
          </td>
          <td>{{ book.id }}</td>
          <td>{{ book.title }}</td>
          <td>{{ book.author }}</td>
          <td>{{ book.price.toLocaleString() }} 円</td>
          <td>
            <button type="button" class="btn btn-sm btn-outline-danger" :disabled="liking"
              :aria-label="'いいね: ' + book.title" @click="likeBook(book.id)">♥ {{ book.like_count }}</button>
          </td>
          <td>
            <RouterLink :to="`/books/${book.id}`" class="btn btn-sm btn-info text-white">
              <i class="bi bi-info-circle me-1"></i>詳細
            </RouterLink>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
