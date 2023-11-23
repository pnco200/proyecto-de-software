<!-- src/components/ButtonComponent.vue -->
<template>
    <router-link :to="{ name: 'request', params: { serviceId: id } }">
    <button>Solicitar servicio id </button>
  </router-link>
  </template>
  
  <script>
  export default {
    props: {
      id: {
        type: Number, // Cambiado a Number
        required: true,
      },
    },
  };
  </script>
  
  <style scoped>
  /* Estilos específicos del botón si es necesario */
  </style>
  