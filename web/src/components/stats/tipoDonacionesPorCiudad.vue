
<template>
  <div>
    <h1>Estadisticas</h1>
    <p>Tipos de Donaciones por ciudad</p>
    <b-container>
      <ve-pie :data="chartData"></ve-pie>
    </b-container>
  </div>
</template>

<script>
import VePie from 'v-charts/lib/pie.common'
//import axios from "axios";
//import {API_LOCATION} from "@/config";

export default {
  name: 'StatsTipoDonacionesPorCiudad',
  components: {VePie},
  data() {
    return {
      chartData: {
        columns: ['date', 'cost', 'profit'],
        rows: [
          {'date': '01/01', 'cost': 123, 'profit': 3},
          {'date': '01/06', 'cost': 7123, 'profit': 20}
        ]
      }
    }
  }
}
</script>
<style>
</style>