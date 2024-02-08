<template>
<router-link to ="/footer">home</router-link>
<router-view></router-view>
</template>

<script>
// No need to import signup here
export default {
  name: 'HomeView ',
}
</script>


<style>
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
  }

</style>