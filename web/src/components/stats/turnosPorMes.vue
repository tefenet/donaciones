<template>
  <div>
    <p><span class="titulo">Estadísticas</span><br/><span
        class="titulo tituloba">Turnos</span>
    </p>
    <p>
      Gráfico que representa la cantidad de turnos reservados en los municipios en el mes seleccionado.
    </p>
    <br>
    <hr>
    <b-container class="mt-5">
      <b-container style="max-width: 600px">
        <h5>Seleccioná un mes</h5>
        <br>
        <b-form-select v-model="selected" :options="meses"
                       @change="() => getDataMunicipios()"></b-form-select>
        <hr>
        <section v-if="empty">
          <span>No hay datos disponibles para graficar.</span>
        </section>
        <section v-else>
          <ve-bar :data="turnosMunicipios"></ve-bar>
        </section>
      </b-container>
    </b-container>
  </div>
</template>

<script>
import VeBar from 'v-charts/lib/bar.common'
import axios from "axios";
import {API_LOCATION} from "@/config";

export default {
  name: 'TurnosPorMes',
  components: {VeBar},
  data() {
    return {
      turnosMunicipios: {},
      selected: null,
      empty: false,
      meses: [{value: 1, text: 'Enero'}, {value: 2, text: 'Febrero'}, {value: 3, text: 'Marzo'},
        {value: 4, text: 'Abril'}, {value: 5, text: 'Mayo'}, {value: 6, text: 'Junio'}, {value: 7, text: 'Julio'},
        {value: 8, text: 'Agosto'}, {value: 9, text: 'Septiembre'}, {value: 10, text: 'Octubre'},
        {value: 11, text: 'Noviembre'}, {value: 12, text: 'Diciembre'}
      ],
    }
  },
  methods: {
    setDataMunicipios(municipios) {
      return {
        columns: ['Municipio', 'Turnos'],
        rows: municipios
      }
    },
    getDataMunicipios() {
      axios
          .get(API_LOCATION + 'stats/byMonth/' + this.selected)
          .then(response => {
            let data = response.data;
            if (Object.keys(data).length > 0) {
              let municipios = Object.entries(data).map(function (ciudad) {
                return {'Municipio': ciudad[0], 'Turnos': ciudad[1]}
              });
              this.turnosMunicipios = this.setDataMunicipios(municipios)
              this.empty = false;
            } else {
              this.turnosMunicipios = [{text: "No hay turnos disponibles"}]
              this.empty = true;
            }
          })
          .catch(() => {
            this.turnosMunicipios = [{text: "No hay turnos disponibles"}]
            this.empty = true;
          })
    },
  }
}
</script>
<style>
</style>
