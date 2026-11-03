<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRoute, useRouter, RouterLink } from 'vue-router'
import axios from 'axios'

const route = useRoute()
const router = useRouter()
const id = Number(route.params.id)

type Book = {
  id: number
  title: string
  author: string
  price: number
  publisher: string | null
  image_path: string | null
  like_count: number
}

const book = ref<Book | null>(null)
const loading = ref(true)
const error = ref<string | null>(null)
const likeError = ref<string | null>(null)
const liking = ref(false)

// 詳細取得
const fetchDetail = async () => {
  try {
    const res = await axios.get<Book>(`http://localhost:8000/api/books/${id}/`)
    book.value = res.data
  } catch (err) {
    console.error(err)
    error.value = '書籍データの取得に失敗しました。'
  } finally {
    loading.value = false
  }
}

// オプション2: 戻ってきた書籍データで、保存済みの回数を表示する。
const likeBook = async () => {
  likeError.value = null
  liking.value = true
  try {
    const res = await axios.post<Book>(`http://localhost:8000/api/books/${id}/like/`)
    book.value = res.data
  } catch (err) {
    console.error(err)
    likeError.value = 'いいねに失敗しました。'
  } finally {
    liking.value = false
  }
}

// 削除処理
const deleteBook = async () => {
  const isConfirmed = confirm('本当にこの書籍データを削除してもよろしいですか？')
  if (!isConfirmed) {
    return
  }

  error.value = null
  try {
    await axios.delete(`http://localhost:8000/api/books/${id}/`)
    alert('削除しました')
    router.push('/books')
  } catch (err) {
    console.error(err)
    error.value = '削除に失敗しました。'
  }
}

onMounted(() => {
  fetchDetail()
})
</script>

<template>
  <div class="container mt-4">
    <h2>書籍詳細</h2>
    <div v-if="loading">読み込み中...</div>
    <div v-else-if="error" class="alert alert-danger" role="alert">{{ error }}</div>
    <div v-else-if="book" class="card p-4">
      <div class="row">
        <!-- 左カラム: 画像 -->
        <div class="col-md-4 text-center">
          <img v-if="book.image_path" :src="book.image_path" alt="書籍表紙" class="img-fluid rounded shadow-sm" style="max-height: 400px;">
          <span v-else class="text-muted">画像なし</span>
        </div>

        <!-- 右カラム: 書籍情報 -->
        <div class="col-md-8">
          <h3 class="mb-3">{{ book.title }}</h3>
          <table class="table table-borderless">
            <tbody>
              <tr>
                <th style="width: 150px;">ID</th>
                <td>{{ book.id }}</td>
              </tr>
              <tr>
                <th>著者</th>
                <td>{{ book.author }}</td>
              </tr>
              <tr>
                <th>価格</th>
                <td class="fs-4">{{ book.price.toLocaleString() }} 円</td>
              </tr>
              <tr>
                <th>出版社</th>
                <td>{{ book.publisher }}</td>
              </tr>
              <tr>
                <th>画像パス</th>
                <td class="text-muted small">{{ book.image_path }}</td>
              </tr>
            </tbody>
          </table>

          <div v-if="likeError" class="alert alert-danger" role="alert">{{ likeError }}</div>
          <button type="button" class="btn btn-outline-danger" :disabled="liking" @click="likeBook">
            ♥ いいね {{ book.like_count }}
          </button>
          <div class="mt-4 d-flex gap-2">
            <RouterLink to="/books" class="btn btn-secondary"><i class="bi bi-arrow-left me-1"></i>一覧へ戻る</RouterLink>
            <RouterLink :to="`/books/edit/${book.id}`" class="btn btn-primary"><i class="bi bi-pencil-square me-1"></i>編集</RouterLink>
            <button class="btn btn-danger" @click="deleteBook"><i class="bi bi-trash me-1"></i>削除</button>
          </div>
        </div>
      </div>
    </div>
    <RouterLink v-if="!loading && error" to="/books" class="btn btn-secondary">一覧へ戻る</RouterLink>
  </div>
</template>
