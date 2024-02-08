<template>
  <div>
    <h1>{{ venue.name }}</h1>
    <p>Location: {{ venue.location }}, {{ venue.city }}</p>
    <h2>Available Shows:</h2>
    <ul>
      <li v-for="show in venue.shows" :key="show.id">
        {{ show.name }} (Rating: {{ show.rating }}) - {{ show.timing }} - Price: {{ show.price }}
        <button @click="bookShow(venue.id, show.id)">Book</button>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'VenueDetail',
  props: ['venue'],
  methods: {
  bookShow(venueId, showId) {  // Removed the 'tickets' parameter
    // Prompt the user to enter the number of tickets
    const tickets = prompt('Enter the number of tickets:');
    
    // Ensure the tickets value is a positive integer
    if (!tickets || isNaN(tickets) || parseInt(tickets) <= 0) {
      console.error('Invalid number of tickets');
      return;
    }

    // Convert tickets to an integer
    const parsedTickets = parseInt(tickets, 10);

    // Send the booking request
    console.log(venueId, showId, parsedTickets,axios)
    fetch(`http://127.0.0.1:3002/api/venues/${venueId}/shows/${showId}/book`,{
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ tickets: parsedTickets }),
      })
      .then(response => {
        if (response.data && response.data.message === 'Booking successful') {
          // You may want to update the venue data here
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
