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
const imageFile = ref<File | null>(null)
const imageInput = ref<HTMLInputElement | null>(null)
const saving = ref(false)
const error = ref<string | null>(null)

// オプション3: ファイルの選択はVue、保存はDjangoが担当する。
const selectImage = (event: Event) => {
  const input = event.target as HTMLInputElement
  const file = input.files?.[0] || null
  imageFile.value = null
  error.value = null
  if (file && (!['image/jpeg', 'image/png'].includes(file.type) || file.size > 5 * 1024 * 1024)) {
    error.value = 'JPEGまたはPNG画像を5MB以下で選択してください。'
    input.value = ''
    return
  }
  imageFile.value = file
}

const submitBook = async () => {
  error.value = null
  // 参考用の登録画面と同じように、送信前に入力を確認する。
  if (!title.value.trim() || !author.value.trim() || !price.value || price.value <= 0 || !Number.isInteger(price.value)) {
    error.value = '書籍名、著者名、1以上の整数の価格を入力してください。'
    return
  }

  saving.value = true
  try {
    if (imageFile.value) {
      const formData = new FormData()
      formData.append('image', imageFile.value)
      const res = await axios.post('http://localhost:8000/api/books/upload-image/', formData)
      image_path.value = res.data.image_path
      imageFile.value = null
      if (imageInput.value) imageInput.value.value = ''
    }
    const newBook = {
      title: title.value,
      author: author.value,
      price: price.value,
      publisher: publisher.value,
      image_path: image_path.value
    }
    await axios.post('http://localhost:8000/api/books/', newBook)
    alert('登録しました')
    router.push('/books')
  } catch (err) {
    console.error(err)
    error.value = '登録に失敗しました。画像と入力内容を確認してください。'
  } finally {
    saving.value = false
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
          <input type="text" class="form-control" v-model="image_path" maxlength="255" :disabled="saving">
          <div class="form-text">※public/images内の画像は /images/1.png のように入力します。画像URLも指定できます。空欄の場合は「画像なし」と表示します。</div>
        </div>
        
        <div class="mb-3">
          <label class="form-label" for="book-image">画像ファイル（任意）</label>
          <input id="book-image" ref="imageInput" type="file" class="form-control"
            accept="image/jpeg,image/png" :disabled="saving" @change="selectImage">
          <div class="form-text">JPEG・PNG、5MB以下。選択したファイルを画像パスより優先して保存します。</div>
        </div>
        <div class="d-flex gap-2">
          <button class="btn btn-success" :disabled="saving"><i class="bi bi-check-lg me-1"></i>{{ saving ? '保存中...' : '登録' }}</button>
          <RouterLink to="/books" class="btn btn-secondary"><i class="bi bi-x-lg me-1"></i>キャンセル</RouterLink>
        </div>
      </form>
    </div>
  </div>
</template>
