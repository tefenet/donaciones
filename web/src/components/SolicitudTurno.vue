<template>
  <b-container id="header-info">
    <section v-if="errored">
      {{ $router.push('/404') }}
    </section>

    <section v-else>
      <div v-if="loading">Cargando...</div>

      <div
          v-else
      >
        <p><span class="titulo">Solicitar Turno para el centro</span><br/><span
            class="titulo tituloba">{{ centro.nombre }}</span>
        </p>
        <p>
      <span class="texto-centro">
        <font-awesome-icon :icon="['fa', 'map-marker-alt']" style="color: darkcyan;"/> {{ centro.direccion }}
        ({{ ciudad[centro.city_id].name }}) |
        <font-awesome-icon :icon="['fa', 'info-circle']"
                           style="color: darkcyan;"/> {{ capitalizarPalabra(centro.tipo) }}
      </span><br>
          <span class="texto-centro">
        <font-awesome-icon :icon="['fa', 'clock']" style="color: darkcyan;"/>
        {{ centro.hora_apertura }} - {{ centro.hora_cierre }}
      </span>
          <span class="texto-centro">&nbsp; &nbsp;
        <font-awesome-icon :icon="['fa', 'phone']" style="color: darkcyan;"/> {{ centro.telefono }}
      </span>
          <br>
        </p>
        <hr>
        <b-alert variant="success" dismissible fade :show="showSuccessAlert" @dismissed="showSuccessAlert=false">
          Turno reservado exitosamente!
        </b-alert>
        <b-alert variant="danger" dismissible fade :show="showErrorAlert" @dismissed="showErrorAlert=false">
          Error al reservar turno, intentá nuevamente.
        </b-alert>
        <b-container style="max-width: 650px">
          <b-form @submit="onSubmit" @reset="onReset" v-if="show">
            <b-form-group
                id="email-group"
                label="Dirección de correo:"
                label-for="input-email"
            >
              <b-form-input
                  id="input-email"
                  v-model="form.email_donante"
                  type="email"
                  required
                  placeholder="diegol@gmail.com"
              ></b-form-input>
            </b-form-group>

            <b-form-group id="telefono-group" label="Teléfono:" label-for="input-telefono">
              <b-form-input
                  id="input-telefono"
                  v-model="form.telefono_donante"
                  required
                  placeholder="221 555 5555"
              ></b-form-input>
            </b-form-group>

            <b-form-group id="fecha-group" label="Fecha:" label-for="input-fecha">
              <b-form-datepicker
                  id="input-fecha"
                  :date-format-options="{ year: 'numeric', month: 'numeric', day: 'numeric' }"
                  :min="min"
                  v-model="form.fecha"
                  locale="es"
                  @input="handleFechaOnChange"
              ></b-form-datepicker>
            </b-form-group>

            <b-form-group id="horario-group" label="Horario:" label-for="input-horario">
              <b-form-select id="input-horario" v-model="form.hora_inicio" :options="horarios" size="sm">

              </b-form-select>
            </b-form-group>
            <b-button type="submit" variant="info" size="sm">Reservar</b-button>
            <b-button type="reset" variant="danger" size="sm">Resetear</b-button>
          </b-form>
        </b-container>
      </div>
    </section>
  </b-container>
</template>

<script>
import axios from 'axios';
import {API_LOCATION, API_REF_LOCATION} from '@/config';
import moment from 'moment';

export default {
  name: 'SolicitudTurno',
  data() {
    const now = new Date();
    const today = new Date(now.getFullYear(), now.getMonth(), now.getDate());
    const minDate = new Date(today);
    return {
      perPage: 5,
      currentPage: 1,
      ciudad_id: 1,
      centro: {},
      ciudad: {},
      loading: true,
      errored: false,
      min: minDate,
      form: {
        email_donante: '',
        telefono_donante: '',
        fecha: null,
        hora_inicio: null
      },
      horarios: [{text: "No hay turnos disponibles", value: '', disabled: true}],
      horariosResponse: {},
      show: true,
      showSuccessAlert: false,
      showErrorAlert: false
    }
  },
  methods: {
    capitalizarPalabra(string) {
      return string.charAt(0).toUpperCase() + string.slice(1);
    },
    calcularHoraFin(horaInicio) {
      return moment.utc(horaInicio, 'HH:mm').add(30, 'minutes').format('HH:mm');
    },
    onSubmit(evt) {
      console.log(this.centro.id)
      evt.preventDefault()
      let turnoJson = this.form
      turnoJson['centro_id'] = this.centro.id
      turnoJson['hora_fin'] = this.calcularHoraFin(turnoJson['hora_inicio'])
      console.log(JSON.stringify(turnoJson))
      this.reservarTurno(turnoJson)
    },
    resetForm() {
      this.form.email_donante = ''
      this.form.telefono_donante = ''
      this.form.fecha = ''
      this.form.hora = ''
      this.horarios = [{text: "No hay turnos disponibles", value: '', disabled: true}]
      this.form.checked = []
      // Trick to reset/clear native browser form validation state
      this.show = false
      this.$nextTick(() => {
        this.show = true
      })
    },
    onReset(evt) {
      evt.preventDefault()
      // Reset our form values
      this.resetForm();
    },
    listarHorarios(horarios) {
      return horarios.map(function (horario) {
        return moment.utc(horario.hora_inicio, 'HH:mm').format("HH:mm");
      });
    },
    setHorariosDisponibles(fecha) {
      axios
          .get(API_LOCATION + 'centros/' + this.centro.id + '/turnos_disponibles?fecha=' + fecha)
          .then(response => {
            let listaHorarios = this.listarHorarios(response.data.turnos);
            this.horarios = listaHorarios.length > 0 ? listaHorarios : [{
              text: "No hay turnos disponibles",
              value: '',
              disabled: true
            }];
          })
          .catch(() => {
            this.horarios = [{text: "No hay turnos disponibles", value: '', disabled: true}]
          })
    },
    reservarTurno(turnoJson) {
      axios
          .post(API_LOCATION + 'centros/' + this.centro.id + '/reserva', turnoJson)
          .then(() => {
            this.showSuccessAlert = true;
            this.resetForm();
          })
          .catch(() => {
            this.showErrorAlert = true;
            this.resetForm();
          })
    },
    handleFechaOnChange() {
      console.log(this.form.fecha);
      this.setHorariosDisponibles(this.form.fecha);
    },
  },
  mounted() {
    axios
        .get(API_LOCATION + 'centros/' + this.$route.params.centro_id)
        .then(response => {
          this.centro = response.data.centro;
          axios
              .get(API_REF_LOCATION + 'municipios/' + this.centro.city_id)
              .then(response => {
                this.ciudad = response.data.data.Town;
              })
              .catch(error => {
                console.log(error);
                this.errored = true;
              })
        })
        .catch(error => {
          console.log(error);
          console.log("asdasdasda");
          this.errored = true;
        })
        .finally(() => {
          this.loading = false;
        });
  }
}

</script>

<style>
</style>