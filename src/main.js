import Vue from 'vue';
import './plugins/vuetify';
import App from './App.vue';
import router from './router';
import store from './store';
import './registerServiceWorker';
import axios from './util/AxiosMock';

Vue.config.productionTip = false;
Vue.prototype.$http = axios.create({
  method: 'get',
  baseURL: 'http://192.168.0.5:5000',
});

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app');
