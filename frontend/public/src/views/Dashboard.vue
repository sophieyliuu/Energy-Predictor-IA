<template>
    <div class="dashboard-container">
      <h2>Dashboard</h2>
      <p>Welcome to your energy usage dashboard.</p>
      <div class="dashboard-buttons">
        <router-link to="/energy-input" class="btn">Enter Energy Data</router-link>
        <router-link to="/predictions" class="btn">View Predictions</router-link>
        <router-link to="/graphs" class="btn">View Graphs</router-link>
        <router-link to="/profile" class="btn">Profile</router-link>
      </div>
      <div v-if="latestPrediction" class="latest-prediction">
        <h3>Latest Prediction</h3>
        <p><strong>Date:</strong> {{ latestPrediction.timestamp }}</p>
        <p><strong>Predicted Usage:</strong> {{ latestPrediction.predicted_usage }} kWh</p>
      </div>
      <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        latestPrediction: null,
        errorMessage: ''
      };
    },
    mounted() {
      this.fetchLatestPrediction();
    },
    methods: {
      async fetchLatestPrediction() {
        const userId = localStorage.getItem('user_id');
        if (!userId) {
          this.$router.push('/login');
          return;
        }
        try {
          const response = await axios.get(`http://localhost:5000/predict/get/${userId}`);
          if (response.data.length) {
            this.latestPrediction = response.data[response.data.length - 1];
          }
          this.errorMessage = '';
        } catch (error) {
          this.errorMessage = 'Failed to load latest prediction. Please try again.';
        }
      }
    }
  };
  </script>
  
  <style scoped>
  .dashboard-container {
    max-width: 600px;
    margin: 0 auto;
    padding: 20px;
    text-align: center;
  }
  .dashboard-buttons {
    margin-top: 20px;
  }
  .btn {
    display: inline-block;
    margin: 10px;
    padding: 12px 20px;
    background-color: #007bff;
    color: white;
    text-decoration: none;
    border-radius: 5px;
  }
  .btn:hover {
    background-color: #0056b3;
  }
  .latest-prediction {
    margin-top: 20px;
    padding: 15px;
    border: 1px solid #ddd;
    border-radius: 5px;
    background: #f9f9f9;
  }
  .error {
    color: red;
    margin-top: 10px;
  }
  </style>
  