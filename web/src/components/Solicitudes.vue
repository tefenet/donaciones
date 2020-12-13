<template>
  <div>
    <b-container>
      <p><span class="titulo">Centros de</span>
        <br/><span class="titulo"> Ayuda</span> <span class="titulo tituloba"> BA</span>
      </p>
    </b-container>
    <b-container>
      <p>
        <span>Bienvenido/a al sitio de Centros de Ayuda de la Provincia de Buenos Aires. A continuación vas a encontrar
          información sobre los centros para poder realizar donaciones de ropa, comida, plasma o sangre.
        </span>
      </p>
      <hr class="my-4">
      <div class="d-flex justify-content-center">
        <b-row align-h="center" class="d-flex align-items-stretch flex-row">
          <b-col md="6" class="mt-4">
            <b-card :img-src=imgCalendar
                    title="Solicitar Turno"
                    img-alt=img-top
                    tag="article"
                    class="mb-2 card-solicitud w-75"
            >
              <b-card-text>
                ¿Querés realizar una donación en el Centro de Ayuda mas cercano a tu barrio? Podés solicitar tu turno
                de manera online a través del sistema de turnos.
              </b-card-text>

              <b-button @click="$router.push('SolicitudTurno')" variant="success">Solicitar Turno</b-button>
            </b-card>
          </b-col>
          <b-col md="6" class="mt-4">
            <b-card :img-src=imgAgregarCentro
                    title="Cargar Centro"
                    img-alt=img-top
                    tag="article"
                    class="mb-2 card-solicitud w-75"
            >
              <b-card-text>
                ¿Hay un centro en tu barrio que no está registrado en el sistema? Podés ingresar los datos y solicitar
                la carga del mismo. Si los datos son correctos, cargaremos el centro.
              </b-card-text>

              <b-button @click="$router.push('SolicitudCentro')" variant="success">Solicitar Centro</b-button>
            </b-card>
          </b-col>
        </b-row>
      </div>
    </b-container>
  </div>
</template>

<script>
import imgCalendar from "@/assets/calendar.jpg"
import imgAgregarCentro from "@/assets/agregar_centro.jpg"

export default {

  name: 'Solicitudes',
  data: function () {
    return {
      imgCalendar: imgCalendar,
      imgAgregarCentro: imgAgregarCentro,
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
@import url('https://fonts.googleapis.com/css2?family=Hammersmith+One&display=swap');

h3 {
  margin: 40px 0 0;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}

</style>
