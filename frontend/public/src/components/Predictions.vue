<template>
    <div class="predictions-container">
      <h2>Energy Usage Predictions</h2>
      <button @click="fetchPredictions">Load Predictions</button>
      <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
      <div v-if="predictions.length" class="predictions-list">
        <div v-for="prediction in predictions" :key="prediction.id" class="prediction-item">
          <p><strong>Date:</strong> {{ prediction.timestamp }}</p>
          <p><strong>Predicted Usage:</strong> {{ prediction.predicted_usage }} kWh</p>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        predictions: [],
        errorMessage: ''
      };
    },
    methods: {
      async fetchPredictions() {
        const userId = localStorage.getItem('user_id');
        if (!userId) {
          this.$router.push('/login');
          return;
        }
        try {
          const response = await axios.get(`http://localhost:5000/predict/get/${userId}`);
          this.predictions = response.data;
          this.errorMessage = '';
        } catch (error) {
          this.errorMessage = 'Failed to load predictions. Please try again.';
        }
      }
    }
  };
  </script>
  
  <style scoped>
  .predictions-container {
    max-width: 500px;
    margin: 0 auto;
    padding: 20px;
    text-align: center;
  }
  button {
    padding: 10px 15px;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    margin-bottom: 20px;
  }
  button:hover {
    background-color: #0056b3;
  }
  .predictions-list {
    margin-top: 20px;
  }
  .prediction-item {
    padding: 10px;
    border: 1px solid #ddd;
    margin-bottom: 10px;
    border-radius: 5px;
    background: #f9f9f9;
  }
  .error {
    color: red;
    margin-top: 10px;
  }
  </style>
  