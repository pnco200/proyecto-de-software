<template>
    <DoughnutChart :chartData="testData" />
</template>

<script lang="js">
import { defineComponent, onMounted, ref } from 'vue'
import { DoughnutChart } from 'vue-chart-3'
import { Chart, registerables } from 'chart.js'
import axios from 'axios'

Chart.register(...registerables)

const fetchData = async () => {
    try {
        const response = await axios.get('http://localhost:5000/api/stats/requests-institutions')
        const data = response.data
        console.log(data)
        return processResponse(data)
    } catch (error) {
        console.error('Error fetching or processing data:', error)
        // Handle error or return a default value
        return { labels: [], datasets: [] }
    }
}

const processResponse = (data) => {
    const labels = data.map((item) => item.Institucion)
    const values = data.map((item) => item.Solicitudes)

    return {
        labels,
        datasets: [
            {
                data: values,
                backgroundColor: ['#77CEFF', '#0079AF', '#123E6B', '#97B0C4', '#A5C8ED']
            }
        ]
    }
}

export default defineComponent({
    name: 'cakeChart',
    components: { DoughnutChart },

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
