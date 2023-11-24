<template>
    <div>
      <h2>Chat con Operador</h2>
      <h3>Notas o Mensajes con Operador del Servicio</h3>
  
      <!-- Aquí puedes agregar algún componente para mostrar detalles de la solicitud si es necesario -->
  
      <!-- Chat Messages -->
      <div v-for="message in filteredMessages" :key="message.id" :class="{ 'my-message': isMyMessage(message) }">
        {{ message.content }}
      </div>
  
      <!-- Aquí puedes agregar un formulario o componente para enviar nuevos mensajes si es necesario -->
    </div>
  </template>
  
  <script>
  import axios from 'axios'
  import Cookies from 'js-cookie'
  export default {
    props: {
      solicitud: Object,
    },
    data() {
      return {
        messages: [], // La lista de mensajes que obtienes de la API
      };
    },
    created() {
    // Llama a la API para obtener mensajes asociados a la solicitud
    this.fetchMessages();
   },
    computed: {
      filteredMessages() {
        // Filtra los mensajes según el user_id de la solicitud
        return this.messages.filter(message => message.user_id === this.solicitud.user_id);
      },
    },
    methods: {
      async fetchMessages() {
         const jwtToken = Cookies.get('token')
         if(jwtToken){
        try {
        // Utiliza this.solicitud.id para enviar el ID de la solicitud a la API
        const response = await axios.get(`http://localhost:5000/api/me/request/${this.$router.params.requestId}}/notes`,{
          headers: {
              'Content-Type': 'application/json',
              'Authorization': `Bearer ${jwtToken}`,
            },
        });
        
        this.messages = response.data;
      } catch (error) {
        console.error('Error al obtener mensajes:', error);
      }
    }else{
      console.log('no hay jwt token para utilizar')
    }
    },
      isMyMessage(message) {
        // Verifica si el mensaje es del usuario que hizo la solicitud
        return message.user_id === this.solicitud.user_id;
      },
    },
  };
  </script>
  
  <style scoped>
  .my-message {
    text-align: right; /* Alinea los mensajes del usuario a la derecha */
    background-color: #DCF8C6; /* Cambia el color de fondo de los mensajes del usuario si es necesario */
  }
  </style>
  