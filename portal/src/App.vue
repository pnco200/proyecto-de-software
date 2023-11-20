<template>
    <NavBar />
    <router-view />
</template>

<script lang="js">
import { defineComponent } from 'vue'

import NavBar from '@/components/NavBar.vue';

export default defineComponent({
  name: 'HomeView',
  components: { NavBar },
  
})
</script>
