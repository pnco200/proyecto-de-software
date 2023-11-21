<template>
  <form class="request-form" @submit.prevent="submitRequest">
    <label for="serviceId">ID de Servicio:</label>
    <input v-model="serviceId" type="text" id="serviceId" required>

    <label for="description">Descripción:</label>
    <textarea v-model="description" id="description" required></textarea>

    <label for="files">Adjuntar Archivos:</label>
    <input class="file-input" type="file" ref="files" @change="validateFile" accept=".txt, .pdf, .docx" multiple>
    <p id="fileSizeError" style="color: red; display: none;">El archivo debe ser menor a 50 MB.</p>
    <p id="fileCountError" style="color: red; display: none;">Selecciona solo un archivo.</p>

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
      // Verificar si se han seleccionado archivos
      if (!this.$refs.files.files || this.$refs.files.files.length !== 1) {
        document.getElementById('fileCountError').style.display = 'block';
        return;
      } else {
        document.getElementById('fileCountError').style.display = 'none';
      }

      // Verificar el tamaño del archivo
      const maxFileSizeInBytes = 50 * 1024 * 1024; // 50 MB
      if (this.$refs.files.files[0].size > maxFileSizeInBytes) {
        document.getElementById('fileSizeError').style.display = 'block';
        return;
      } else {
        document.getElementById('fileSizeError').style.display = 'none';
      }

      // Emitir el evento con los datos del formulario
      this.$emit('submitRequest', {
        serviceId: this.serviceId,
        description: this.description,
        files: this.$refs.files.files,
      });
    },
    validateFile() {
      const fileSizeError = document.getElementById('fileSizeError');
      const fileCountError = document.getElementById('fileCountError');

      // Verificar el tamaño del archivo en el evento change
      const maxFileSizeInBytes = 50 * 1024 * 1024; // 50 MB

      if (this.$refs.files.files.length !== 1) {
        fileCountError.style.display = 'block';
      } else {
        fileCountError.style.display = 'none';
      }

      for (let i = 0; i < this.$refs.files.files.length; i++) {
        if (this.$refs.files.files[i].size > maxFileSizeInBytes) {
          this.$refs.files.value = ''; // Limpiar el input si el archivo es demasiado grande
          fileSizeError.style.display = 'block';
          return;
        } else {
          fileSizeError.style.display = 'none';
        }
      }
    },
  },
};
</script>

<style scoped>
.request-form {
  max-width: 400px;
  margin: 0 auto;
}

label {
  display: block;
  margin-bottom: 5px;
  color: #007BFF;
  text-align: center;
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
  background-color: #007BFF;
  color: white;
  padding: 10px;
  border: none;
  cursor: pointer;
  border-radius: 5px;
}

button:hover {
  background-color:#007BFF;
  text-align: center;
}

label{
  color: #007BFF;
  text-align: center;
}
</style>
