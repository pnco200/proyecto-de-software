
<template>
    <div>
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
        <h1>Información de la institución:</h1>
        <div class="card">
            <div class="card-body">
                <h5 class="card-title">{{ institucion.name }}</h5>
                <p class="card-text">Información: {{ institucion.information }}</p>
                <p class="card-text">Palabras clave: {{ institucion.key_words }}</p>
                <p class="card-text">Contacto: {{ institucion.contact }}</p>
                <p class="card-text">Web: {{ institucion.web }}</p>
                <p class="card-text">Horario de atención: {{ institucion.attention_time }}</p>
                <p class="card-text">Dirección: {{ institucion.address }}</p>
            </div>
        
        </div>
    </div>

</template>

<script>
import axios from 'axios';
export default {

    data() {
        return {
            service: {},
            service_id: this.$route.query.service_id,
            institucion: {},
        }
    },
    methods : {
        getService() {
            axios.get(`http://127.0.0.1:5000/api/services/${this.service_id}`)
            .then(response => {
                this.service = response.data;
                console.log(this.service);
                this.getInstitucion();
            })
            .catch(error => {
                console.log(error);
            })
        },
        getInstitucion() {
            axios.get(`http://127.0.0.1:5000/api/institutions/${this.service.institution_id}`)
            .then(response => {
                this.institucion = response.data;
                console.log(this.institucion);
            })
        }
    },
    created() {
        this.getService();
    }
};
</script>
  