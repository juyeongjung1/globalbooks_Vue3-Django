<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRoute, useRouter, RouterLink } from 'vue-router'
import axios from 'axios'

const route = useRoute()
const router = useRouter()
const id = Number(route.params.id)

// 入力データ
const title = ref('')
const author = ref('')
const price = ref<number | null>(null)
const publisher = ref('')
const image_path = ref('')
const loading = ref(true)
const loaded = ref(false)
const error = ref<string | null>(null)

// 既存データの取得
const fetchBook = async () => {
  try {
    const res = await axios.get(`http://localhost:8001/api/books/${id}/`)
    title.value = res.data.title
    author.value = res.data.author
    price.value = res.data.price
    publisher.value = res.data.publisher || ''
    image_path.value = res.data.image_path || ''
    loaded.value = true
  } catch (err) {
    console.error(err)
    error.value = '書籍データの取得に失敗しました。'
  } finally {
    loading.value = false
  }
}

// 更新処理
const updateBook = async () => {
  error.value = null
  if (!title.value.trim() || !author.value.trim() || !price.value || price.value <= 0 || !Number.isInteger(price.value)) {
    error.value = '書籍名、著者名、1以上の整数の価格を入力してください。'
    return
  }

  try {
    const updatedBook = {
      title: title.value,
      author: author.value,
      price: price.value,
      publisher: publisher.value,
      image_path: image_path.value
    }
    await axios.put(`http://localhost:8001/api/books/${id}/`, updatedBook)
    alert('更新しました')
    router.push(`/books/${id}`)
  } catch (err) {
    console.error(err)
    error.value = '更新に失敗しました。'
  }
}

onMounted(() => {
  fetchBook()
})
</script>

<template>
  <div class="container mt-4">
    <h2>書籍情報編集</h2>
    <div v-if="loading">読み込み中...</div>
    <div v-if="error" class="alert alert-danger" role="alert">{{ error }}</div>
    <RouterLink v-if="!loading && !loaded" to="/books" class="btn btn-secondary">一覧へ戻る</RouterLink>
    <div v-if="loaded" class="card p-4">
      <form @submit.prevent="updateBook">
        <div class="mb-3">
          <label class="form-label">ID</label>
          <input type="text" class="form-control" :value="id" disabled>
        </div>
        <div class="mb-3">
          <label class="form-label">書籍名 <span class="text-danger">*</span></label>
          <input type="text" class="form-control" v-model="title" maxlength="255" required>
        </div>
        <div class="mb-3">
          <label class="form-label">著者名 <span class="text-danger">*</span></label>
          <input type="text" class="form-control" v-model="author" maxlength="255" required>
        </div>
        <div class="mb-3">
          <label class="form-label">価格 <span class="text-danger">*</span></label>
          <input type="number" class="form-control" v-model="price" min="1" step="1" required>
        </div>
        <div class="mb-3">
          <label class="form-label">出版社</label>
          <input type="text" class="form-control" v-model="publisher" maxlength="255">
        </div>
        <div class="mb-3">
          <label class="form-label">画像パス (例: /images/1.png)</label>
          <input type="text" class="form-control" v-model="image_path" maxlength="255">
          <div class="form-text">※public/images内の画像は /images/1.png のように入力します。画像URLも指定できます。空欄の場合は「画像なし」と表示します。</div>
        </div>
        
        <div class="d-flex gap-2">
          <button class="btn btn-primary"><i class="bi bi-save me-1"></i>保存</button>
          <RouterLink :to="`/books/${id}`" class="btn btn-secondary"><i class="bi bi-x-lg me-1"></i>キャンセル</RouterLink>
        </div>
      </form>
    </div>
  </div>
</template>
