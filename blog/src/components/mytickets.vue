<template>
    <div class="my-tickets">
      <h2>My Tickets</h2>
      <div v-if="bookedShows.length === 0">
        <p>No shows booked.</p>
      </div>
      <div v-else>
        <div v-for="(show, index) in bookedShows" :key="index" class="ticket">
          <h3>{{ show.name }}</h3>
          <p>Venue: {{ show.venueName }}</p>
          <p>Tickets booked: {{ show.ticketsBooked }}</p>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'MyTicketsPage',
    data() {
      return {
        bookedShows: [] // Store the booked shows here
      };
    },
    mounted() {
      // Fetch booked shows from the API and update the bookedShows array
      this.fetchBookedShows();
    },
    methods: {
      async fetchBookedShows() {
        try {
          const response = await fetch('http://localhost:3002/api/getVenuess');
          const data = await response.json();
          const bookedShows = [];
  
          data.forEach(venueArray => {
            // Loop through the inner shows array if it exists
            if (venueArray.length > 5) {
              const showsArray = venueArray[5];
              showsArray.forEach(show => {
                if (show.count > 0) {
                  bookedShows.push({
                    id: show.id,
                    name: show.name,
                    venueName: venueArray[1], // Use venue name from outer array
                    ticketsBooked: show.count
                  });
                }
              });
            }
          });
  
          this.bookedShows = bookedShows;
        } catch (error) {
          console.error('Error fetching booked shows:', error);
        }
      }
    }
  };
  </script>
  
  <style>
  /* Your component styles */
  </style>
  