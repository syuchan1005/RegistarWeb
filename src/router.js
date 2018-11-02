import Vue from 'vue';
import Router from 'vue-router';
import Home from './views/Home.vue';
import SelectPrice from './views/SelectPrice.vue';
import SelectCount from './views/SelectCount.vue';
import Payment from './views/Payment.vue';
import Setting from './views/Setting.vue';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
    },
    {
      path: '/selectprice',
      name: 'select-price',
      component: SelectPrice,
    },
    {
      path: '/selectcount',
      name: 'select-count',
      component: SelectCount,
    },
    {
      path: '/payment',
      name: 'payment',
      component: Payment,
    },
    {
      path: '/setting',
      name: 'setting',
      component: Setting,
    },
  ],
});
