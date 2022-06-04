<template>
  <div id="skills">
    <h1>My Skills</h1>
    <ul>
      <li v-for="skill in skills" :key="skill.index">
        {{ skill.name }} - {{ skill.strength }}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Skills",
  data() {
    return {
      skills: [],
    };
  },
  mounted() {
    this.getSkills();
  },
  methods: {
    getSkills() {
      let config = {
        method: "get",
        url: "http://127.0.0.1:8000/skills/",
        auth: {
          username: "admin",
          password: "admin",
        },
      };
      axios(config)
      .then((response) => {
        this.skills = response.data;
      });
    },
  },
};
</script>

<style>
#skills {
  margin-left: 30px;
  border: 2px;
  border-color: black;
  border-style: dashed;
  margin-bottom: 30px;
}
</style>