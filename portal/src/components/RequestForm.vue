<template>
  <form class="request-form" @submit.prevent="submitRequest">
    <label for="serviceId">ID de Servicio:</label>
    <input v-model="serviceId" type="text" id="serviceId" required>

    <label for="description">Descripción:</label>
    <textarea v-model="description" id="description" required></textarea>

    <label for="files">Adjuntar Archivos:</label>
    <input class="file-input" type="file" ref="files" multiple>

    <button type="submit">Enviar Solicitud</button>
  </form>
</template>

<script>
export default {
  data() {
    return {
      serviceId: '',
      description: '',
      files: null,
    };
  },
  methods: {
    submitRequest() {
      this.$emit('submitRequest', {
        serviceId: this.serviceId,
        description: this.description,
        files: this.$refs.files.files, // Obtén los archivos desde el elemento ref
      });
    },
  },
};
</script>

<style scoped>
/* Estilos específicos del componente */
.request-form {
  max-width: 400px;
  margin: 0 auto;
}

label {
  display: block;
  margin-bottom: 5px;
}

input,
textarea {
  width: 100%;
  padding: 8px;
  margin-bottom: 10px;
}

.file-input {
  margin-bottom: 20px;
}

button {
  background-color: #4caf50;
  color: white;
  padding: 10px;
  border: none;
  cursor: pointer;
  border-radius: 5px;
}

button:hover {
  background-color: #45a049;
}
</style>
