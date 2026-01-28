<template>
  <div class="list-group">
    <div class="list-group-item disabled fw-bold">メニュー</div>
    <RouterLink 
      to="/books" 
      class="list-group-item list-group-item-action" 
      active-class="active"
    >
      書籍一覧
    </RouterLink>
    <RouterLink 
      to="/books/new" 
      class="list-group-item list-group-item-action" 
      active-class="active"
    >
      書籍登録
    </RouterLink>
  </div>
</template>

<script setup lang="ts">
import { RouterLink } from 'vue-router'
</script>
