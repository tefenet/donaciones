
<template>
  <div>
    <h1>Estadisticas</h1>
    <p>Tipos de Donaciones por ciudad</p>
    <b-container style="max-width: 450px">
      <span> Selecciona una ciudad </span>
    <b-form-select id="input-ciudad" v-model="ciudad_id" :options="ciudades" @change="selectCity()" size="sm"> </b-form-select>
    </b-container>
    <div v-if="ciudadSinDonaciones"><br>
      <h5>No tenemos registros de donaciones en centros de esta ciudad :( </h5>
    </div>
    <b-container>
      <ve-pie :data="chartData"></ve-pie>
    </b-container>
  </div>
</template>

<script>
import VePie from 'v-charts/lib/pie.common'
import axios from "axios";
import {API_LOCATION} from "@/config";
import {API_REF_LOCATION} from "@/config";

export default {
  name: 'StatsTipoDonacionesPorCiudad',
  components: {VePie},
  data() {
    return {
      ciudadStats: [],
      ciudad_id: [],
      ciudades: [],
      ciudadSinDonaciones: false, //posiblemente convenga que sea una propiedad computada
      chartData: {
        columns: ['tipo', 'donaciones'],
        rows: [
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
    cityIsEmpty() {
      return Object.keys(this.ciudadStats).length === 0;
    },
    updateStats() {
      this.chartData.rows = [];
      Object.keys(this.ciudadStats).forEach(key => {
        this.chartData.rows.push({'tipo': key , 'donaciones': this.ciudadStats[key] });
      });
    },
    selectCity(){
      axios
        .get(API_LOCATION + 'stats/byCity/' + this.ciudad_id)
        .then(response => {
        this.ciudadStats = response.data;
        })
        .catch(error => {
          console.log(error);
        });
        this.ciudadSinDonaciones = this.cityIsEmpty();
        this.updateStats();
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