<template>
  <li>
    <h4>{{ solicitud.title }} - {{ solicitud.creation_date }}</h4>
    <p>{{ solicitud.status }}</p>
    <p>{{ solicitud.observations }}</p>

    <ButtonComponent @buttonClick="handleButtonClick" />
    <ButtonRequestnote @buttonClick="handleButtonRequestnoteClick" />
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
      this.$emit('detailsClick',this.solicitud);
    },
  },
};
</script>

<style scoped>
/* Estilos específicos del elemento de la lista si es necesario */
</style>
