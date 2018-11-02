<template>
  <v-list>
    <v-list-tile v-for="item in list" :key="item.id" @click="() => {
      $store.commit('setProduct', item);
      $router.push('/selectcount');
    }">
      <v-list-tile-title>{{item.name}}</v-list-tile-title>
      <v-list-tile-content>{{item.price}}円</v-list-tile-content>
    </v-list-tile>
  </v-list>
</template>

<script>
export default {
  name: 'SelectPrice',
  data() {
    return {
      list: [],
    };
  },
  mounted() {
    this.$store.commit('changeBarTitle', '価格選択');
    this.$http({
      method: 'get',
      url: '/api/products/list',
      params: {
        className: this.$store.state.className,
      },
    }).then((res) => {
      this.list = res.data.data;
    });
  },
};
</script>

<style scoped lang="scss">

</style>
