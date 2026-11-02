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
}

const books = ref<Book[]>([])
const loading = ref(true)
const error = ref<string | null>(null)
const searchMessage = ref<string | null>(null)
const keyword = ref('')

// 検索・一覧取得関数
const fetchBooks = async () => {
  loading.value = true
  error.value = null
  searchMessage.value = null
  try {
    const res = await axios.get<Book[]>('http://localhost:8001/api/books/', {
      params: { keyword: keyword.value }
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
            <RouterLink :to="`/books/${book.id}`" class="btn btn-sm btn-info text-white">
              <i class="bi bi-info-circle me-1"></i>詳細
            </RouterLink>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
