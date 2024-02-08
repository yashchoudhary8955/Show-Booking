<template>
  <div>
    <h1>Welcome User To Add Venue</h1>
    <Header></Header>
    <form @submit.prevent="addVenue">
      <div>
        <label for="name">Name:</label>
        <input type="text" id="name" v-model="venue.name" required />
      </div>
      <div>
        <label for="location">Location:</label>
        <input type="text" id="location" v-model="venue.location" required />
      </div>
      <div>
        <label for="city">City:</label>
        <input type="text" id="city" v-model="venue.city" required />
      </div>
      <div>
        <label for="count">Count:</label>
        <input type="number" id="count" v-model="venue.count" required />
      </div>
      <button type="submit">Add Venue</button>
    </form>
  </div>
</template>

<script>
import Header from './Header.vue';

export default {
  name: 'AddView',
  components: {
    Header,
  },
  data() {
    return {
      venue: {
        name: '',
        location: '',
        city: '',
        count: 0,
      },
    };
  },
  methods: {
    addVenue() {
      fetch('http://localhost:3002/api/addVenue', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(this.venue),
      })
        .then((response) => response.json())
        .then((data) => {
          console.log(data.message);
          // Clear the form after successful addition
          this.venue = {
            name: '',
            location: '',
            city: '',
            count: 0,
          };
        })
        .catch((error) => console.error('Error:', error));
    },
  },
};
</script>
