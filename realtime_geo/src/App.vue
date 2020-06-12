<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png" class="logo">.
    <h1>Positionsabfrage - Server</h1>
    <Graph msg="hallo"/>
  </div>
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
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.logo {
  margin: 0;
  position:absolute; 
  width: 7% ;
  left:0px;
  top:0px;
}
</style>
