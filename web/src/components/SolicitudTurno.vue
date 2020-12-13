<template>
  <b-container id="header-info">
    <p><span class="titulo">Solicitar</span><br/><span class="titulo tituloba">Turno</span>
    </p>
    <p>
      <span>
        ¿Querés realizar una donación en el Centro de Ayuda mas cercano a tu barrio? <br>
        Seleccioná un centro y elegí un día y horario disponible para concurrir
      </span>
      <br>
    </p>
  </b-container>
</template>

<script>
import axios from 'axios';

export default {
  name: 'SolicitudTurno',
  data() {
    return {
      perPage: 5,
      currentPage: 1,
      centros: [],
      ciudades: [],
      loading: true,
      errored: false,
      get itemsForList() {
        return this.centros.slice(
            (this.currentPage - 1) * this.perPage,
            this.currentPage * this.perPage,
        );
      }
    }
  },
  computed: {
    rows() {
      return this.centros.length
    }
  },
  methods: {
    capitalizarPalabra(string) {
      return string.charAt(0).toUpperCase() + string.slice(1);
    }
  },
  mounted() {
    axios
        .get('https://api-referencias.proyecto2020.linti.unlp.edu.ar/municipios?per_page=1000')
        .then(response => {
          this.ciudades = response.data.data.Town;
          console.log(this.ciudades);
        })
        .catch(error => {
          console.log(error);
          this.errored = true;
        })
    axios
        .get('https://admin-grupo56.proyecto2020.linti.unlp.edu.ar/api/v1.0/centrosAll')
        .then(response => {
          this.centros = response.data.centros;
        })
        .catch(error => {
          console.log(error);
          this.errored = true;
        })
        .finally(() => this.loading = false);
  },
}

</script>

<style>
</style>