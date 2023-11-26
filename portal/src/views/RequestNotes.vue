<template>
  <div>
    <h2 align="center">Chat con Operador</h2>
    <h3 align="center">Notas o Mensajes con Operador del Servicio</h3>
    
    <!-- Chat Messages -->
    <div class="chat-container">
      <div v-for="message in messages" :key="message.id" :class="{ 'my-message': isMyMessage(message) }">
        <div class="message-container">
          <div class="message-content">{{ message.content }}</div>
          <div class="message-time"><p>{{message.creation_date }}</p></div>
        </div>
      </div>
    </div>

    <!-- Message Input Form -->
    <div class="message-input-container">
      <input v-model="newMessage" placeholder="Escribe un mensaje..." />
      <button @click="sendMessage">Enviar</button>
    </div>
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
      newMessage: '', // Nuevo mensaje que el usuario está escribiendo
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

          // Verifica si la respuesta tiene datos antes de asignarlos
          this.messages = response.data.data;
          this.id = response.data.id; // Corregido para asignar solicitud.id
          
        } catch (error) {
          alert(error);
          console.error('Error al obtener mensajes:', error);
        }
      } else {
        alert('Debe iniciar sesión');
        console.log('No hay token JWT para utilizar');
      }
    },
    isMyMessage(message) {
      // Verifica si el mensaje es del usuario que hizo la solicitud
      return message.user_id === this.id;
    },
    formatTime(time) {
      // Formatea la hora del mensaje como desees
      const messageTime = new Date(time);
      return `${messageTime.getHours()}:${messageTime.getMinutes()}`;
    },
    async sendMessage() {
      if (this.newMessage.trim() !== '') {
        // Enviar el nuevo mensaje a la API
        const jwtToken = Cookies.get('token');
        if (jwtToken) {
          try {
            // Primero, enviar el mensaje a la segunda API
            await axios.post(
              `http://localhost:5000/api/me/requests/${this.$route.params.requestId}/add-notes`,
              {
                text: this.newMessage,
              },
              {
                headers: {
                  'Content-Type': 'application/json',
                  'Authorization': `Bearer ${jwtToken}`,
                },
              }
            );

            // Luego, actualizar la lista de mensajes haciendo una llamada a la primera API
            await this.fetchMessages();

            // Limpiar el campo del nuevo mensaje
            this.newMessage = '';
          } catch (error) {
            alert('Error al enviar el mensaje');
            console.error('Error al enviar el mensaje:', error);
          }
        } else {
          alert('Debe iniciar sesión');
          console.log('No hay token JWT para utilizar');
        }
      }
    },
  },
};
</script>

<style>
.chat-container {
  max-width: 400px;
  margin: 20px auto;
}

.my-message {
  text-align: right;
}

.message-container {
  background-color: #dcf8c6;
  border-radius: 10px;
  padding: 8px;
  margin: 5px;
}

.message-content {
  display: inline-block;
  max-width: 80%;
  word-wrap: break-word;
}

.message-time {
  font-size: 12px;
  color: #888;
}

.message-input-container {
  display: flex;
  margin-top: 20px;
}

.message-input-container input {
  flex: 1;
  padding: 10px;
}

.message-input-container button {
  padding: 10px;
  background-color: #25d366;
  color: #fff;
  border: none;
  cursor: pointer;
}
</style>
