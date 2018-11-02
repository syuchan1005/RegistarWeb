import Vue from 'vue';
import './plugins/vuetify';
import App from './App.vue';
import router from './router';
import store from './store';
import './registerServiceWorker';
import axios from './util/AxiosMock';

Vue.config.productionTip = false;
Vue.prototype.$http = axios.create({ method: 'get' });

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app');
