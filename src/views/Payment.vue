<template>
  <div class="payment">
    <div class="information">
      <div>合計: {{total}}円</div>
      <div>{{change >= 0 ? '不足' : 'お釣り'}}: {{Math.abs(change)}}円</div>
    </div>
    <v-text-field type="number" class="field" v-model="receipt" label="預かり金額" />
    <v-text-field type="number" class="field" v-model="ticket" label="食券" placeholder="食券: 0枚" />

    <v-btn block class="primary" @click="addOrder">支払い</v-btn>
  </div>
</template>

<script>
export default {
  name: 'Payment',
  data() {
    return {
      receipt: 0,
      ticket: 0,
    };
  },
  computed: {
    total() {
      return this.$store.state.product.price * this.$store.state.amount;
    },
    change() {
      const price = this.total - this.ticket * 100;
      if (price < 0) return this.receipt;
      return price - this.receipt;
    },
  },
  mounted() {
    this.$store.commit('changeBarTitle', '支払い');
  },
  methods: {
    addOrder() {
      this.$http({
        method: 'post',
        url: '/api/order/add',
        data: {
          className: this.$store.state.className,
          productID: this.$store.state.product.id,
          amount: this.$store.state.amount,
        },
      }).then((res) => {
        this.$store.commit('setLastProductId', res.data.id);
        this.$router.push('/');
      });
    },
  },
};
</script>

<style scoped lang="scss">
  .payment {
    padding: 10px;
  }

  .information {
    margin: 10px;
    & > div {
      font-size: 1.5rem;
    }
  }

  .field {
    padding: 20px;
  }
</style>
