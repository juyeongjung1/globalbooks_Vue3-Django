<template>
  <div class="list-group">
    <div class="list-group-item disabled fw-bold">メニュー</div>
    <RouterLink 
      to="/books" 
      class="list-group-item list-group-item-action" 
      active-class="active"
    >
      <i class="bi bi-journal-text me-2"></i>書籍一覧
    </RouterLink>
    <RouterLink 
      to="/books/new" 
      class="list-group-item list-group-item-action" 
      active-class="active"
    >
      <i class="bi bi-journal-plus me-2"></i>書籍登録
    </RouterLink>
  </div>
</template>

<script setup lang="ts">
import { RouterLink } from 'vue-router'
</script>
