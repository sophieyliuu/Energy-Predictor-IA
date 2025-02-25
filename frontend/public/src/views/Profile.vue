<template>
    <div class="profile-container">
      <h2>User Profile</h2>
      <p><strong>Name:</strong> {{ user.name }}</p>
      <p><strong>Email:</strong> {{ user.email }}</p>
      <button @click="logout">Logout</button>
      <h3>Past Energy Logs</h3>
      <ul v-if="energyLogs.length">
        <li v-for="log in energyLogs" :key="log.id">
          <p><strong>Date:</strong> {{ log.timestamp }}</p>
          <p><strong>Energy Usage:</strong> {{ log.energy_usage }} kWh</p>
        </li>
      </ul>
      <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        user: {
          name: '',
          email: ''
        },
        energyLogs: [],
        errorMessage: ''
      };
    },
    mounted() {
      this.fetchUserProfile();
      this.fetchEnergyLogs();
    },
    methods: {
      async fetchUserProfile() {
        const userId = localStorage.getItem('user_id');
        if (!userId) {
          this.$router.push('/login');
          return;
        }
        try {
          const response = await axios.get(`http://localhost:5000/auth/user/${userId}`);
          this.user = response.data;
          this.errorMessage = '';
        } catch (error) {
          this.errorMessage = 'Failed to load user profile.';
        }
      },
      async fetchEnergyLogs() {
        const userId = localStorage.getItem('user_id');
        if (!userId) return;
        try {
          const response = await axios.get(`http://localhost:5000/energy/get/${userId}`);
          this.energyLogs = response.data;
          this.errorMessage = '';
        } catch (error) {
          this.errorMessage = 'Failed to load energy logs.';
        }
      },
      logout() {
        localStorage.removeItem('user_id');
        this.$router.push('/login');
      }
    }
  };
  </script>
  
  <style scoped>
  .profile-container {
    max-width: 600px;
    margin: 0 auto;
    padding: 20px;
    text-align: center;
  }
  button {
    margin-top: 15px;
    padding: 10px 15px;
    background-color: #dc3545;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }
  button:hover {
    background-color: #c82333;
  }
  ul {
    list-style-type: none;
    padding: 0;
  }
  li {
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
  