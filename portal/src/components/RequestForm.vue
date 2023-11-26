<template>
  <div class="request-form">
    <h3>Complete el formulario de solicitud</h3>

    <!-- Formulario -->
    <form @submit.prevent="submitForm">
      <!-- Campo de service_id (readonly y con valor predeterminado) -->
      <label for="serviceId">ID del servicio: {{ serviceId }}</label>

      <!-- Campo de description -->
      <label for="description">Descripción:</label>
      <textarea v-model="formData.description" required></textarea>

      <!-- Campo de archivo -->
      <label for="file">Adjuntar archivo (opcional):</label>
      <input type="file" @change="handleFileChange" />

      <!-- Botón de enviar -->
      <button type="submit">Enviar Solicitud</button>
    </form>
  </div>
</template>

<script>
export default {
  props: {
    serviceId: {
      type: Number,
      required: true
    },
  },
  data() {
    return {
      formData: {
        serviceId: this.serviceId,  // Establecer el valor predeterminado con la prop recibida
        description: '',
        files: null,
      },
    };
  },
  methods: {
    handleFileChange(event) {
      // Permitir que se elija un solo archivo
      this.formData.files = event.target.files.length > 0 ? event.target.files[0] : null;
    },
    submitForm() {
      // Emitir evento al componente padre con los datos del formulario
      this.$emit('submitRequest', this.formData);

      // Restablecer el formulario después de enviar la solicitud
      this.formData = {
        serviceId: this.serviceId,  // Mantener el valor predeterminado
        description: '',
        files: null,
      };
    },
  },
};
</script>

<style scoped>
/* Estilos específicos para el formulario */
.request-form {
  background-color: #ccf5d1;
  padding: 20px;
  margin: 10px;
  border-radius: 8px;
}

/* Estilos para etiquetas y campos */
label {
  display: block;
  margin-bottom: 5px;
}

input,
textarea,
button {
  margin-bottom: 10px;
}

/* Estilos para el botón de enviar */
button {
  background-color: #4caf50;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
</style>
