<template>
    <div>
      <router-link to="/venuelist">Venue List</router-link>
      <router-link to="/mytickets">Add Venue</router-link>
      <a v-on:click="logout" href="#">Logout</a>
    </div>
  </template>
  
  <script>
  export default {
  name: 'HeaderAreaComponent', // Updated component name
  methods: {
    logout() {
      // Handle logout logic here
    },
  },
};
  </script>