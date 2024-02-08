<template>
    <div>
      <h1>Welcome User, to Ticket Booking</h1>
      <Headera />
    </div>
  </template>
  
  <script>
  import Headera from '@/components/headera.vue';
  
  export default {
    name: 'HomeView',
    components: {
      Headera,
    },
    mounted() {
      let user = localStorage.getItem('user-info');
      if (!user) {
        this.$router.push({ name: 'Signup' });
      }
    },
  };
  </script>
  