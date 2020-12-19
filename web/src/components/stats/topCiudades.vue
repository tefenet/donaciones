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
  name: 'Estadisticas',
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
  methods: {
    /*addCenterToGraph(ciudad){
      this.chartData.rows.push({'ciudad': ciudad[1] , 'donaciones': ciudad[1]});
    }*/
  },
  mounted() {
    axios.get(API_LOCATION + 'stats/topSixCities')
    .then(response => {
      this.ciudades = response.data;
      //this.centros.forEach(this.addCenterToGraph());
      this.chartData.rows.push({'ciudad': 'La Plata', 'donaciones': 6}); //push de un elemento de prueba
    })
    .catch(error => {
      console.log(error);
    })
  }

}

</script>
<style>
</style>
