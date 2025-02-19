<template>
    <div class="home-container">
      <h1>Welcome to Energy Usage Predictor</h1>
      <p>Manage and predict your energy consumption efficiently.</p>
      <div class="buttons">
        <router-link to="/energy-input" class="btn">Enter Energy Data</router-link>
        <router-link to="/predictions" class="btn">View Predictions</router-link>
        <router-link to="/profile" class="btn">Profile</router-link>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    mounted() {
      const userId = localStorage.getItem('user_id');
      if (!userId) {
        this.$router.push('/login');
      }
    }
  };
  </script>
  
  <style scoped>
  .home-container {
    text-align: center;
    padding: 40px;
  }
  .buttons {
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
  </style>
  