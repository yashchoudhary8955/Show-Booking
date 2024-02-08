import { createApp } from 'vue';
import App from './App.vue';
import router from './routers';
// import axios from 'axios';

// axios.defaults.baseURL = 'http://127.0.0.1:3000'; // Update with your backend URL


const app = createApp(App);
// app.config.globalProperties.$axios = axios;
app.use(router);
app.mount('#app');
