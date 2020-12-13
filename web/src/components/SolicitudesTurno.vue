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
    <b-container class="mt-5">
      <section v-if="errored">
        <p>Lo sentimos, no es posible obtener la información en este momento, por favor intente nuevamente mas tarde</p>
      </section>

      <section v-else>
        <div v-if="loading">Cargando...</div>

        <div
            v-else
        >
          <b-list-group id="listaCentros">
            <b-list-group-item v-for="centro in itemsForList"
                               :key="centro.id">
              <b-row align-content="center" align-v="center" align-h="center">
                <b-col>
                  <span class="font-weight-bold" style="font-size: 15px;">
                    {{ centro.nombre }} - {{ ciudades[centro.city_id].name }}</span><br>
                  <span class="texto-centro">
                        <font-awesome-icon :icon="['fa', 'map-marker-alt']" style="color: darkcyan;"/>
                        {{ centro.direccion }} |  <font-awesome-icon :icon="['fa', 'info-circle']"
                                                                     style="color: darkcyan;"/>
                        {{ capitalizarPalabra(centro.tipo) }}
                      </span><br>
                  <span class="texto-centro">
                        <font-awesome-icon :icon="['fa', 'clock']" style="color: darkcyan;"/>
                        {{ centro.hora_apertura }} - {{ centro.hora_cierre }}
                      </span><br>
                  <span class="texto-centro">
                        <font-awesome-icon :icon="['fa', 'phone']" style="color: darkcyan;"/> {{ centro.telefono }}<br>
                      </span>

                </b-col>
                <b-col sm="6">
                  <b-button @click="$router.push({name:'ReservaTurno', params:{centro_id: centro.id}})" size="sm"
                            variant="info"><b>Solicitar Turno</b>
                  </b-button>
                </b-col>
              </b-row>
            </b-list-group-item>
          </b-list-group>
          <br>
          <b-pagination
              v-model="currentPage"
              :total-rows="rows"
              :per-page="perPage"
              aria-controls="listaCentros"
              align="center"
              pills
          ></b-pagination>
        </div>
      </section>
    </b-container>
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