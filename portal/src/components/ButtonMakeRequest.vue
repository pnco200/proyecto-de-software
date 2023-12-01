<template>
  <div>
    
    <router-link v-if="tieneToken" :to="{ name: 'request', params: { serviceId: id } }">
      <button class="custom-button-alt">Solicitar servicio id {{ id }}</button>
    </router-link>
    <router-link v-else :to="{ name: 'login' }">
      <button  class="custom-button-alt" >Inicie sesion para solicitar</button>
    </router-link>
  </div>
</template>

<script>
import Cookies from "js-cookie";

export default {
  props: {
    id: {
      type: Number,
      required: true,
    },
  },
  data() {
    return {
      tieneToken: false,
    };
  },
  mounted() {
    // Verifica si la cookie 'token' está presente
    const jwtToken = Cookies.get('token');
    this.tieneToken = !!jwtToken;
  },
};
</script>

<style scoped>
.custom-button-alt {
  display: block;
  width: 100%;
  text-align: center;
  padding: 15px;
  background-color: #e74c3c; 
  color: #ffffff; 
  border: none;
  border-radius: 5px; 
  cursor: pointer;
  font-size: 16px;
}

.custom-button-alt:hover {
  background-color: #c0392b;
}
</style>
