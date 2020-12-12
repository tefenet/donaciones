<template>
  <div>
    <b-container>
      <p><span class="titulo">Centros de</span>
        <br/><span class="titulo"> Ayuda</span> <span class="titulo tituloba"> BA</span>
      </p>
      <!--      <img :src="require('@/assets/logo_gba.png')" class="img-fluid h-25 w-25"/>-->
    </b-container>>
    <b-container>
      <p>
        <span>Bienvenido/a al sitio de Centros de Ayuda de la Provincia de Buenos Aires. A continuación vas a encontrar
          información sobre los centros para poder realizar donaciones de ropa, comida, plasma o sangre.
        </span>
      </p>
      <hr class="my-4">
      <div class="d-flex justify-content-center">
        <b-row align-h="center" class="d-flex align-items-stretch flex-row">
          <b-col md="4" class="mt-4">
            <b-card :img-src=mapaBa
                    title="Mapa de Centros"
                    img-alt=img-top
                    tag="article"
                    style="max-width: 20rem;"
                    class="mb-2"
            >
              <b-card-text>
                En este mapa vas a poder buscar los Centros de Ayuda mas cercanos a tu barrio, ya que se encuentran
                georeferenciados en el mapa de la provincia de Buenos Aires
              </b-card-text>

              <b-button @click="$router.push('Mapa')" variant="success">Ir al mapa</b-button>
            </b-card>
          </b-col>
          <b-col md="4" class="mt-4">
            <b-card :img-src=logoBa
                    title="Solicitudes"
                    img-alt=img-top
                    tag="article"
                    style="max-width: 20rem;"
                    class="mb-2"
            >
              <b-card-text>
                En esta seccion vas a poder solicitar turnos para concurrir al Centro de Ayuda mas cercano a tu barrio.
                También vas a poder solicitar la carga de un nuevo Centro de Ayuda en el sistema.
              </b-card-text>

              <b-button @click="$router.push('Solicitudes')" variant="success">Ir a Solicitudes</b-button>
            </b-card>
          </b-col>
          <b-col md="4" class="mt-4">
            <b-card :img-src=estadisticas
                    title="Estadísticas"
                    img-alt=img-top
                    tag="article"
                    style="max-width: 20rem;"
                    class="mb-2"
            >
              <b-card-text>
                En esta seccion vas a poder consultar las estadísticas de
                a los centros de ayuda social en gráficos con
                distintos formatos.
              </b-card-text>

              <b-button @click="$router.push('Estadisticas')" variant="success">Ir a Estadísticas</b-button>
            </b-card>
          </b-col>
        </b-row>
      </div>
    </b-container>
  </div>
</template>

<script>
import mapaBa from "@/assets/mapa_ba.jpg"
import logoBa from "@/assets/logo_gba_card.png"
import estadisticas from "@/assets/estadisticas.jpg"

export default {

  name: 'Home',
  props: {
    msg: String,
  },
  data: function () {
    return {
      mapaBa: mapaBa,
      logoBa: logoBa,
      estadisticas: estadisticas,
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
