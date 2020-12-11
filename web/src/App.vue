<template>
  <div id="app">
    <Navigation></Navigation>
    <div class="mt-5"></div>
    <router-view/>
    <div class="mb-5 text-white">.</div>
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
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  position: relative;
  min-height: 100vh;
  padding-bottom: 60px;
}
</style>
