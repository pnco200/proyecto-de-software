<template>
  <router-link :to="{ name: 'RequestInfo', params: { requestId: solicitud.id } }">
    <button class="details-button">Detalles</button>
  </router-link>
</template>

<script>
export default {
  props: {
    solicitud: Object,
  },
};
</script>

<style scoped>
.details-button {
  background-color: #ffffff; /* Blanco */
  color: #000000; /* Texto negro */
  border: 1px solid #e0e0e0; /* Borde gris claro */
  padding: 8px 16px;
  cursor: pointer;
  border-radius: 5px;
}

.details-button:hover {
  background-color: #f0f0f0; /* Fondo gris claro al pasar el ratón */
}
</style>
