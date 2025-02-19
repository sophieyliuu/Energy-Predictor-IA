<template>
    <div class="graphs-container">
      <h2>Energy Usage Graphs</h2>
      <button @click="fetchGraphData">Load Graph</button>
      <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
      <canvas v-if="graphData.length" ref="chartCanvas"></canvas>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  import Chart from 'chart.js/auto';
  
  export default {
    data() {
      return {
        graphData: [],
        errorMessage: '',
        chart: null
      };
    },
    methods: {
      async fetchGraphData() {
        const userId = localStorage.getItem('user_id');
        if (!userId) {
          this.$router.push('/login');
          return;
        }
        try {
          const response = await axios.get(`http://localhost:5000/energy/get/${userId}`);
          this.graphData = response.data;
          this.errorMessage = '';
          this.renderChart();
        } catch (error) {
          this.errorMessage = 'Failed to load graph data. Please try again.';
        }
      },
      renderChart() {
        if (this.chart) {
          this.chart.destroy();
        }
        const ctx = this.$refs.chartCanvas.getContext('2d');
        this.chart = new Chart(ctx, {
          type: 'line',
          data: {
            labels: this.graphData.map(data => data.timestamp),
            datasets: [{
              label: 'Energy Usage (kWh)',
              data: this.graphData.map(data => data.energy_usage),
              borderColor: '#007bff',
              fill: false
            }]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false
          }
        });
      }
    }
  };
  </script>
  
  <style scoped>
  .graphs-container {
    max-width: 600px;
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
  canvas {
    width: 100%;
    height: 400px;
  }
  .error {
    color: red;
    margin-top: 10px;
  }
  </style>
  