<template>
    <div class="settings-container">
      <h2>Settings</h2>
      <p>Manage your account and preferences.</p>
      <div class="input-group">
        <label for="name">Update Name:</label>
        <input type="text" id="name" v-model="updatedName" />
      </div>
      <div class="input-group">
        <label for="email">Update Email:</label>
        <input type="email" id="email" v-model="updatedEmail" />
      </div>
      <button @click="updateProfile">Save Changes</button>
      <p v-if="successMessage" class="success">{{ successMessage }}</p>
      <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        updatedName: '',
        updatedEmail: '',
        successMessage: '',
        errorMessage: ''
      };
    },
    mounted() {
      this.fetchUserProfile();
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
          this.updatedName = response.data.name;
          this.updatedEmail = response.data.email;
          this.errorMessage = '';
        } catch (error) {
          this.errorMessage = 'Failed to load user profile.';
        }
      },
      async updateProfile() {
        const userId = localStorage.getItem('user_id');
        if (!userId) return;
        try {
          await axios.put(`http://localhost:5000/auth/user/${userId}`, {
            name: this.updatedName,
            email: this.updatedEmail
          });
          this.successMessage = 'Profile updated successfully!';
          this.errorMessage = '';
        } catch (error) {
          this.successMessage = '';
          this.errorMessage = 'Failed to update profile. Please try again.';
        }
      }
    }
  };
  </script>
  
  <style scoped>
  .settings-container {
    max-width: 500px;
    margin: 0 auto;
    padding: 20px;
    text-align: center;
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
    margin-top: 15px;
    padding: 10px 15px;
    background-color: #28a745;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }
  button:hover {
    background-color: #218838;
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
  