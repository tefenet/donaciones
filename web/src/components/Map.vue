<template>
  <div style="height: 350px; width: 700px">
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
      <l-marker
        v-for="(point, index) in points"
        :lat-lng="point"
        v-bind:key="index"
        @click="removePoint(point)"
      ></l-marker>
    </l-map>
  </div>
</template>

<script>
import { LMap, LTileLayer, LMarker } from "vue2-leaflet";
import axios from "axios";

export default {
  components: {
    LMap,
    LTileLayer,
    LMarker,
  },
  data() {
    return {
      url: "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
      zoom: 5,
      center: [-36.9187, -64.956],
      bounds: null,
      centers: Array,
      points: Array,
    };
  },
  methods: {
    zoomUpdated(zoom) {
      this.zoom = zoom;
    },
    centerUpdated(center) {
      this.center = center;
    },
    boundsUpdated(bounds) {
      this.bounds = bounds;
    },
    addPoint(point) {
      this.points.push(point.latlng);
    },
    removePoint(point) {
      const index = this.points.indexOf(point);
      this.points.splice(index, 1);
    },
  },
  mounted() {
    axios
      .create({
        headers: {
          "Access-Control-Allow-Origin": "*",
        },
      })
      .get("http://127.0.0.1:5000/api/v1.0/centrosAll")
      .then((res) => {
        this.centers = res.data.centros;
        this.points = this.centers.map((c) => [
          parseFloat(c.latitud),
          parseFloat(c.longitud),
        ]);
        console.log(this.centers);
      })
      .catch((error) => {
        console.log(error);
        // Manage errors if found any
      });
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
