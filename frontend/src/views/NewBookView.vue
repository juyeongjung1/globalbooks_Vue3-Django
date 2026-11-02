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
const error = ref<string | null>(null)

const submitBook = async () => {
  error.value = null
  // 参考用の登録画面と同じように、送信前に入力を確認する。
  if (!title.value.trim() || !author.value.trim() || !price.value || price.value <= 0 || !Number.isInteger(price.value)) {
    error.value = '書籍名、著者名、1以上の整数の価格を入力してください。'
    return
  }

  try {
    const newBook = {
      title: title.value,
      author: author.value,
      price: price.value,
      publisher: publisher.value,
      image_path: image_path.value
    }
    await axios.post('http://localhost:8001/api/books/', newBook)
    alert('登録しました')
    router.push('/books')
  } catch (err) {
    console.error(err)
    error.value = '登録に失敗しました。'
  }
}
</script>

<template>
  <div class="container mt-4">
    <h2>書籍登録</h2>
    <div v-if="error" class="alert alert-danger" role="alert">{{ error }}</div>
    <div class="card p-4">
      <form @submit.prevent="submitBook">
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
          <button class="btn btn-success"><i class="bi bi-check-lg me-1"></i>登録</button>
          <RouterLink to="/books" class="btn btn-secondary"><i class="bi bi-x-lg me-1"></i>キャンセル</RouterLink>
        </div>
      </form>
    </div>
  </div>
</template>
