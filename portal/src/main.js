import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import OpenLayersMap from "vue3-openlayers";
import "vue3-openlayers/styles.css";

import App from './App.vue'
import router from './router'

import Cookies from 'js-cookie'
import axios from 'axios' 
const app = createApp(App)

app.use(createPinia())
app.use(router)
app.config.globalProperties.$axios = axios;
app.use(OpenLayersMap)

app.mount('#app')
