<template>
  <div class="chart-container">
    <div class="chart-section">
      <h4>Cantidad de solicitudes por Institución</h4>
      <CakeChart />
    </div>
    <div class="chart-section">
      <h4>Top 5 servicios más solicitados</h4>
      <PolarChart />
    </div>
    <div class="chart-section">
      <h4>Top 5 instituciones con mejor tiempo de resolución</h4>
      <BarChart />
    </div>
  </div>
</template>

<style>
.chart-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around; 
}

.chart-section {
  flex: 1;
  margin: 10px;
  padding: 15px;
  border: 1px solid #ccc;
  border-radius: 5px;
  box-sizing: border-box;
  text-align: center;
  min-width: 300px; 
}

@media screen and (max-width: 768px) {
  .chart-section {
    flex-basis: 100%;
  }
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
    PolarChart,
  },
};
</script>