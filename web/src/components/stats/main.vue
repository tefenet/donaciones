<template>
  <div>
    <b-container>
        <p><span class="titulo">Estadísticas sobre nuestros centros de</span>
          <br/><span class="titulo"> Ayuda</span> <span class="titulo tituloba"> BA</span>
        </p>
    </b-container>
    <div>
  <b-container>
        <p>
          <span>En esta página podes consultar diferentes estadísticas con respecto a las donaciones realizadas en los centros de ayuda publicados en nuestro sitio.
          </span>
        </p>
        <hr class="my-4">
        <div class="d-flex justify-content-center">
          <b-row align-h="center" class="d-flex align-items-stretch flex-row">
            <b-col md="4" class="mt-4">
              <b-card title="Estadísticas de donaciones por ciudad en cada mes"
                      img-alt=img-top
                      tag="article"
                      class="mb-2"
              >
                <b-card-text>
                  En esta sección podes ver gráficos sobre la cantidad de donaciones realizadas en las distintas ciudades del país, en el mes que vos elijas.
                </b-card-text>

                <b-button @click="$router.push('Estadisticas/TurnosPorMes')" variant="success">Ver estadisticas</b-button>
              </b-card>
            </b-col>
            <b-col md="4" class="mt-4">
                <b-card title="Estadistícas de tipos de donaciones en cada ciudad"
                      img-alt=img-top
                      tag="article"
                      class="mb-2"
              >
                <b-card-text>
                  En esta sección podes ver gráficos sobre qué tipos de donaciones (alimentos, salud, ropa, etc) se realizaron en cada ciudad.
                </b-card-text>

                <b-button @click="$router.push('Estadisticas/TurnosPorCiudad')" variant="success">Ver estadisticas</b-button>
              </b-card>
            </b-col>
            <b-col md="4" class="mt-4">
              <b-card title="Top 6 ciudades con mas donaciones de alimentos por mes"
                      img-alt=img-top
                      tag="article"
                      class="mb-2"
              >
                <b-card-text>
                 En esta sección podes ver el top 6 de ciudades con más donaciones de alimentos en los distintos meses del año.
                </b-card-text>

                <b-button @click="$router.push('Estadisticas/TopCiudades')" variant="success">Ver estadisticas</b-button>
              </b-card>
            </b-col>
          </b-row>
        </div>
      </b-container>
    </div>

  </div>
</template>
<script>
import estadisticas from "@/assets/estadisticas.jpg"

export default {

  name: 'Estadisticas',
  props: {
    msg: String,
  },
  data: function () {
    return {
      estadisticas: estadisticas,
    }
  }
}

</script>


<style>
</style>