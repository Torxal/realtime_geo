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
      <v-btn
  elevation="2"
  icon
> <img alt="self-Logo" src="./img/option_icon.svg" width="30" v-on:click="ask_for_options"></v-btn>
    </v-app-bar>

    <v-content>
      <Graph/>
    </v-content>
<div id="option_menue">
<h1>Optionen</h1>
  <v-text-field
      label="Longitude"
      :rules="rules"
      hide-details="auto"
      v-model="position[0]"
    ></v-text-field>
  <v-text-field
      label="Latitude"
      :rules="rules"
      hide-details="auto"
      v-model="position[1]"
    ></v-text-field>
<v-btn
      depressed
      color="primary"
      id="primary_button"
      v-on:click="set_options"
    >
      Speichern
    </v-btn>
</div>
  </v-app>

</template>

<script>
import Graph from './components/Graph.vue'
import Vue from 'vue'
import VueLayers from 'vuelayers'
import 'vuelayers/lib/style.css' // needs css-loaders
import axios from 'axios'
import VueAxios from 'vue-axios'
Vue.use(VueLayers)
Vue.use(VueAxios, axios)

export default {
  name: 'App',

   data: function(){
     return { 
        position: [ 0, 0]
      }
   },
  components: {
    Graph
  },
   methods: {
      //Achtung CORS wurde mittels Firefox addon ausgehebelt. Normalerweise Fehlermeldung
        ask_for_options: function(){
          // Trick 17
          var t = this;
          console.log("test");
          const axios = require('axios').default;
            console.log("this.zoom");
          axios({
          method: 'get',
            url: 'http://127.0.0.1:5000/app_options',
 headers: {
        'Access-Control-Allow-Origin': '*'
    }, 
          })
          .then(function (response) {
            t.position = [Number(response.data[0].longitude), Number(response.data[0].latitude)]
            console.log(t.position)
          });
             console.log("Ausgelöst")     
        },
        set_options: function(){
          var bodyFormData = new FormData();
          bodyFormData.append('longitude', this.position[0]);
          bodyFormData.append('latitude', this.position[1]);
          axios({
            method: 'post',
            url: 'http://127.0.0.1:5000/app_options',
            data: bodyFormData,
              headers: {
                      'Access-Control-Allow-Origin': '*'
                  }
          })
        }
      }
};
</script>
<style scoped>
#option_menue{
  width: 22%;
  height: 600px;
  margin-left: 38%;
  position: absolute; 
  background-color: #e7e7e7;
  color: blue;
  margin-top:120px;
}
#primary_button{
  margin-top:20px;
}
</style>

