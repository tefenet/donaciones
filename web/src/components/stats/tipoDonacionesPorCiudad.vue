
<template>
  <div>
    <h1>Estadisticas</h1>
    <p>Tipos de Donaciones por ciudad</p>
    <div v-if="ciudadSinDonaciones">
      <span>No tenemos registros de donaciones en centros de esta ciudad :( </span>
    </div>
    <b-container style="max-width: 450px">
     <b-form-select id="input-ciudad" v-model="ciudad" :options="ciudades" size="sm"> </b-form-select>
    </b-container>
    <b-container>
      <ve-pie :data="chartData"></ve-pie>
    </b-container>
  </div>
</template>

<script>
import VePie from 'v-charts/lib/pie.common'
import axios from "axios";
//import {API_LOCATION} from "@/config";
import {API_REF_LOCATION} from "@/config";

export default {
  name: 'StatsTipoDonacionesPorCiudad',
  components: {VePie},
  data() {
    return {
      ciudad: {},
      ciudades: [],
      ciudadSinDonaciones: false, //posiblemente convenga que sea una propiedad computada
      chartData: {
        columns: ['tipo', 'cantidad'],
        rows: [
          {'tipo': 'alimentos', cantidad: 2},
          {'tipo': 'salud', cantidad: 5},
          {'tipo': 'general', cantidad: 4},
        ]
      }
    }
  },
  methods: {
    optionsCiudades(ciudadesResponse) {
      return Object.values(ciudadesResponse).map(function (c) {
        return {'value': c.id, 'text': c.name};
      });
    },
  },
  mounted() {
    axios
        .get(API_REF_LOCATION + 'municipios?per_page=1000')
        .then(response => {
          this.ciudades = this.optionsCiudades(response.data.data.Town);
        })
        .catch(error => {
          console.log(error);
          this.errored = true;
        });
  }

};
</script>
<style>
</style>