<template>
    <DoughnutChart :chartData="testData" />
</template>

<script lang="js">
import { defineComponent, onMounted, ref } from 'vue';
import { DoughnutChart } from 'vue-chart-3';
import { Chart, registerables } from 'chart.js';


Chart.register(...registerables);

const fetchData = async () => {
    try {
        const response = await fetch('http://localhost:5000/api/stats/requests-institutions');
        const data = await response.json();
		console.log(data);
        testData.value = processResponse(data.labels, data.values);
    } catch (error) {
        console.error('Error fetching or processing data:', error);
    }
};

const processResponse = (labels, values) => {
    return {
        labels,
        datasets: [
            {
                data: values,
                backgroundColor: ['#77CEFF', '#0079AF', '#123E6B', '#97B0C4', '#A5C8ED'],
            },
        ],
    };
};

export default defineComponent({
    name: 'testComponent',
    components: { DoughnutChart },

    setup() {
        const testData = ref(null);

        onMounted(async () => {
            try {
                const response = await fetchData();
                testData.value = processResponse(response);
            } catch (error) {
                console.error('Error fetching or processing data:', error);
            }
        });

        return { testData };
    },
});
</script>
