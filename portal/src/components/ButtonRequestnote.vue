<!-- src/components/ButtonComponent.vue -->
<!-- Componente boton que llama a la vista que muestra con otro componente la informacion completa de la solicitud-->
<template>
    <router-link :to="{ name: 'info-request', params: { requestId: solicitud.id } }">
      <button>Detalles</button>
    </router-link>
  </template>
  
  <script>
  export default {
    props: {
      solicitud: Object,
    },
  };
  </script>
  
  <style scoped>
  /* Estilos específicos del botón si es necesario */
  </style>
  