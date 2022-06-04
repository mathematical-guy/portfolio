<template>
  <div id="projects">
    <h1>My Projects</h1>
    <ul>
      <li v-for="project in projects" :key="project.index">
        <h2>{{ project.name }}</h2>
        {{ project.description }}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Projects",
  data() {
    return {
      projects: [],
    };
  },
  methods: {
    getProjects() {
      let config = {
        method: "get",
        url: "http://localhost:8000/projects/",
        auth: {
          username: "admin",
          password: "admin",
        },
      };

      axios(config)
      .then((response) => {
        console.log(response.data);
        this.projects = response.data;
      });
    },
  },

  mounted() {
    this.getProjects();
  },

};
</script>

<style>
#projects {
  margin-left: 30px;
  border: 2px;
  border-color: red;
  border-style: double dashed;
  margin-bottom: 30px;
}
</style>