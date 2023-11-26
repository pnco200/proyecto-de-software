<template>
    <div class="grid-container">
      <div class="info-service">
        <h1>Información del servicio:</h1>
        <div class="card">
          <div class="card-body">
            <h5 class="card-title">Servicio: {{ service.name }}</h5>
            <p class="card-text">Descripción: {{ service.description }}</p>
            <p class="card-text">Palabras clave: {{ service.key_words }}</p>
            <p class="card-text">Tipo: {{ service.type }}</p>
            <p class="card-text">Centros: {{ service.centers }}</p>
          </div>
        </div>
      </div>
  
      <div>
        <ButtonMakeRequest :id="service_id" />
  
      </div>
  
      <div class="info-institution">
        <h1>Información de la institución:</h1>
        <div class="card">
          <div class="card-body">
            <h5 class="card-title">{{ institucion.name }}</h5>
            <p class="card-text">Información: {{ institucion.information }}</p>
            <p class="card-text">Web: {{ institucion.web }}</p>
            <p class="card-text">Horario de atención: {{ institucion.attention_time }}</p>
            <p class="card-text">Dirección: {{ institucion.address }}</p>
          </div>
        </div>
      </div>
  
      <div class="map-container">
        <div class="map">
          <MapComponent 
            :key="componentkey" 
            :coordinates="[latitud, longitud]" 
            :contact_information="institucion.contact"
          />
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import ButtonMakeRequest from '../components/ButtonMakeRequest.vue';
  import axios from 'axios';
  import MapComponent from '../components/MapComponent.vue';
  
  export default {
    data() {
      return {
        service: {},
        service_id: this.$route.query.service_id,
        institucion: {},
        longitud: 0,
        latitud: 0,
        componentkey: 0,
      };
    },
    components: {
      MapComponent,
      ButtonMakeRequest,
    },
    methods: {
      getService() {
        axios
          .get(`https://admin-grupo25.proyecto2023.linti.unlp.edu.ar/api/services/${this.service_id}`)
          .then((response) => {
            this.service = response.data;
            this.getInstitucion();
          })
          .catch((error) => {
            console.log(error);
          });

      },
      getInstitucion() {
        axios
          .get(`https://admin-grupo25.proyecto2023.linti.unlp.edu.ar/api/institutions/${this.service.institution_id}`)
          .then((response) => {
            this.institucion = response.data;
            this.longitud = this.institucion.localization[0];
            this.latitud = this.institucion.localization[1];
            this.componentkey += 1;
          });
      },
    },
    created() {
      this.getService();
    },
  };
  </script>
  
  <style scoped>
  .grid-container {
    display: grid;
    grid-template-columns: 60% 40%;
    gap: 20px;
    padding: 20px;
  }
  
  .info-service {
    grid-column: 1;
  }
  
  .info-institution {
    grid-column: 1;
  }
  
  .map-container {
    grid-column: 2;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  
  .map {
    width: 90%;
  }
  
  .card {
    border: 1px solid #ddd;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  }
  
  .card-title {
    color: #333;
    font-size: 1.5rem;
    margin-bottom: 10px;
  }
  
  .card-text {
    color: #555;
    margin-bottom: 5px;
  }
  </style>
  