<template>
  <h1>Sign up form</h1>
  <div class="register">
    <input type="text" v-model="email" placeholder="Enter your ID">
    <input type="text" v-model="Password" placeholder="Enter your Password">
    <button @click="signup">Sign up</button>
    <p>
      <router-link to="/login">Login</router-link>
    </p>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'SignUpForm',
  data () {
    return {
      email: '',
      Password: ''
    } 
  },
  methods: {
    async signup() {
      let result = await axios.post('http://localhost:3000/user', {
        email: this.email,
        password: this.Password
        });

      console.warn(result);
       if(result.status == 201) {
        localStorage.setItem("user-info", JSON.stringify(result.data))
        this.$router.push({ name: 'Home' })
        }
      }
    },
  //mounted()
  //{
  //  let user = localStorage.getItem('user-info');
  //  if(user)
  //  {
  //    this.$router.push({ name: 'home' })
  //  }
 // }  
}

</script>

<style>
  .register input {
    width: 300px;
    height: 30px;
    margin: 10px;
    border-radius: 5px;
    border: 1px solid #ccc;
    padding: 0 10px;
  }
  .register button {
    width: 300px;
    height: 30px;
    margin: 10px;
    border-radius: 5px;
    border: 1px solid #ccc;
    padding: 0 10px;
    background-color: #ccc;
  }
</style>
