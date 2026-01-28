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

// 既存データの取得
const fetchBook = async () => {
  try {
    const res = await axios.get(`http://localhost:8001/api/books/${id}/`)
    title.value = res.data.title
    author.value = res.data.author
    price.value = res.data.price
    publisher.value = res.data.publisher
    image_path.value = res.data.image_path
  } catch (err) {
    alert('データ取得エラー')
  }
}

// 更新処理
const updateBook = async () => {
  try {
    await axios.put(`http://localhost:8001/api/books/${id}/`, {
      title: title.value,
      author: author.value,
      price: price.value,
      publisher: publisher.value,
      image_path: image_path.value
    })
    alert('更新しました')
    router.push(`/books/${id}`)
  } catch (err) {
    alert('更新エラー')
  }
}

onMounted(() => {
  fetchBook()
})
</script>

<template>
  <div class="container mt-4">
    <h2>書籍情報編集</h2>
    <div class="card p-4">
      <form @submit.prevent="updateBook">
        <div class="mb-3">
          <label class="form-label">書籍名 <span class="text-danger">*</span></label>
          <input type="text" class="form-control" v-model="title" required>
        </div>
        <div class="mb-3">
          <label class="form-label">著者名 <span class="text-danger">*</span></label>
          <input type="text" class="form-control" v-model="author" required>
        </div>
        <div class="mb-3">
          <label class="form-label">価格 <span class="text-danger">*</span></label>
          <input type="number" class="form-control" v-model="price" required>
        </div>
        <div class="mb-3">
          <label class="form-label">出版社</label>
          <input type="text" class="form-control" v-model="publisher">
        </div>
        <div class="mb-3">
          <label class="form-label">画像パス (例: /images/1001.png)</label>
          <input type="text" class="form-control" v-model="image_path">
          <div class="form-text">※public/imagesフォルダ内のファイルパスを指定してください</div>
        </div>
        
        <div class="d-flex gap-2">
          <button class="btn btn-primary">保存</button>
          <RouterLink :to="`/books/${id}`" class="btn btn-secondary">キャンセル</RouterLink>
        </div>
      </form>
    </div>
  </div>
</template>