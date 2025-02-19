<template>
    <div class="energy-input-container">
      <h2>Enter Energy Usage</h2>
      <form @submit.prevent="submitEnergyUsage">
        <div class="input-group">
          <label for="date">Date:</label>
          <input type="date" id="date" v-model="date" required />
        </div>
        <div class="input-group">
          <label for="energy">Energy Usage (kWh):</label>
          <input type="number" id="energy" v-model="energyUsage" required />
        </div>
        <button type="submit">Submit</button>
        <p v-if="successMessage" class="success">{{ successMessage }}</p>
        <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
      </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        date: '',
        energyUsage: '',
        successMessage: '',
        errorMessage: ''
      };
    },
    methods: {
      async submitEnergyUsage() {
        const userId = localStorage.getItem('user_id');
        if (!userId) {
          this.$router.push('/login');
          return;
        }
        try {
          await axios.post('http://localhost:5000/energy/add', {
            user_id: userId,
            energy_usage: this.energyUsage,
            timestamp: this.date
          });
          this.successMessage = 'Energy usage recorded successfully!';
          this.errorMessage = '';
          this.date = '';
          this.energyUsage = '';
        } catch (error) {
          this.successMessage = '';
          this.errorMessage = 'Failed to record energy usage. Please try again.';
        }
      }
    }
  };
  </script>
  
  <style scoped>
  .energy-input-container {
    max-width: 400px;
    margin: 0 auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 8px;
    box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
  }
  .input-group {
    margin-bottom: 15px;
  }
  label {
    display: block;
    margin-bottom: 5px;
  }
  input {
    width: 100%;
    padding: 8px;
    border: 1px solid #ccc;
    border-radius: 4px;
  }
  button {
    width: 100%;
    padding: 10px;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  button:hover {
    background-color: #0056b3;
  }
  .success {
    color: green;
    margin-top: 10px;
  }
  .error {
    color: red;
    margin-top: 10px;
  }
  </style>
  