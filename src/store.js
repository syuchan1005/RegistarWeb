import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    barTitle: '売上計算',
    className: '4CS',
    product: undefined,
    amount: 0,
    lastProductId: -1,
  },
  mutations: {
    /* eslint-disable no-param-reassign */
    changeBarTitle(state, title) {
      state.barTitle = title;
    },
    setProduct(state, product) {
      state.product = product;
    },
    setAmount(state, amount) {
      state.amount = amount;
    },
    setClassName(state, name) {
      state.className = name;
    },
    setLastProductId(state, id) {
      state.lastProductId = id;
    },
  },
  actions: {

  },
});
