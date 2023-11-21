<!-- src/components/SolicitudesListComponent.vue -->

<template>
    <div>
      <h2>Listado de Solicitudes de Servicio</h2>
  
      <ul v-if="solicitudes.length">
        <ListItemComponent
          v-for="solicitud in solicitudes"
          :key="solicitud.id"
          :solicitud="solicitud"
          @detailsClick="handleDetailsClick"
        />
        <!--Aca le pasa la info al componente-->
      </ul>
  
      <p v-else>No hay solicitudes de servicio.</p>
    </div>
  </template>
  
  <script>
  import ListItemComponent from '@/components/RequestListElement.vue'; // Ajusta la ruta según tu estructura de archivos
  import axios from 'axios'
  export default {
    data() {
      return {
        solicitudes: [],
      };
    },
    mounted() {
      this.fetchSolicitudes();
    },
    methods: {
      async fetchSolicitudes() {
        try {
          const response = await axios.get('https://admin-grupo25.proyecto2023.unlp.edu.ar/api/me/requests', {
            params: {
              page: 1,
              per_page: 10,
              sort: 'creation_date',
              order: 'desc',
            },
            headers: {
              'Content-Type': 'application/json',
              'Authorization': 'JWT <token>',
            },
          });
  
          this.solicitudes = response.data;
        } catch (error) {
          console.error('Error al obtener las solicitudes:', error.message);
        }
      },
      handleDetailsClick(solicitud) {
        console.log('Detalles de la solicitud:', solicitud);
        // Aquí puedes realizar acciones adicionales al hacer clic en el botón "Detalles"
      },
    },
    components: {
      ListItemComponent,
    },
  };
  </script>
  
  <style>
  /* Estilos específicos de la lista si es necesario */
  </style>
  