<template>
  <div>
    <h1>Solicitudes</h1>
    <b-row align-h="center" class="d-flex align-items-stretch">
      <b-col md="3" class="mt-4">
        <b-card :img-src=nuevoTurno
                title="Solicitar un turno para realizar una donación"
                img-alt=img-top
                tag="article"
                style="max-width: 20rem;"
                class="mb-2"
        >
        <b-card-text>
            En esta seccion vas a poder solicitar un turno para realizar una donación en alguno de los centros de ayuda listados en nuestra pagina.
        </b-card-text>
        <b-button @click="$router.push('solicitudTurno')" variant="success">Solicitar un turno</b-button>
        </b-card>
      </b-col>
      <b-col md="3" class="mt-4">
        <b-card :img-src=nuevoCentro
                title="Publicar un nuevo Centro de Ayuda"
                img-alt=img-top
                tag="article"
                style="max-width: 20rem;"
                class="mb-2"
        >
        <b-card-text>
            En esta seccion vas a poder solicitar la publicación de un nuevo centro de ayuda en la pagina.
        </b-card-text>
        <b-button @click="$router.push('solicitudCentro')" variant="success">Solicitar Publicación de un Centro</b-button>
        </b-card>
      </b-col>
  </b-row>
  </div>
</template>


<script>
import nuevoCentro from "@/assets/nuevoCentro.png"
import nuevoTurno from "@/assets/nuevoTurno.png"
export default {
    name: 'Solicitudes',
    data: function () {
        return {
            nuevoCentro: nuevoCentro,
            nuevoTurno: nuevoTurno,
        }
    }
}
</script>
<style>
</style>
