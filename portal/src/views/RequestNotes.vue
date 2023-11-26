<template>
  <div>
    <h2>Chat con Operador</h2>
    <h3>Notas o Mensajes con Operador del Servicio{{ this.id }}</h3>

    <!-- Chat Messages -->
    <p>{{ this.messages }}</p>
    <div v-for="message in messages" :key="message.id" >
      {{ message.msg_content }}
    </div>

    <!-- Aquí puedes agregar un formulario o componente para enviar nuevos mensajes si es necesario -->
  </div>
</template>

<script>
import axios from 'axios';
import Cookies from 'js-cookie';

export default {
  props: {
    solicitud: Object,
  },
  data() {
    return {
      messages: [], // La lista de mensajes que obtienes de la API
      id: null,
    };
  },
  created() {
    // Llama a la API para obtener mensajes asociados a la solicitud
    this.fetchMessages();
  },
  methods: {
    async fetchMessages() {
      const jwtToken = Cookies.get('token');
      if (jwtToken) {
        try {
          // Utiliza this.solicitud.id para enviar el ID de la solicitud a la API
          const response = await axios.get(`http://localhost:5000/api/me/request/${this.$route.params.requestId}/notes`, {
            headers: {
              'Content-Type': 'application/json',
              'Authorization': `Bearer ${jwtToken}`,
            },
          });
            
          this.messages = response.data;
          this.id = response.id; // Corregido para asignar solicitud.id
        } catch (error) {
          console.error('Error al obtener mensajes:', error);
        }
      } else {
        console.log('No hay token JWT para utilizar');
      }
    },
    isMyMessage(message) {
      // Verifica si el mensaje es del usuario que hizo la solicitud
      return message.user_id === this.id;
    },
  },
};
</script>

<style>
.my-message {
  text-align: right; /* Alinea los mensajes del usuario a la derecha */
  background-color: #DCF8C6; /* Cambia el color de fondo de los mensajes del usuario si es necesario */
}
</style>
