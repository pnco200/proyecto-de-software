<template>
  <li class="request-list-element">
    <h4> Fecha: {{ solicitud.creation_date }}</h4>
    <p>Estado: {{ solicitud.status }}</p>
    <p>Observaciones: {{ solicitud.observations }}</p>

    <RequestButton :solicitud="solicitud" @buttonClick="handleButtonClick" />
    <ButtonRequestnote :solicitud="solicitud" @buttonClick="handleButtonRequestnoteClick" />
  </li>
</template>

<script>
import RequestButton from '@/components/RequestButton.vue';
import ButtonRequestnote from '@/components/ButtonRequestnote.vue';

export default {
  props: {
    solicitud: Object,
  },
  components: {
    RequestButton,
    ButtonRequestnote,
  },
  methods: {
    handleButtonClick() {
      this.$emit('detailsClick', this.solicitud);
    },
    handleButtonRequestnoteClick() {
      this.$emit('notesClick', this.solicitud);
    },
  },
};
</script>

<style >
.request-list-element {
  background-color: #e0f7fa; /* Celeste claro */
  border: 1px solid #4fc3f7; /* Azul claro */
  padding: 15px;
  margin: 10px;
  border-radius: 5px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.request-list-element h4 {
  color: #0288d1; /* Azul */
}

.request-list-element p {
  color: #01579b; /* Azul oscuro */
}

.request-list-element button {
  background-color: #03a9f4; /* Azul brillante */
  color: #ffffff; /* Blanco */
  border: none;
  padding: 8px 16px;
  margin-top: 10px;
  cursor: pointer;
  border-radius: 3px;
}

.request-list-element button:hover {
  background-color: #0288d1; /* Azul más oscuro al pasar el ratón */
}
</style>
