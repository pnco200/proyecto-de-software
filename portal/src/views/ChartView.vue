<template>
    <div class="chart-container">
      <div class="chart-section">
        <h4>Cantidad de solicitudes por Instituto</h4>
        <CakeChart />
      </div>
      <div class="chart-section">
        <h4>Top 5 servicios mas solicitados</h4>
        <PolarChart />
      </div>
      <div class="chart-section">
        <h4>Top 5 instituciones con mejor tiempo de resolucion</h4>
        <BarChart />
      </div>
    </div>
  </template>
  
  <style>
  .chart-container {
    display: flex;
    flex-wrap: wrap;
  }
  
  .chart-section {
    flex: 1;
    margin: 10px;
    padding: 15px;
    border: 1px solid #ccc;
    border-radius: 5px;
    box-sizing: border-box;
    text-align: center;
  }

  </style>

<script lang="js">
import CakeChart from '@/components/CakeChart.vue'
import BarChart from '@/components/BarChart.vue'
import PolarChart from '@/components/PolarChart.vue'
export default {
    name: 'ChartView',
    components: {
        CakeChart,
        BarChart,
		PolarChart
    }
}
</script>
