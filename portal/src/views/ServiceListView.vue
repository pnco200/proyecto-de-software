<template>
    <div class="info-section">
      <h1>Busqueda de servicios</h1>
  
      <div class="mb-3">
        <div class="row">
          <div class="col-md-2">
            <label class="ml-2 mr-2">Palabra Clave</label>
            <input v-model="filters.keywords" class="form-control form-control-sm" />
          </div>

          <div class="col-md-2">
            <label class="ml-2 mr-2">Tipo de servicio</label>
            <select v-model="filters.serviceType" class="form-control form-control-sm">
              <option value="TODOS" selected>TODOS</option>
              <option v-for="_typ in types" :key="_typ" :value="_typ">{{ _typ }}</option>
            </select>
          </div>
          <div class="col-md-2">
            <button @click="fetchServices" class="btn btn-primary btn-sm mt-4">Buscar</button>
          </div>
      </div>
    </div>
      <div v-if="services.length > 0">
        <table class="table table-striped mt-3">
        <thead>
          <tr>
            <th>Titulo</th>
            <th>Descripcion</th>
            <th>Institucion</th>
            <th>Palabras Claves</th>
            <th>Tipo de Servicio</th>
            <th>Detalle</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="service in services" :key="service.id">
            <td>{{ service.name }}</td>
            <td>{{ service.description }}</td>
            <td>{{ service.institution_name }}</td>
            <td>{{ service.key_words }}</td>
            <td>{{ service.type }}</td>
            <td>           
              <router-link :to="{ name: 'service-detail', query: { service_id: service.id } }">
                <button class="btn btn-info btn-sm">Visualizar</button>
              </router-link>
            </td>

          </tr>
        </tbody>
      </table>
      <div class="mt-3">
        <button @click="fetchServices(page - 1)" :disabled="page === 1" class="btn btn-secondary btn-sm">Anterior</button>
        <span class="mx-2">Pagina {{ page }} de {{ totalPages }}</span>
        <button @click="fetchServices(page + 1)" :disabled="page === totalPages" class="btn btn-secondary btn-sm">Siguiente</button>
      </div>
      </div>
      <div v-else>
      <p>No se encontraron servicios con los filtros aplicados.</p>
    </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        types:[],
        filters: {
          keywords: '',
          serviceType: '',
        },
        services: [],
        page: 1,
        totalPages: 1,
      };
    },
    async created() {
      await this.fetchServices();
      await this.fetchTypes();

    },
    methods: {
      async fetchServices(newPage = 1) {
        try {
          const response = await axios.get('https://admin-grupo25.proyecto2023.linti.unlp.edu.ar/api/services/search', {
            params: {
              q: this.filters.keywords,
              type: this.filters.serviceType,
              page: newPage,
            },
          });


          this.services = response.data.data;
          this.page = response.data.page;
          let totalPages = Math.floor(response.data.total/response.data.per_page);
          if(response.data.total % response.data.per_page > 0){
            this.totalPages = totalPages + 1
          }else{
            this.totalPages = totalPages
          }
        } catch (error) {
          alert("Ocurrio un error al traer los servicios.")
          console.error('Error fetching services:', error);
        }
      },
      async fetchTypes() {
        try {
          const response = await axios.get('http://127.0.0.1:5000/api/services/types');

          this.types = Object.keys(response.data);
          console.log(response.data)
          this.page = response.data.page;
        } catch (error) {
          console.error('Error fetching types:', error);
          alert("Ocurrio un error al traer los tipos.")
        }
      },
    },
  };
  </script>