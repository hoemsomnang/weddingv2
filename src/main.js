import { createApp } from 'vue'
import { createRouter, createWebHashHistory } from 'vue-router'
import App from './App.vue'
import './styles/main.css'

// ── Routes ──────────────────────────────────────────────────
import CoverPage from './views/CoverPage.vue'
import HomePreviewPage from './views/HomePreviewPage.vue'

const routes = [
  { path: '/', name: 'cover', component: CoverPage },
  { path: '/home-preview', name: 'homePreviewPage', component: HomePreviewPage, alias: '/homePreviewPage' },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes,
  scrollBehavior: () => ({ top: 0, behavior: 'smooth' }),
})

createApp(App).use(router).mount('#app')
