<!-- eslint-disable vue/multi-word-component-names -->
<template>
    <div class="main-home">
      <h1>Welcome to Main Home</h1>
      <button @click="redirectToAdminLogin">Admin</button>
      <button @click="redirectToUserLogin">User</button>
    </div>
  </template>
  
  <script>
  export default {
    methods: {
      redirectToAdminLogin() {
        this.$router.push('/Login');
      },
      redirectToUserLogin() {
        this.$router.push('/mainlogin');
      }
    }
  };
  </script>
  