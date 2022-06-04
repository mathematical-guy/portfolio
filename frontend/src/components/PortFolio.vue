<template>
  <div class="main">
    <Skills />
    <Projects />
  </div>
</template>

<script>
import Skills from "./Skills.vue";
import Projects from "./Projects.vue";

export default {
  name: "PortFolio",
  props: {
    msg: String,
  },
  components: {
    Skills,
    Projects,
  },
};
</script>

<style>
</style>
