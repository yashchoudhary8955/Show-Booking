<template>
    <div class="Login">
      <h1>Login page</h1> 
      <input type="text" v-model="email" placeholder="Enter your ID">
      <input type="text" v-model="password" placeholder="Enter your Password">
      <button v-on:click="login">Login</button>
      <p>
        <RouterLink to="/mainsignup">Sign up</RouterLink>
      </p>
    </div>  
  </template>
  
  <script>
    import axios from 'axios'
  export default {
    name: 'LoginButton',
    data() {
      return {
        email: '',
        password: ''
      };
    },
    methods: {
      async login() 
      {
        let result = await axios.get(
            `http://localhost:3000/mainuser?email=${this.email}&password=${this.password}`
        )

        if(result.status == 200 && result.data.length > 0) 
        {
          localStorage.setItem("user-info", JSON.stringify(result.data))
          this.$router.push({ name: 'UserDashboard' })
        }
        else
        {
          alert("Wrong email or password")
        }
        console.warn(result);  
      }
    }
  };
  </script>
  