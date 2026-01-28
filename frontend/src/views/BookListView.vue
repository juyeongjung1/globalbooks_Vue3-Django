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
  publisher: string
  image_path: string
}

const books = ref<Book[]>([])
const loading = ref(true)
const error = ref<string | null>(null)
const keyword = ref('')

// 画像のパスを解決する関数
const getImagePath = (path: string) => {
  if (!path) return '/images/no_image.png' // デフォルト画像（あれば）
  if (path.startsWith('http')) return path
  return path // publicフォルダ以下のパスを想定
}

// 検索・一覧取得関数
const fetchBooks = async () => {
  loading.value = true
  error.value = null
  try {
    const res = await axios.get('http://localhost:8001/api/books/', { // Port 8001 for Django
      params: { keyword: keyword.value }
    })
    books.value = res.data
  } catch (err) {
    error.value = '書籍情報の取得に失敗しました。'
  } finally {
    loading.value = false
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

    <!-- ローディング・エラー表示 -->
    <div v-if="loading">読み込み中...</div>
    <div v-else-if="error" class="text-danger"><i class="bi bi-exclamation-triangle me-1"></i>{{ error }}</div>

    <!-- 書籍一覧テーブル -->
    <table v-else class="table table-striped align-middle">
      <thead>
        <tr>
          <th>画像</th>
          <th>ID</th>
          <th>書籍名</th>
          <th>著者名</th>
          <th>価格</th>
          <th>アクション</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="book in books" :key="book.id">
          <td>
            <img :src="getImagePath(book.image_path)" alt="表紙" style="width: 50px; height: auto;">
          </td>
          <td>{{ book.id }}</td>
          <td>{{ book.title }}</td>
          <td>{{ book.author }}</td>
          <td>{{ book.price.toLocaleString() }} 円</td>
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