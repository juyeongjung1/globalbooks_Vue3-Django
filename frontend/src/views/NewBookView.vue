<script setup lang="ts">
import { ref } from 'vue'
import { useRouter, RouterLink } from 'vue-router'
import axios from 'axios'

const router = useRouter()

// 入力データ
const title = ref('')
const author = ref('')
const price = ref<number | null>(null)
const publisher = ref('')
const image_path = ref('')

const submitBook = async () => {
  if(!title.value || !author.value || !price.value) {
    alert('必須項目（タイトル、著者、価格）を入力してください')
    return
  }

  try {
    await axios.post('http://localhost:8001/api/books/', {
      title: title.value,
      author: author.value,
      price: price.value,
      publisher: publisher.value,
      image_path: image_path.value
    })
    alert('登録しました')
    router.push('/books')
  } catch (err) {
    alert('登録に失敗しました')
  }
}
</script>

<template>
  <div class="container mt-4">
    <h2>書籍登録</h2>
    <div class="card p-4">
      <form @submit.prevent="submitBook">
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
          <button class="btn btn-success">登録</button>
          <RouterLink to="/books" class="btn btn-secondary">キャンセル</RouterLink>
        </div>
      </form>
    </div>
  </div>
</template>