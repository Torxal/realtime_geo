
<template>
  <div class="hello">
    <h1>{{ msg2 }}</h1>
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
    </vl-map>
    <div style="padding: 20px">
      Zoom: {{ zoom }}<br>
      Betrachtete Position: {{ center }}<br>
      Drehung: {{ rotation }}<br>
    </div>
  </div>
  <div class="options">
  <h2 class="options_title">Optionen</h2>
    <v-slider v-model="winkel"
          thumb-label="always"
          max="360"
          
          ></v-slider>
          </div>
  </div>

</template>

<script>

export default {
  name: 'Graph',
  props: {
    msg: String
  },
  watch: {
    msg2: function(){this.msg ="tzest"},
    winkel: function(){this.rotation = this.winkel*6.3/360}
  },
    data: function(){
     return { 
        zoom: 17.3,
        center: [ -0.46868189640700264, 51.35113755158258],
        rotation: 1.4,
        geolocPosition: undefined,
        winkel: 2,
        copy: 1
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
</style>
