
<template>
  <div class="hello">
    <div>
    <vl-map :load-tiles-while-animating="true" :load-tiles-while-interacting="true"
             data-projection="EPSG:4326" style="height: 400px">
      <vl-view :zoom.sync="zoom" :center.sync="center" :rotation.sync="rotation"></vl-view>

      <vl-geoloc @update:position="geolocPosition = $event">
        <template slot-scope="geoloc">
          <vl-feature v-if="geoloc.position" id="position-feature">
            <vl-geom-point :coordinates="geoloc.position"></vl-geom-point>
            <vl-style-box>
              <vl-style-icon src="_media/marker.png" :scale="0.4" :anchor="[0.5, 1]"></vl-style-icon>
            </vl-style-box>
          </vl-feature>
        </template>
      </vl-geoloc>
 
      <vl-layer-tile id="osm">
        <vl-source-osm></vl-source-osm>
      </vl-layer-tile>
      <vl-feature>
       <vl-geom-point
            :coordinates="this.punkt"
            :color="red"
          ></vl-geom-point>
           <vl-style-box>
            <vl-style-circle :radius="15">
              <vl-style-fill color="white"></vl-style-fill>
              <vl-style-stroke color="red"></vl-style-stroke>
            </vl-style-circle>
          </vl-style-box>
    </vl-feature>
    
    </vl-map>
          <v-card
        color="green"
        max-height="200"
        class="beschleunigung"
      >
      <v-card-title><p>Status Beschleunigungssensor</p>
      </v-card-title>
      <v-card-subtitle>
       <h1>Ok</h1>
      </v-card-subtitle>
    
      
      
  </v-card>
    <div style="padding: 20px">
      Zoom: {{ zoom }}<br>
      Betrachtete Position: {{ center }}<br>
    </div>
  </div>
  <div class="options">
  <v-card shaped=true>
  <h2 class="options_title">Optionen</h2>
  <p id="text_optionen">Drehwinkel</p>
    <v-slider v-model="winkel"
          thumb-label="always"
          max="360"
          color="red"
          ></v-slider>
          <p  id="text_optionen">Zoomfaktor</p>
          <v-slider v-model="zoom"
          thumb-label="always"
          max="22"
          min="1"
          step="0.1"
          ></v-slider>
           <v-btn small color="primary" v-on:click="messung">Messung</v-btn>
          
          </v-card>
        

          </div>

  </div>

</template>

<script>

export default {
  name: 'Graph',
  props: {
    msg: String
  }, 
   data: function(){
     return { 
        zoom: 17.3,
        center: [ -0.46868189640700264, 51.35113755158258],
        rotation: 6.3/360*80,
        geolocPosition: undefined,
        winkel: 80,
        copy: 1,
        punkt: [-0.468680700264, 51.35113755158258]
      }
  },

  watch: {
    winkel: function(){this.rotation = this.winkel*6.3/360},
  },
  methods: {
      //Achtung CORS wurde mittels Firefox addon ausgehebelt. Normalerweise Fehlermeldung
        messung: function(){
          // Trick 17
          var t = this;
          console.log("test");
          const axios = require('axios').default;
          setInterval(function(){ 
            console.log("this.zoom");
          axios({
          method: 'get',
            url: 'http://127.0.0.1:5000/loc',
 headers: {
        'Access-Control-Allow-Origin': '*'
    }, 
          })
          .then(function (response) {
            t.punkt = [Number(response.data[0].longitude), Number(response.data[0].latitude)]
            console.log(t.punkt)
          });
             console.log("Ausgelöst")},3000)
          
        },
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
            t.center = [Number(response.data[0].longitude), Number(response.data[0].latitude)]
            console.log(t.position)
          });
             console.log("Ausgelöst")     
        }
      }


}

</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
 .map {
        height: 400px;
        width: 100%;
      }
.options {
    width: 20%;
    margin-left:50px;
}
.options_title{
   margin-bottom: 30px;
}
.beschleunigung{
  position: absolute; 
  width:400px;
  right: 0px;
  top: 0px;
}
#text_optionen{
  margin-bottom:40px;
}
</style>

