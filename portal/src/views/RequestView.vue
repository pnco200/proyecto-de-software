<template>
  <div class="solicitar-servicio">
    <h2 align="center">Solicitar Servicio {{ $route.params.serviceId}}</h2>

    <!-- Condicionalmente mostrar el componente RequestForm o RequestCompleteInfo -->
    <RequestForm
      v-if="!solicitudEnviada"
      :serviceId="$route.params.serviceId"
      @submitRequest="submitRequestToApi"
    />
    <RequestCompleteInfo
      v-else
      :solicitud="solicitudObtenida"
    />

    <!-- Notificación flotante -->
    <Notification
      v-if="showNotification"
      :message="notificationMessage"
      @close="showNotification = false"
    />
  </div>
</template>

<script>
import RequestForm from '@/components/RequestForm.vue';
import RequestCompleteInfo from '@/components/RequestCompleteInfo.vue';
import Notification from '@/components/Notification.vue';
import axios from 'axios';
import Cookies from 'js-cookie';

export default {
  components: {
    RequestForm,
    RequestCompleteInfo,
    Notification,
  },
  data() {
    return {
      solicitudEnviada: false,
      solicitudObtenida: null,
      showNotification: false,
      notificationMessage: '',
    };
  },
  methods: {
    async submitRequestToApi(requestData) {
      const jwtToken = Cookies.get('token');

      if (jwtToken) {
        try {
          const formData = {
            service_id: requestData.serviceId,
            description: requestData.description,
          };

          if (requestData.files) {
            formData["file"] = requestData.files;
          } else {
            formData["file"] = null;
          }

          const response = await axios.post(
            'http://localhost:5000/api/me/created-request',
            formData,
            {
              headers: {
                'Content-Type': 'application/json',
                Authorization: `Bearer ${jwtToken}`,
              },
            }
          );

          this.solicitudObtenida = response.data;
          this.solicitudEnviada = true;

          this.showNotification = true;
          this.notificationMessage = 'Solicitud enviada con éxito';

          console.log('Solicitud enviada con éxito:', response.data);
        } catch (error) {
          console.error('Error al enviar la solicitud:', error.message);

          // Mostrar el mensaje de error proveniente de la respuesta del servidor
          this.showNotification = true;
          this.notificationMessage = error.response.data.message || 'Error al enviar la solicitud';
        }
      } else {
        console.error('No se encontró un token en las cookies.');
      }
    },
  },
};
</script>

<style scoped>
/* Estilos específicos de la vista */
.solicitar-servicio {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background-color: #e0f7e9; /* Color celeste azulado muy claro */
}

/* Estilos específicos de los componentes */
.RequestForm,
.RequestCompleteInfo,
.Notification {
  background-color: #ccf5d1; /* Tonalidad de celeste azulado para los componentes */
  padding: 20px;
  margin: 10px;
  border-radius: 8px;
}

h2 {
  color: #007BFF; /* Azul */
  text-align: center;
}
</style>
