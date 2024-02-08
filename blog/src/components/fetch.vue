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
      venuesList: [], // Add this array to store the fetched venues
    };
  },
  methods: {
    addVenue() {
      // ... existing code to add a venue ...

      // Fetch the updated list of venues after adding a new one
      this.fetchVenuesList();
    },
    fetchVenuesList() {
      fetch('/api/getVenuess')
        .then((response) => response.json())
        .then((data) => {
          this.venuesList = data;
        })
        .catch((error) => console.error('Error fetching venues:', error));
    },
  },
  mounted() {
    // Fetch the initial list of venues when the component is mounted
    this.fetchVenuesList();
  },
};
</script>
