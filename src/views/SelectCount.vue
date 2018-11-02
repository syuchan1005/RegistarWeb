<template>
  <div class="select-count">
    <div class="information">
      <div>一個: {{$store.state.product.price}}円</div>
      <div>合計: {{$store.state.product.price * amount}}円</div>
    </div>

    <v-text-field class="field" type="number" v-model="amount" label="販売個数" />

    <v-btn block depressed class="primary" @click="() => {
      $store.commit('setAmount', amount);
      $router.push('/payment');
    }">支払い</v-btn>
  </div>
</template>

<script>
export default {
  name: 'SelectCount',
  data() {
    return {
      amount: 0,
    };
  },
  mounted() {
    this.$store.commit('changeBarTitle', '品数入力');
  },
};
</script>

<style scoped lang="scss">
  .select-count {
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
