<template>
  <div>
    <b-navbar toggleable="lg" type="dark" variant="info">
      <b-navbar-brand href="#">Centros de Ayuda BA</b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto mr-4">
          <b-navbar-nav>
            <router-link class="spacing text-white" v-for="routes in links"
                         v-bind:key="routes.id"
                         :to="`${routes.page}`">{{ routes.text }}
            </router-link>
          </b-navbar-nav>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>


<script>
export default {
  name: 'Navigation',
  data() {
    return {
      links: [
        {
          id: 0,
          text: 'Home',
          page: '/'
        },
        {
          id: 1,
          text: 'Mapa',
          page: '/mapa'
        },
        {
          id: 2,
          text: 'Solicitudes',
          page: '/solicitudes'
        },
        {
          id: 3,
          text: 'Estadisticas',
          page: '/estadisticas'
        }
      ]
    }
  }
}
</script>
<style>
.spacing {
  Margin-right: 10px;
}
</style>