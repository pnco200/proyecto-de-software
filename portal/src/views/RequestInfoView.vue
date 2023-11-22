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
  import Cookies from 'js-cookie'
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
      const jwtToken = Cookies.get('token')
      if (jwtToken) {
        // Configurar el encabezado de autorización con el token JWT  
      try {
        const response = await axios.get(`http://localhost:5000/api/me/requests/${requestId}`, {
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${jwtToken}`,
          },
        });
  
        this.solicitudDetails = response.data;
      } catch (error) {
        console.error('Error al obtener detalles de la solicitud:', error.message);
        this.showNotification = true;
        this.notificationMessage = 'Error al obtener detalles de la solicitud';
      }
    }else{
      console.error('No se encontró un token en las cookies.');
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
  