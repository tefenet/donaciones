<template>
  <div id="app">
    <Navigation></Navigation>
    <b-container fluid="100%" class="pt-5 pb-5">
      <router-view/>
    </b-container>
    <Footer></Footer>
  </div>
</template>

<script>
import Navigation from '@/components/partials/Navbar'
import Footer from '@/components/partials/Footer'

export default {
  name: 'App',
  components: {
    'Navigation': Navigation,
    'Footer': Footer
  }
}
</script>

<style>
@import './assets/styles/base.css';

html {
  position: relative;
  min-height: 100%;
}
</style>
