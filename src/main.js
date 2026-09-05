import { createApp } from 'vue'
import { createRouter, createWebHashHistory } from 'vue-router'
import App from './App.vue'
import './styles/main.css'

// ── Routes (only Cover for now; others added later) ──────────────────────────
import CoverPage from './views/CoverPage.vue'

const routes = [
  { path: '/', name: 'cover', component: CoverPage },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes,
  scrollBehavior: () => ({ top: 0, behavior: 'smooth' }),
})

createApp(App).use(router).mount('#app')
