<script setup lang="ts">
import { RouterView } from 'vue-router'
import HeaderMenu from './components/HeaderMenu.vue'
import SideMenu from './components/SideMenu.vue'
import FooterInfo from './components/FooterInfo.vue'
</script>

<template>
  <!-- 
    アプリケーション全体のレイアウト
    ・ヘッダー、サイドメニュー、フッターの配置
    ・RouterViewによるメインコンテンツの切り替え
   -->
  <div class="container-fluid bg-light min-vh-100 d-flex flex-column p-0">
    <!-- ヘッダーエリア -->
    <HeaderMenu />

    <!-- メインレイアウト（サイドメニュー + コンテンツ） -->
    <div class="container flex-grow-1">
      <div class="row">
        <!-- サイドメニューエリア -->
        <div class="col-md-3 mb-4">
          <SideMenu />
        </div>

        <!-- メインコンテンツエリア -->
        <div class="col-md-9">
          <RouterView />
        </div>
      </div>
    </div>

    <!-- フッターエリア -->
    <FooterInfo />
  </div>
</template>

<style scoped>
/* 全体のスタイル定義 */
</style>