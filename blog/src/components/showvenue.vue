<template>
    <div>
      <h1>All Shows with Venues</h1>
      <ul>
        <li v-for="show in shows" :key="show.id">
          <h2>{{ show.name }}</h2>
          <p>Venue: {{ show.venue.name }}</p>
          <p>Location: {{ show.venue.location }}, {{ show.venue.city }}</p>
          <p>Rating: {{ show.rating }}</p>
          <p>Timing: {{ show.timing }}</p>
          <p>Price: {{ show.price }}</p>
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'ShowVenue',
    data() {
      return {
        shows: [],
      };
    },
    mounted() {
      this.fetchShowsWithVenues();
    },
    methods: {
      fetchShowsWithVenues() {
        axios
          .get('http://localhost:3002/api/getShowsWithVenues')
          .then(response => {
            this.shows = response.data;
          })
          .catch(error => {
            console.error('Error fetching shows with venues:', error);
          });
      },
    },
  };
  </script>
  