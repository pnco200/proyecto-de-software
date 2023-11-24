<template>
    <PolarAreaChart :chartData="testData" />
</template>

<script lang="js">
import { defineComponent, onMounted, ref } from 'vue'
import { PolarAreaChart } from 'vue-chart-3'
import { Chart, registerables } from 'chart.js'
import axios from 'axios'

Chart.register(...registerables)

const fetchData = async () => {
    try {
        const response = await axios.get('https://admin-grupo25.proyecto2023.linti.unlp.edu.ar/api/stats/most-requested-services')
        const data = response.data
        console.log(data)
        return processResponse(data)
    } catch (error) {
        alert('Error al traer la informacion:', error)
        return { labels: [], datasets: [] }
    }
}

const processResponse = (data) => {
    const chartData = {
        labels: [],
        datasets: [
            {
                label: 'Solicitudes',
                data: [],
                backgroundColor: []
            }
        ]
    }

    const colorPalette = [
        'rgba(255, 99, 132, 0.7)',
        'rgba(54, 162, 235, 0.7)',
        'rgba(255, 206, 86, 0.7)',
        'rgba(75, 192, 192, 0.7)',
        'rgba(153, 102, 255, 0.7)'
    ]

    data.forEach((item, index) => {
        chartData.labels.push(item.Servicio + ' - ' + item.Institucion)
        chartData.datasets[0].data.push(item.Solicitudes)
        chartData.datasets[0].backgroundColor.push(colorPalette[index % colorPalette.length])
    })

    return chartData
}

export default defineComponent({
    name: 'polarAreaChart',
    components: { PolarAreaChart },

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
    }
})
</script>
