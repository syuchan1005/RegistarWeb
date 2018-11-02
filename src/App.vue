<template>
  <v-app>
    <v-toolbar>
      <v-btn icon v-if="$router.currentRoute.path === '/'">
        <v-icon>refresh</v-icon>
      </v-btn>
      <v-btn icon v-else @click="$router.go(-1)">
        <v-icon>keyboard_arrow_left</v-icon>
      </v-btn>
      <v-toolbar-title>{{$store.state.barTitle}}({{$store.state.className}})</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn icon v-if="$router.currentRoute.path === '/'" to="/setting">
        <v-icon>settings</v-icon>
      </v-btn>
    </v-toolbar>
    <v-content>
      <router-view />
    </v-content>
  </v-app>
</template>

<script>

export default {
  name: 'App',
};
</script>
