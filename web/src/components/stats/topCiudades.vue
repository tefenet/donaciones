<template>
  <div>
    <h1>Estadisticas</h1>
    <p>Top 6 de ciudades con mas donaciones de alimentos </p>
    <b-container>
      <ve-bar :data="chartData"></ve-bar>
    </b-container>
  </div>
</template>

<script>
import VeBar from 'v-charts/lib/bar.common'
import axios from "axios";
import {API_LOCATION} from "@/config";

export default {
  name: 'StatsTopCiudades',
  components: {VeBar},
  data() {
    return {
      ciudades: [],
      chartData: {
        columns: ['ciudad', 'donaciones'],
        rows: [
        ]
      }
    }
  },
  mounted() {
    axios.get(API_LOCATION + 'stats/topSixCities')
    .then(response => {
      this.ciudades = response.data;
      Object.keys(this.ciudades).forEach(key => {
        this.chartData.rows.push({'ciudad': key , 'donaciones': this.ciudades[key] });
      });
    })
    .catch(error => {
      console.log(error);
    })
  }
}
</script>
<style>
</style>
