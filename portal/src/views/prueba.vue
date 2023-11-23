<template>
    <div>
      <h2 align="center">Vista de Solicitud de Servicio</h2>
  
      <!-- Input para ingresar el valor de serviceId -->
      <label for="serviceIdInput">Ingrese el valor de serviceId:</label>
      <input type="number" v-model="serviceIdFromInput" id="serviceIdInput" />
  
      <!-- Componente de botón -->
      <ButtonMakeRequest :id="serviceIdFromInput" />
  
      <!-- Otras partes de tu vista si las hay -->
    </div>
  </template>
  
  <script>
  import ButtonMakeRequest from '@/components/ButtonMakeRequest.vue'; // Ajusta la ruta según tu estructura de carpetas
  
  export default {
    components: {
      ButtonMakeRequest,
    },
    data() {
      return {
        serviceIdFromInput: 1, // Valor inicial del input
      };
    },
    // Puedes agregar métodos o lógica adicional según sea necesario
  };
  </script>
  
  <style>
  /* Estilos específicos de la vista si es necesario */
  </style>
  