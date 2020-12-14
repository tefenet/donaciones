<template>
  <b-container id="header-info">
    <section v-if="errored">
      <p>Ha ocurrido un error! Intentá nuevamente</p>
    </section>

    <section v-else>
      <p><span class="titulo">Solicitar lacarga de un nuevo</span><br/>
        <span class="titulo tituloba">Centro de Ayuda</span>
      </p>
      <b-container class="mt-5">
        <hr>
        <b-alert variant="success" dismissible fade :show="showSuccessAlert" @dismissed="showSuccessAlert=false">
          Solicitud de carga de centro registrada exitosamente!
        </b-alert>
        <b-alert variant="danger" dismissible fade :show="showErrorAlert" @dismissed="showErrorAlert=false">
          Error al procesar la solicitud de carga, intentá nuevamente.
        </b-alert>
        <b-row>
          <b-col md="6">
            <b-form @submit="onSubmit" @reset="onReset" v-if="show">
              <b-form-group
                  id="nombre-group"
                  label="Nombre del Centro:"
                  label-for="input-nombre"
              >
                <b-form-input
                    id="input-nombre"
                    v-model="form.nombre"
                    required
                    placeholder="Centro Springfield"
                ></b-form-input>
              </b-form-group>

              <b-form-group
                  id="direccion-group"
                  label="Dirección del centro:"
                  label-for="input-direccion"
              >
                <b-form-input
                    id="input-direccion"
                    v-model="form.direccion"
                    required
                    placeholder="Av. Siempre Viva 123"
                ></b-form-input>
              </b-form-group>

              <b-form-group
                  id="telefono-group"
                  label="Número de Teléfono:"
                  label-for="input-telefono"
              >
                <b-form-input
                    id="input-telefono"
                    v-model="form.telefono"
                    type="number"
                    required
                    placeholder="1154345431"
                ></b-form-input>
              </b-form-group>

              <b-form-group
                  id="apertura-group"
                  label="Horario de apertura:"
                  label-for="input-apertura"
              >
                <b-form-input id="input-apertura" type="time" v-model="form.hora_apertura" required></b-form-input>
              </b-form-group>

              <b-form-group
                  id="cierre-group"
                  label="Horario de cierre:"
                  label-for="input-cierre"
              >
                <b-form-input id="input-cierre" type="time" v-model="form.hora_cierre" required></b-form-input>
              </b-form-group>

              <b-form-group
                  id="tipo-group"
                  label="Tipo de Centro:"
                  label-for="input-tipo"
              >
                <b-form-input
                    id="input-tipo"
                    v-model="form.tipo"
                    required
                    placeholder="Merendero"
                ></b-form-input>
              </b-form-group>

              <b-form-group
                  id="web-group"
                  label="Dirección web del Centro:"
                  label-for="input-web"
              >
                <b-form-input
                    id="input-web"
                    v-model="form.web"
                    type="url"
                    required
                    placeholder="http://www.homerswebpage.com/"
                ></b-form-input>
              </b-form-group>

              <b-form-group
                  id="email-group"
                  label="Dirección de correo:"
                  label-for="input-email"
              >
                <b-form-input
                    id="input-email"
                    v-model="form.email"
                    type="email"
                    required
                    placeholder="Ingresar email"
                ></b-form-input>
              </b-form-group>

              <b-form-group id="ciudad-group" label="Seleccione una ciudad" label-for="input-ciudad">
                <b-form-select id="input-ciudad" v-model="form.ciudad_id" :options="ciudades" required size="sm"
                               @change="() => {this.disableEnviar=false}">
                </b-form-select>
              </b-form-group>

              <b-form-group
                  id="coordenadas-group"
                  label="Coordenadas"
                  label-for="input-coordenadas"
              >
                <b-form-input
                    id="input-coordenadas"
                    v-model="this.coordenadasStr"
                    readonly
                ></b-form-input>
              </b-form-group>
              <div class="form-group row">
                <label for="robot" class="col-sm-2 col-form-label"></label>
                <div class="col-sm-10">
                  <vue-recaptcha ref="recaptcha"
                                 @verify="onVerify" sitekey="6Ld1mwUaAAAAAJXmnW-cIA3lSU_rzgGlsJxjpczd"
                                 accesskey="6Ld1mwUaAAAAAMGTFRRxhi518S_TIr1Bl-Giks80"
                                 :loadRecaptchaScript="true">
                  </vue-recaptcha>
                </div>
              </div>

              <b-button type="submit" variant="info" :disabled="disableEnviar">Enviar</b-button>
              <b-button type="reset" variant="danger">Reset</b-button>
            </b-form>
          </b-col>
          <b-col md="6" class="p-4">
            <l-map :zoom="zoom" :center="center" @click="handleMapClick">
              <l-tile-layer :url="url" :attribution="attribution"></l-tile-layer>
              <l-marker :lat-lng="marker"></l-marker>
            </l-map>
          </b-col>
        </b-row>
      </b-container>
    </section>
  </b-container>
