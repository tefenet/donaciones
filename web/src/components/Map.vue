<template>
  <div style="height: 450px">
    <!-- <div class="info" style="height: 15%">
      <span>Center: {{ center }}</span>
      <span>Zoom: {{ zoom }}</span>
      <span>Bounds: {{ bounds }}</span>
    </div> -->
    <b-container>
      <p><span class="titulo">Mapa </span><span class="titulo tituloba">Centros
        <br/>de Ayuda</span>
      </p>
      <!--      <img :src="require('@/assets/logo_gba.png')" class="img-fluid h-25 w-25"/>-->
      <p>
        <span>
          Mapa con las ubicaciones geográficas de los Centros de Ayuda de la provincia de Buenos Aires. En cada punto
          vas a encontrar información de cada centro(horario de apertura y cierre, dirección y teléfono).
        </span>
      </p>
    </b-container>
    <hr class="mb-4">
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
        <b-modal :header-bg-variant="headerBgVariant"
                 :header-text-variant="headerTextVariant"
                 :id="'modal-'+index" :title="'Centro:  '+center.nombre"
                 ok-only
                 ok-title="Cerrar"
                 ok-variant="info">
          <p class="titulo-text">
            <span><font-awesome-icon :icon="['fa', 'map-marker-alt']"
                                     style="color: darkcyan;"/> direccion: {{ center.direccion }}</span><br>
            <span><font-awesome-icon :icon="['fa', 'phone']" style="color: darkcyan;"/> telefono: {{ center.telefono }}</span><br>
            <span><font-awesome-icon :icon="['fa', 'door-open']"
                                     style="color: darkcyan;"/> abre: {{ center.hora_apertura }}hs</span><br>
            <span><font-awesome-icon :icon="['fa', 'door-closed']"
                                     style="color: darkcyan;"/> cierra: {{ center.hora_cierre }}hs</span>
          </p>
        </b-modal>
      </l-marker>
    </l-map>
  </div>
</template>

<script>
import {LMap, LTooltip, LTileLayer, LMarker} from "vue2-leaflet";
import axios from "axios";
import {API_LOCATION} from '@/config';

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
      zoom: 5,
      center: [-36.9187, -64.956],
      bounds: null,
      centers: Array,
      points: Array,
      headerBgVariant: 'info',
      headerTextVariant: 'white titulo',
    };
  },
  methods: {
    locationMarkerOnClick(index) {
      window.event.stopPropagation();
      this.$bvModal.show("modal-" + index);
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
        .get(API_LOCATION + 'centrosAll')
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
