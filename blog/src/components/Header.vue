<template>
    <div>
      <router-link to="/">Home</router-link>
      <router-link to="/add">Add Venue</router-link>
      <router-link to="/Update">Update Venue</router-link>
      <router-link to="/addshow">Add show</router-link>
      <router-link to="/TheaterCSVExport">Export CSV</router-link>
      <a href="#">Delete Venue</a>
      <a v-on:click="logout" href="#">Logout</a>
    </div>
  </template>
  
<script>
export default {
    name: 'HeaderView ',
    methods:{
        logout()
        {
            localStorage.clear();
            this.$router.push({ name: 'Login' })
        }
}
}
</script>