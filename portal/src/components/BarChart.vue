<template>
    <BarChart :chartData="testData" />
  </template>
  
  <script lang="js">
  import { defineComponent, onMounted, ref } from 'vue'
  import { BarChart } from 'vue-chart-3'
  import { Chart, registerables } from 'chart.js'
  import axios from 'axios'
  
  Chart.register(...registerables)
  
  const fetchData = async () => {
    try {
      const response = await axios.get('https://admin-grupo25.proyecto2023.linti.unlp.edu.ar/api/stats/efficient-institutions')
      const data = response.data
      return processResponse(data)
    } catch (error) {
      alert('Error al traer la informacion:', error)
      return { labels: [], datasets: [] }
    }
  }
  
  const processResponse = (data) => {
  const sortedData = data.sort((a, b) => a.TiempoTotalSecs - b.TiempoTotalSecs)

  const labels = sortedData.map((item) => `${item.Institucion} - ${item.TiempoEnDias} dias`)
  const values = sortedData.map((item) => item.TiempoTotalSecs)

  return {
    labels,
    datasets: [
      {
        label: 'Tiempo Total (secs)',
        data: values,
        backgroundColor: ['#77CEFF', '#0079AF', '#123E6B', '#97B0C4', '#A5C8ED'],
      },
    ],
  }
}

export default defineComponent({
  name: 'barChart',
  components: { BarChart },

  setup() {
    const testData = ref(null)

    onMounted(async () => {
      try {
        const processedData = await fetchData()
        testData.value = processedData
      } catch (error) {
        console.error('Error fetching or processing data:', error)
      }
    })

    return { testData }
  },
})
  </script>