<template>
  <div>
    <b-navbar toggleable="lg" type="dark" variant="info" class="p-4">
      <router-link v-bind:to='`/`'>
        <b-navbar-brand class="navbar-titulo font-weight-bold">Centros de Ayuda BA</b-navbar-brand>
      </router-link>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav class="ml-auto">
          <router-link class="spacing text-white navbar-titulo" v-for="routes in links"
                       v-bind:key="routes.id"
                       :to="`${routes.page}`">{{ routes.text }}
          </router-link>
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
@import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@500&display=swap');

.spacing {
  Margin-right: 10px;
}

.navbar-titulo {
  font-family: 'Quicksand', sans-serif;
  text-transform: uppercase;
}
</style>