<template>
  <router-link :to="{ name: 'request', params: { serviceId: id } }">
    <button class="custom-button">Solicitar servicio id {{ id }}</button>
  </router-link>
</template>

<script>
export default {
  props: {
    id: {
      type: Number,
      required: true,
    },
  },
};
</script>

<style scoped>
/* Estilos específicos del botón */
.custom-button {
  display: block;
  width: 100%;
  text-align: center;
  padding: 15px;
  background-color: #3498db; /* Color celeste azulado */
  color: #ffffff; /* Color blanco para el texto */
  border: none;
  border-radius: 5px; /* Borde redondeado */
  cursor: pointer;
  font-size: 16px; /* Ajusta el tamaño de la fuente según sea necesario */
}

.custom-button:hover {
  background-color: #2980b9; /* Cambia el color al pasar el ratón sobre el botón */
}
</style>
