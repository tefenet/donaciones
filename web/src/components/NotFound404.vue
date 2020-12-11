<template>
  <div>
    <p>
      <span class="not-found-title">404</span>
    </p>
    <p>
      <span class="not-found-text">página no encontrada</span>
    </p>
  </div>
</template>

<script>
export default {
  name: 'Solicitudes' //this is the name of the component
}
</script>
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@600&display=swap');

.not-found-title {
  font-family: 'Cairo', sans-serif;
  font-size: 20vh;
}

.not-found-text {
  font-family: 'Cairo', sans-serif;
  font-size: 5vh;
  font-weight: bold;
}
</style>