</template>

<script>
import {latLng} from "leaflet";
import {LMap, LTileLayer, LMarker} from "vue2-leaflet";
import axios from "axios";
import {API_LOCATION, API_REF_LOCATION} from "@/config";
import VueRecaptcha from 'vue-recaptcha';


export default {
  name: "CargarCentro",
  components: {
    LMap,
    LTileLayer,
    LMarker,
    'vue-recaptcha': VueRecaptcha,
  },

  data() {
    return {
      ciudades: [],
      coordenadas: [-34.629317, -58.598996],
      coordenadasStr: '',
      show: true,
      //  Leaflet vars
      zoom: 10,
      center: latLng(-34.629317, -58.598996),
      url: "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
      attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
      // form vars
      errored: false,
      disableEnviar: true,
      marker: latLng(0, 0),
      form: {
        nombre: '',
        direccion: '',
        telefono: '',
        hora_apertura: '',
        hora_cierre: '',
        tipo: '',
        web: '',
        email: '',
        ciudad_id: '',
        gl_long: '',
        gl_lat: '',
        robot: false,
      },
      showErrorAlert: false,
      showSuccessAlert: false,
    };
  },
  methods: {
    onSubmit(evt) {
      evt.preventDefault();
      if (this.form.hora_cierre <= this.form.hora_apertura) {
        alert("La hora de cierre no puede ser menor a la hora de apertura");
      } else if ((this.form.gl_lat || this.form.gl_long) === '') {
        alert("Seleccioná un punto en el mapa!");
      } else {
        var data = JSON.stringify(this.form);
        if (this.form.robot) {
          this.cargarCentro(data);
        }
      }
    },
    resetForm() {
      this.form.nombre = ''
      this.form.direccion = ''
      this.form.telefono = ''
      this.form.hora_apertura = ''
      this.form.hora_cierre = ''
      this.form.tipo = ''
      this.form.web = ''
      this.form.email = ''
      this.form.ciudad_id = ''
      this.form.gl_long = ''
      this.form.gl_lat = ''
      // Trick to reset/clear native browser form validation state
      this.show = false
      this.$nextTick(() => {
        this.show = true
      })
      this.marker = latLng(0, 0)
      this.coordenadasStr = ''
    }
    ,
    onReset(evt) {
      evt.preventDefault()
      // Reset our form values
      this.resetForm();
    },
    handleMapClick(event) {
      this.marker = event.latlng;
      this.form.gl_lat = event.latlng.lat;
      this.form.gl_long = event.latlng.lng;
      this.coordenadasStr = event.latlng.lat.toString() + ', ' + event.latlng.lng.toString();
    },
    optionsCiudades(ciudadesResponse) {
      return Object.values(ciudadesResponse).map(function (c) {
        return {'value': c.id, 'text': c.name};
      });
    },
    cargarCentro(centroJson) {
      axios
          .post(API_LOCATION + 'centros/', centroJson,
              {
                headers: {
                  "content-type": "application/json", "Accept": "application/json"
                }
              }
          )
          .then(() => {
            this.showSuccessAlert = true;
            this.resetForm();
          })
          .catch(() => {
            this.showErrorAlert = true;
            // this.resetForm();
          })
    },
    onVerify: function (response) {
      if (response) this.form.robot = true;
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
}
</script>
<style>
</style>