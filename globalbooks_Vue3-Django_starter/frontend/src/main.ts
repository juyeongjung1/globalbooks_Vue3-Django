import { createApp } from 'vue'
import App from './App.vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-icons/font/bootstrap-icons.css'

import router from './router' // 追加：Vue Router のインポート

createApp(App)
    .use(router) // 追加：Vue Router をアプリに登録
    .mount('#app')
