<template>
    <div>
        <CakeChart />
        <BarChart />
		<PolarChart />
    </div>
</template>

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
