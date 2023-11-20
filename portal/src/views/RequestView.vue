<template>
  <div>
    <h2>Solicitar Servicio</h2>

    <!-- Condicionalmente mostrar el componente RequestForm o RequestCompleteInfo -->
    <RequestForm v-if="modoSolicitud && !solicitudEnviada" @submitRequest="submitRequestToApi" />
    <RequestCompleteInfo v-else :solicitud="solicitudObtenida" />

    <!-- Notificación flotante -->
    <Notification v-if="showNotification" :message="notificationMessage" @close="showNotification = false" />

    <!-- Botón para solicitar otro servicio -->
    <button v-if="solicitudEnviada" @click="resetSolicitud">
      Solicitar Otro Servicio
    </button>
  </div>
</template>

<script>
import RequestForm from '@/components/RequestForm.vue';
import RequestCompleteInfo from '@/components/RequestCompleteInfo.vue';
import Notification from '@/components/Notification.vue';
import axios from 'axios';

export default {
  components: {
    RequestForm,
    RequestCompleteInfo,
    Notification,
  },
  data() {
    return {
      solicitudEnviada: JSON.parse(localStorage.getItem('solicitudEnviada')) || false,
      solicitudObtenida: JSON.parse(localStorage.getItem('solicitudObtenida')) || null,
      modoSolicitud: JSON.parse(localStorage.getItem('modoSolicitud')) || true,
      showNotification: false,
      notificationMessage: '',
    };
  },
  methods: {
    async submitRequestToApi(requestData) {
      try {
        const formData = new FormData();
        formData.append('serviceId', requestData.serviceId);
        formData.append('description', requestData.description);

        if (requestData.files) {
          for (let i = 0; i < requestData.files.length; i++) {
            formData.append('files', requestData.files[i]);
          }
        }

        const response = await axios.post('https://admin-grupo25.proyecto2023.linti.unlp.edu.ar/api/me/requests/', formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
            'Authorization': `JWT ${333}`,
          },
        });

        this.solicitudObtenida = response.data;
        this.solicitudEnviada = true;

        // Configura la notificación para mostrar un mensaje de éxito
        this.showNotification = true;
        this.notificationMessage = 'Solicitud enviada con éxito';

        // Almacena el estado en el localStorage
        localStorage.setItem('solicitudEnviada', JSON.stringify(this.solicitudEnviada));
        localStorage.setItem('solicitudObtenida', JSON.stringify(this.solicitudObtenida));
        localStorage.setItem('modoSolicitud', JSON.stringify(this.modoSolicitud));

        console.log('Solicitud enviada con éxito:', response.data);
      } catch (error) {
        console.error('Error al enviar la solicitud:', error.message);

        // Configura la notificación para mostrar un mensaje de error
        this.showNotification = true;
        this.notificationMessage = 'Error al enviar la solicitud';
      }
    },
    resetSolicitud() {
      this.solicitudEnviada = false;
      this.modoSolicitud = true;
      this.showNotification = false;

      // Almacena el estado en el localStorage
      localStorage.setItem('solicitudEnviada', JSON.stringify(this.solicitudEnviada));
      localStorage.setItem('modoSolicitud', JSON.stringify(this.modoSolicitud));
    },
  },
};
</script>


/* Estilos específicos de la vista */
<style >
/* Estilos específicos de la vista */
.solicitar-servicio {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background-color: #e0f7e9; /* Color verde muy claro */
}

/* Estilos específicos de los componentes */
.RequestForm, .RequestCompleteInfo, .Notification {
  background-color: #ccf5d1; /* Tonalidad de verde para los componentes */
  padding: 20px;
  margin: 10px;
  border-radius: 8px;
}

/* Estilos para el botón */
button {
  background-color: #4caf50; /* Verde más oscuro para el botón */
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
</style>
