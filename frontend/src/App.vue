<script setup lang="ts">
import { RouterView } from 'vue-router'
import HeaderMenu from './components/HeaderMenu.vue'
import SideMenu from './components/SideMenu.vue'
import FooterInfo from './components/FooterInfo.vue'
</script>

<template>
  <!-- 
    【レイアウト構成】
    ここはアプリケーション全体の基本レイアウトを定義しています。
    - HeaderMenu: 画面上部の共通ヘッダー
    - SideMenu: 左側の共通メニュー
    - RouterView: URLに応じて切り替わるメインコンテンツ部分 (各Viewコンポーネントが表示されます)
    - FooterInfo: 画面下部の共通フッター
    
    必要に応じてスタイルや構造を調整してください。
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
          <!-- RouterView: ここに BookListView などが表示されます -->
          <RouterView />
        </div>
      </div>
    </div>

    <!-- フッターエリア -->
    <FooterInfo />
  </div>
</template>

<style scoped>
/* 必要に応じて全体のスタイルを追加 */
</style>