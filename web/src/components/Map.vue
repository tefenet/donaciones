<template>
  <div style="height: 350px;width:700px">
    <!-- <div class="info" style="height: 15%">
      <span>Center: {{ center }}</span>
      <span>Zoom: {{ zoom }}</span>
      <span>Bounds: {{ bounds }}</span>
    </div> -->
    <l-map
      style="height: 80%; width: 100%"
      :zoom="zoom"
      :center="center"
      @update:zoom="zoomUpdated"
      @update:center="centerUpdated"
      @update:bounds="boundsUpdated"
      @click="addPoint"
    >
      <l-tile-layer :url="url"></l-tile-layer>
      <l-marker v-for="(point,index) in points" :lat-lng="point" v-bind:key="index" @click="removePoint(point)" ></l-marker>
    </l-map>
  </div>
</template>

<script>
import {LMap, LTileLayer, LMarker} from 'vue2-leaflet';

export default {
  components: {
    LMap,
    LTileLayer,
    LMarker,
  },
  data () {
    return {
      url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
      zoom: 12,
      center: [-34.9187, -57.956],
      bounds: null,      
      points:[[-34.9187, -57.958],[-34.9187, -57.960],[-34.9187, -57.950],[-34.9180, -57.956]]
    };
  },
  methods: {
    zoomUpdated (zoom) {
      this.zoom = zoom;
    },
    centerUpdated (center) {
      this.center = center;
    },
    boundsUpdated (bounds) {
      this.bounds = bounds;
    },
    addPoint(point){
       this.points.push(point.latlng)
    },
    removePoint(point){
        const index= this.points.indexOf(point)
        this.points.splice(index,1)
    } 
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
