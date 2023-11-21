import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

impoer Cookies from ''
import axios from 'axios' 
const app = createApp(App)

app.use(createPinia())
app.use(router)
app.config.globalProperties.$axios = axios;

app.mount('#app')
