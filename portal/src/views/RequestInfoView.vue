<template>
    <div>
      <h2>Detalles de Solicitud</h2>
      <RequestCompleteInfo :solicitud="solicitudDetails" />
      <Notification v-if="showNotification" :message="notificationMessage" @close="handleNotificationClose" />
    </div>
  </template>
  
  <script>
  import RequestCompleteInfo from '@/components/RequestCompleteInfo.vue';
  import Notification from '@/components/Notification.vue';
  import axios from 'axios';
  
  export default {
    data() {
      return {
        solicitudDetails: null,
        showNotification: false,
        notificationMessage: '',
      };
    },
    async created() {
      const requestId = this.$route.params.requestId;
  
      try {
        const response = await axios.get(`http://localhost:5000/api/me/requests/${requestId}`, {
          headers: {
            'Content-Type': 'application/json',
            'Authorization': 'JWT <token>',
          },
        });
  
        this.solicitudDetails = response.data;
      } catch (error) {
        console.error('Error al obtener detalles de la solicitud:', error.message);
        this.showNotification = true;
        this.notificationMessage = 'Error al obtener detalles de la solicitud';
      }
    },
    methods: {
      handleNotificationClose() {
        if (this.showNotification) {
          this.showNotification = false;
          this.$router.push('/home');
        }
      },
    },
    components: {
      RequestCompleteInfo,
      Notification,
    },
  };
  </script>
  
  <style>
  /* Agrega estilos específicos de la vista si es necesario */
  </style>
  