import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import './assets/index.css'
import './assets/fontawesome/all.css'
import { store, key } from './store'

const app = createApp(App)

app.use(store, key)
app.use(router)

app.mount('#app')
