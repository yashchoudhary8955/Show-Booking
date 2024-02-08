<template>
    <div>
      <h2>Theater CSV Export</h2>
      <button @click="exportCSV">Export CSV</button>
      <p>{{ exportMessage }}</p>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        exportMessage: '',
      };
    },
    methods: {
      exportCSV() {
        const venueId = 1; // Set the venue ID you want to export CSV for
        this.exportMessage = 'Export initiated...';
  
        // Call the API endpoint to trigger CSV export
        fetch(`http://localhost:3002/api/exportTheaterCSV/${venueId}`)
          .then(response => response.json())
          .then(data => {
            this.exportMessage = data.message;
          })
          .catch(error => {
            console.error('Error:', error);
            this.exportMessage = 'Error initiating export.';
          });
      },
    },
  };
  </script>
  
  <style scoped>
  /* Add your component styles here */
  </style>
  