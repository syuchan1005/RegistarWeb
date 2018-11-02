<template>
  <div class="home">
    <div class="information">
      <div>売上金額: {{total.money}}円</div>
      <div>売上個数: {{total.amount}}個</div>
    </div>

    <v-btn block large color="primary" to="/selectprice">販売</v-btn>
    <v-btn block large color="error"
           v-if="this.$store.state.lastProductId !== -1" @click="deleteLast">
      最後の注文を取り消し
    </v-btn>
  </div>
</template>

<script>
export default {
  name: 'home',
  data() {
    return {
      total: {
        money: 0,
        amount: 0,
      },
    };
  },
  mounted() {
    this.$store.commit('changeBarTitle', '売上計算');
    this.loadTotal();
  },
  methods: {
    deleteLast() {
      if (this.$store.state.lastProductId === -1) return;
      this.$http({
        method: 'post',
        url: '/api/order/delete',
        data: {
          className: this.$store.state.className,
          id: this.$store.state.lastProductId,
        },
      }).then(() => {
        this.$store.commit('setLastProductId', -1);
        this.loadTotal();
      });
    },
    loadTotal() {
      this.$http({
        url: '/api/order/total',
        params: {
          className: this.$store.state.className,
        },
      }).then((res) => {
        if (res.data === 'None') return;
        this.total = res.data;
      });
    },
  },
};
</script>

<style scoped lang="scss">
.home {
  padding: 10px;
}

.information {
  margin: 10px;
  & > div {
    font-size: 1.5rem;
  }
}
</style>
