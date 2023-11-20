<template>
  <div class="request-complete-info">
    <h3>{{ solicitud.title }}</h3>
    <p class="description">{{ solicitud.description }}</p>
    <div class="info">
      <p><strong>Fecha de Creación:</strong> {{ solicitud.creation_date }}</p>
      <p><strong>Fecha de Cierre:</strong> {{ solicitud.close_date }}</p>
      <p><strong>Estado:</strong> {{ solicitud.status }}</p>
    </div>
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
