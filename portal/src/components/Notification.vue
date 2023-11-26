<template>
    <div class="notification">
      <p>{{ message }}</p>
      <button @click="closeNotification">Cerrar</button>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      message: {
        type: String,
        required: true,
      },
    },
    methods: {
      closeNotification() {
        // Emitir un evento para indicar que la notificación debe cerrarse
        this.$emit('close');
      },
    },
  };
  </script>
  
  <style scoped>
  .notification {
    border: 1px solid #ddd;
    border-radius: 5px;
    padding: 15px;
    margin-bottom: 15px;
    background-color: #f8f8f8;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  
  p {
    margin: 0;
    flex: 1;
  }
  
  button {
    cursor: pointer;
    background-color: #4caf50;
    color: white;
    border: none;
    padding: 10px 15px;
    border-radius: 5px;
    transition: background-color 0.3s ease;
  }
  
  button:hover {
    background-color: #45a049;
  }
  </style>
  