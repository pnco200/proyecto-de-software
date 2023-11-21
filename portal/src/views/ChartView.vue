<template>
    <div>
      <testComponent />
    </div>
  </template>
  
  <script>
  import testComponent from '@/components/BarChart.vue'
  
  export default {
    name: 'ChartView',
    components: {
      testComponent
    }
  }
  </script>