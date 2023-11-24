<template>
  <div class="request-complete-info">
    <h3>ID :{{ solicitud.id}}</h3>
    <p class="description">Descripción/Observacion suya: {{ solicitud.observations}}</p>
    <div class="info">
      <p><strong>Fecha de Creación:  </strong> {{ solicitud.inserted_at}}</p>
      <p><strong>Estado:  </strong> {{ solicitud.status }}</p>


    </div>
    <div v-if="solicitud.state_message" class="message-section">
      <p><strong>Sobre el Estado:</strong> {{ solicitud.state_message }}</p>
    </div>
    <div v-if="solicitud.file" class="file-section">
      <a :href="solicitud.file" download>
        <button class="download-button">Descargar Archivo</button>
      </a>
    </div>
    <router-link :to="{ name: 'service-detail', query: { service_id: solicitud.service_id } }">
      <button class="details-button">Ver Servicio que se pidió</button>
    </router-link>
    <!-- Otros detalles de la solicitud -->
  </div>
</template>

<script>
export default {
  props: {
    solicitud: Object,
    // Puedes agregar más props según sea necesario
  },
};
</script>

<style scoped>
/* Estilos específicos del componente */
.request-complete-info {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  background-color: #fff;
}
.details-button {
  background-color: #ffffff; /* Blanco */
  color: #000000; /* Texto negro */
  border: 1px solid #e0e0e0; /* Borde gris claro */
  padding: 8px 16px;
  cursor: pointer;
  border-radius: 5px;
}
.request-complete-info h3 {
  font-size: 1.5em;
  color: #333;
  margin-bottom: 10px;
}

.request-complete-info .description {
  font-size: 1.2em;
  color: #555;
  margin-bottom: 15px;
}

.request-complete-info .info {
  margin-top: 15px;
}

.request-complete-info .info p {
  font-size: 1em;
  color: #777;
  margin: 5px 0;
}
</style>
