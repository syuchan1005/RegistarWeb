<template>
  <div class="setting">
    <v-text-field v-model="className" label="団体名"/>

    <v-card>
      <v-card-title>
        商品
        <v-spacer></v-spacer>
        <v-dialog v-model="showDialog" persistent max-width="600px">
          <v-btn icon slot="activator">
            <v-icon>add</v-icon>
          </v-btn>
          <v-card>
            <v-card-title>商品追加</v-card-title>
            <v-card-text>
              <v-text-field label="商品名" v-model="addProductItem.name" required />
              <v-text-field type="number" label="価格" v-model="addProductItem.price" required />
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue darken-1" flat @click.native="showDialog = false">Close</v-btn>
              <v-btn color="blue darken-1" flat @click.native="() => {
                addProduct();
                showDialog = false;
              }">Add</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-card-title>
      <v-data-table
        :headers="headers"
        :items="products"
        hide-actions
      >
        <template slot="items" slot-scope="props">
          <td>{{ props.item.name }}</td>
          <td>{{ props.item.price }}</td>
          <td>
            <v-icon @click="deleteProduct(props.item)">
              delete
            </v-icon>
          </td>
        </template>
      </v-data-table>
    </v-card>
  </div>
</template>

<script>
import { debounce } from 'lodash';

export default {
  name: 'Setting',
  data() {
    return {
      headers: [
        { text: '商品名', value: 'name' },
        { text: '価格', value: 'price' },
        {
          text: '',
          value: 'delete',
          align: 'right',
          sortable: false,
          width: '30px',
        },
      ],
      products: [],
      showDialog: false,
      addProductItem: {
        name: '',
        price: 0,
      },
      debounceLoadProduct: undefined,
    };
  },
  computed: {
    className: {
      get() {
        return this.$store.state.className;
      },
      set(val) {
        this.$store.commit('setClassName', val);
      },
    },
  },
  watch: {
    className: {
      handler()  {
        if (!this.debounceLoadProduct) {
          this.debounceLoadProduct = debounce(() => {
            this.$http({
              url: '/api/products/list',
              params: {
                className: this.className,
              },
            }).then((res) => {
              this.products = res.data.data;
            });
          }, 600);
        }
        this.debounceLoadProduct();
      },
      immediate: true,
    },
  },
  mounted() {
    this.$store.commit('changeBarTitle', '設定');
  },
  methods: {
    deleteProduct(product) {
      this.$http({
        method: 'post',
        url: '/api/products/delete',
        data: {
          className: this.$store.state.className,
          id: product.id,
        },
      }).then(() => {
        this.products = this.products.filter(v => v.id !== product.id);
      });
    },
    addProduct() {
      this.$http({
        method: 'post',
        url: '/api/products/add',
        data: {
          className: this.$store.state.className,
          ...this.addProductItem,
        },
      }).then((res) => {
        this.products.push({
          id: res.data.id,
          ...this.addProductItem,
        });
      });
    },
  },
};
</script>

<style scoped lang="scss">
  .setting {
    padding: 20px;
  }
</style>
