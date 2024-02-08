<template>
  <div>
    <h1>Update Show</h1>
    <form @submit.prevent="updateShow">
      <div>
        <label for="name">Name:</label>
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
      <button type="submit">Update Show</button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'UpdateShow',
  data() {
    return {
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
    // Fetch the show data to update from the backend API
    const showId = this.$route.params.showId; // Assuming a route parameter for the show ID
    fetch(`http://127.0.0.1:3002/api/updateshow/${showId}`)
      .then(response => response.json())
      .then(data => {
        this.show = data;
      })
      .catch(error => {
        console.error('Error fetching show data:', error);
      });
  },
  methods: {
    updateShow() {
      fetch(`/api/updateshow/${this.$route.params.showId}`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(this.show),
      })
        .then(response => response.json())
        .then(data => {
          console.log(data.message);
          // Optionally, show a success message or navigate back to the show list
          this.$router.push({ name: 'ShowList' }); // Adjust route name accordingly
        })
        .catch(error => {
          console.error('Error updating show:', error);
        });
    },
  },
};
</script>
