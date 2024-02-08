<template>
  <div>
    <h1>Venues and Shows</h1>
    <div v-for="venue in venues" :key="venue.id">
      <h2 @click="showVenueDetails(venue)">{{ venue.name }}</h2>
      <p>Location: {{ venue.location }}, {{ venue.city }}</p>
      <!-- Rest of the content -->
    </div>
    <VenueDetail v-if="selectedVenue" :venue="selectedVenue" @book-show="bookShow" />
  </div>
</template>

<script>
import axios from 'axios';
import VenueDetail from './VenueDetail.vue';

export default {
  
  name: 'VenueList',
  components: {
    VenueDetail,
  },
  data() {
    return {
      venues: [],
      selectedVenue: null,
    };
  },
  mounted() {
    this.fetchVenues();
  },

  methods: {
    fetchVenues() {
      axios
        .get('http://127.0.0.1:3002/api/getVenues', {
          params: {
            includeshows: true,
          },
        })
        .then(response => {
          this.venues = response.data;
        })
        .catch(error => {
          console.error('Error fetching venues:', error);
        });
    },
    showVenueDetails(venue) {
      this.selectedVenue = venue;
    },
    bookShow(venueId, showId, tickets) {
    // Ensure the tickets value is a positive integer
    tickets = parseInt(tickets);
    if (isNaN(tickets) || tickets <= 0) {
      console.error('Invalid number of tickets');
      return;
    }

    // Send the booking request
    // axios
    //   .post
    //(`http://127.0.0.1:3000/api/venues/${venueId}/shows/${showId}/book`, { tickets }).
      // {
      //   headers: {
      //     'Content-Type': 'application/json',
      //   },
      // }
      fetch(`http://127.0.0.1:3002/api/venues/${venueId}/shows/${showId}/book`,{
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ tickets }),
      }).
      then(response => {
        if (response.data && response.data.message === 'Booking successful') {
          this.fetchVenues(); // Update venue data after successful booking
          console.log('Booking successful:', response.data);
        } else {
          console.error('Booking failed:', response.data.error);
        }
      })
      .catch(error => {
        console.error('Error booking show:', error);
      });
  },
},
};
</script>
