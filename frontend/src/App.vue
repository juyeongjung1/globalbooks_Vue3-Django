<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <div class="container-fluid bg-light min-vh-100 d-flex flex-column">
    <!-- ヘッダーエリア -->
    <header class="bg-dark text-white p-3 mb-4">
      <div class="container">
        <h1 class="h3 mb-0">人事管理システム</h1>
      </div>
    </header>

    <!-- メインレイアウト（サイドメニュー + コンテンツ） -->
    <div class="container flex-grow-1">
      <div class="row">
        <!-- サイドメニューエリア -->
        <div class="col-md-3 mb-4">
          <div class="list-group">
            <div class="list-group-item disabled fw-bold">メニュー</div>
            <!-- ルーターリンクでページ切り替え -->
            <RouterLink 
              to="/employees" 
              class="list-group-item list-group-item-action" 
              active-class="active"
            >
              社員一覧
            </RouterLink>
            <RouterLink 
              to="/employees/new" 
              class="list-group-item list-group-item-action" 
              active-class="active"
            >
              新規社員登録
            </RouterLink>
          </div>
        </div>

        <!-- メインコンテンツエリア -->
        <div class="col-md-9">
          <!-- ここにURLに応じた画面（EmployeeListViewなど）が表示される -->
          <RouterView />
        </div>
      </div>
    </div>

    <!-- フッターエリア -->
    <footer class="bg-secondary text-white text-center p-3 mt-auto">
      &copy; 2025 人事管理システム
    </footer>
  </div>
</template>

<style scoped>
/* 必要に応じてスタイルを追加 */
</style>