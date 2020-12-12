<template>
  <div style="height: 450px">
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
        v-for="(center, index) in centers"
        :lat-lng="getGeoLocation(center)"
        v-bind:key="index"
        @click="locationMarkerOnClick(index)"
      >
        <l-tooltip>{{ center.nombre }}</l-tooltip>        
        <b-modal :id="'modal-'+index" :title="'Centro:  '+center.nombre" ok-only >           
           <p class="my-4">direccion:  {{ center.direccion }}</p>
           <p class="my-4">telefono:  {{ center.telefono }}</p>
           <p class="my-4">abre: {{ center.hora_apertura }}hs</p>
           <p class="my-4">cierra: {{ center.hora_cierre }}hs</p>           
        </b-modal>        
      </l-marker>
    </l-map>
  </div>
</template>

<script>
import { LMap, LTooltip, LTileLayer, LMarker } from "vue2-leaflet";
import axios from "axios";

export default {
  components: {
    LMap,
    LTileLayer,
    LMarker,
    LTooltip,
  },
  data() {
    return {
      url: "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
      zoom: 9,
      center: [-34.664, -58.681],
      bounds: null,
      centers: Array,
      points: Array,
    };
  },
  methods: {
    locationMarkerOnClick(index) {                        
      window.event.stopPropagation();
      this.$bvModal.show("modal-"+index);
      return false;
    },
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
    getGeoLocation(center) {
      return [parseFloat(center.latitud), parseFloat(center.longitud)];
    },
  },
  mounted() {
    axios
      .create({
        headers: {
          "Access-Control-Allow-Origin": "*",
        },
      })
      .get("http://127.0.0.1:8085/api/v1.0/centros/?max=60")
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
