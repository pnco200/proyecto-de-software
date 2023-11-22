<template>
	<div>
		<cakeChart/>
		<barChart/>
	</div>
</template>
  
<script lang="js">
import cakeChart from '@/components/CakeChart.vue'
import barChart from '@/components/BarChart.vue'

export default {
	name: 'ChartView',
	components: {
		cakeChart,
		barChart
	}
}
</script>