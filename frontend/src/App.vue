<template>
  <div id="app">
    <a href=""><img id="logo" alt="Mathematical-Guy" src="./assets/logo.png"></a>
    <PortFolio/>
  </div>
</template>

<script>
import PortFolio from './components/PortFolio.vue'

export default {
  name: 'App',
  components: {
    PortFolio
  }
}
</script>

<style>
#logo{
  width: 300px;
  height: 170px;
}
</style>
