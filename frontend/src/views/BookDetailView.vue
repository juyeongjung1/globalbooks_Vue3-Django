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
  publisher: string
  image_path: string
}

const book = ref<Book | null>(null)

// 画像パス解決
const getImagePath = (path: string) => {
  if (!path) return '/images/no_image.png'
  if (path.startsWith('http')) return path
  return path
}

// 詳細取得
const fetchDetail = async () => {
  try {
    const res = await axios.get(`http://localhost:8001/api/books/${id}/`)
    book.value = res.data
  } catch (err) {
    alert('データ取得に失敗しました')
  }
}

// 削除処理
const deleteBook = async () => {
  if(!confirm('本当にこの書籍データを削除してもよろしいですか？')) return

  try {
    await axios.delete(`http://localhost:8001/api/books/${id}/`)
    alert('削除しました')
    router.push('/books')
  } catch (err) {
    alert('削除に失敗しました')
  }
}

onMounted(() => {
  fetchDetail()
})
</script>

<template>
  <div class="container mt-4" v-if="book">
    <h2>書籍詳細</h2>
    <div class="card p-4">
      <div class="row">
        <!-- 左カラム: 画像 -->
        <div class="col-md-4 text-center">
          <img :src="getImagePath(book.image_path)" alt="書籍表紙" class="img-fluid rounded shadow-sm" style="max-height: 400px;">
        </div>

        <!-- 右カラム: 書籍情報 -->
        <div class="col-md-8">
          <h3 class="mb-3">{{ book.title }}</h3>
          <table class="table table-borderless">
            <tbody>
              <tr>
                <th style="width: 150px;">著者</th>
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

          <div class="mt-4 d-flex gap-2">
            <RouterLink to="/books" class="btn btn-secondary">一覧へ戻る</RouterLink>
            <RouterLink :to="`/books/edit/${book.id}`" class="btn btn-primary">編集</RouterLink>
            <button class="btn btn-danger" @click="deleteBook">削除</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>