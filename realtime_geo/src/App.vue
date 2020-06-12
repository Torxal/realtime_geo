<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark
    >
      <div class="d-flex align-center">
        <v-img
          alt="Hanseatic Efficiency Logo"
          class="shrink mr-2"
          contain
          src="./assets/logo.png"
          transition="scale-transition"
          width="40"
        />
      <h1>Echtzeitortungssystem</h1>
      </div>
      <v-spacer></v-spacer>
    </v-app-bar>

    <v-content>
      <Graph/>
    </v-content>
  </v-app>
</template>

<script>
import Graph from './components/Graph.vue'
import Vue from 'vue'
import VueLayers from 'vuelayers'
import 'vuelayers/lib/style.css' // needs css-loaders
Vue.use(VueLayers)

export default {
  name: 'App',

  components: {
    Graph
  },

  data: () => ({
    //
  }),
};
</script>
