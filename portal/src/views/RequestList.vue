<template>
  <div>
    <h2 align="center">Listado de Solicitudes de Servicio</h2>

    <div align="center">
      <label>
       <strong> Ordenar por fecha:</strong>
        <input type="checkbox" v-model="orderByDate" />
      </label>

      <label>
        <strong> por estado:</strong>
        <select v-model="selectedStatus">
          <option value="">Todos</option>
          <option value="inicial">Inicial</option>
          <option value="aceptada">Aceptada</option>
          <option value="en_proceso">En Proceso</option>
          <option value="finalizada">Finalizada</option>
          <option value="cancelada">Cancelada</option>
        </select>
      </label>

      <!-- Botón que activa el filtrado y ordenamiento -->
      <button @click="fetchSolicitudes">Aplicar Filtros</button>
    </div>

    <ul align="center" v-if="solicitudes.length > 0">
      <RequestListElement
        v-for="solicitud in solicitudes"
        :key="solicitud.id"
        :solicitud="solicitud"
        @detailsClick="handleDetailsClick"
        @notesClick="handleButtonRequestnoteClick"
      />
      <!-- Aca le pasa la info al componente -->
    </ul>

    <p v-else>No hay solicitudes de servicio.</p>

    <div align="center">
      <button @click="prevPage" :disabled="currentPage === 1">Anterior</button>
      <span>{{ currentPage }}</span>
      <button @click="nextPage" :disabled="currentPage * perPage >= total">Siguiente</button>
    </div>
  </div>
</template>

<script>
import RequestListElement from "@/components/RequestListElement.vue";
import axios from "axios";
import Cookies from "js-cookie";

export default {
  data() {
    return {
      solicitudes: [],
      currentPage: 1,
      perPage: 10,
      total: 0,
      orderByDate: false,
      selectedStatus: "",
    };
  },
  mounted() {
    this.fetchSolicitudes();
  },
  methods: {
    async fetchSolicitudes() {
      const jwtToken = Cookies.get("token");
      if (jwtToken) {
        try {
          const response = await axios.get(
            "https://admin-grupo25.proyecto2023.linti.unlp.edu.ar/api/me/requests-paginated",
            {
              params: {
                page: this.currentPage,
                per_page: this.perPage,
                sort: this.orderByDate ? "creation_date" : "",
                status: this.selectedStatus,
                order: this.orderByDate,
              },
              headers: {
                "Content-Type": "application/json",
                Authorization: `Bearer ${jwtToken}`,
              },
            }
          );

          this.solicitudes = response.data.data;
          this.total = response.data.total;
        } catch (error) {
          console.error("Error al obtener las solicitudes:", error.message);
          alert(error.message)
        }
      } else {
        console.error("No se encontró un token en las cookies.");
      }
    },
    handleDetailsClick(solicitud) {
      console.log("Detalles de la solicitud:", solicitud);
    },
    handleButtonRequestnoteClick(solicitud) {
      console.log("Notas/mensajes de la solicitud:", solicitud);
    },
    prevPage() {
      if (this.currentPage > 1) {
        this.currentPage -= 1;
        this.fetchSolicitudes();
      }
    },
    nextPage() {
      if (this.currentPage * this.perPage < this.total) {
        this.currentPage += 1;
        this.fetchSolicitudes();
      }
    },
  },
  components: {
    RequestListElement,
  },
};
</script>

<style>
/* Estilos específicos de la lista si es necesario */
</style>
