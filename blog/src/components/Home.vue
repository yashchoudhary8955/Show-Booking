<template>
    <div>
        <h1> Welcome User To ticket Booking </h1>
        <Header></Header>
    </div>
</template>

<script>
import Header from './Header.vue'
export default{
    name:'HomeView ',
    components:{
        Header
    },
    mounted(){
        let user = localStorage.getItem('user-info');
        if(!user)
        {
            this.$router.push({ name: 'Signup' })
        }
    }
}
</script>
