<template>
  <div>
    <h1>Welcome to Add Shows</h1>
    <Header></Header>

    <!-- Form to Add Show -->
    <h2>Add a New Show</h2>
    <form @submit.prevent="addShow">
      <div>
        <label for="venue">Select Venue:</label>
        <select v-model="selectedVenue" required>
          <option v-for="venue in venues" :key="venue.id" :value="venue.id">{{ venue.name }}</option>
        </select>
      </div>
      <div>
        <label for="name">Show Name:</label>
        <input type="text" id="name" v-model="show.name" required />
      </div>
      <div>
        <label for="rating">Rating:</label>
        <input type="number" id="rating" v-model="show.rating" required />
      </div>
      <div>
        <label for="timing">Timing:</label>
        <input type="text" id="timing" v-model="show.timing" required />
      </div>
      <div>
        <label for="tags">Tags:</label>
        <input type="text" id="tags" v-model="show.tags" required />
      </div>
      <div>
        <label for="price">Price:</label>
        <input type="number" id="price" v-model="show.price" required />
      </div>
      <div>
        <label for="count">Count:</label>
        <input type="number" id="count" v-model="show.count" required />
      <button type="submit">Add Show</button>
      </div>

    </form>

    <!-- Display All Venues -->
    <h2>All Venues</h2>
    <ul>
      <li v-for="venue in venues" :key="venue.id">
        {{ venue.name }} - {{ venue.location }} ({{ venue.city }})
      </li>
    </ul>
  </div>
</template>

<script>
import Header from './Header.vue';

export default {
  name: 'AddShows', // Make sure the name matches
  components: {
    Header,
  },
  data() {
    return {
      venues: [],
      selectedVenue: '',
      show: {
        name: '',
        rating: 0,
        timing: '',
        tags: '',
        price: 0,
        count: 0,
      },
    };
  },
  mounted() {
    this.fetchVenues();
  },
  methods: {
  fetchVenues() {
  fetch('http://localhost:3002/api/getVenuess')
    .then((response) => response.json())
    .then((data) => {
      // Assuming data is an array of arrays, convert it to an array of objects
      this.venues = data.map(venueArray => ({
        id: venueArray[0],
        name: venueArray[1],
        location: venueArray[2],
        city: venueArray[3]
      }));
    })
    .catch((error) => console.error('Error:', error));
},

    addShow() {
      fetch(`http://localhost:3002/api/addshow/${this.selectedVenue}`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(this.show),
      })
        .then((response) => response.json())
        .then((data) => {
          console.log(data.message);
          this.show = {
            name: '',
            rating: 0,
            timing: '',
            tags: '',
            price: 0,
            count: 0,
          };
          this.fetchVenues();
        })
        .catch((error) => console.error('Error:', error));
    },
  },
};
</script>