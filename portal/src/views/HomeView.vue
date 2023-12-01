<template>
  <h1>Bienvenido a CIDEPINT </h1>
  <p>
    CIDEPINT, el Centro de Investigación y Desarrollo en Tecnología de Pinturas de Argentina, 
    te da la bienvenida. Somos pioneros en el impulso de la competitividad de los productos de 
    pintura argentinos a nivel nacional e internacional mediante investigaciones y desarrollos 
    avanzados en tecnología de recubrimientos. Desde nuestros inicios en la década de 1970, hemos 
    evolucionado para abordar no solo las necesidades de la industria de pinturas, sino también para 
    explorar soluciones en el tratamiento de aceros, la protección contra la corrosión y alternativas 
    ecológicas.
  </p>

  <div class="container">
    <h2>¿Cómo puedes aprovechar nuestra plataforma?</h2>
    <div class="item">
      <h3>Realizar búsqueda de servicios</h3>
      <p>
        Utiliza nuestra herramienta de búsqueda para encontrar rápidamente los servicios que necesitas. 
        Ingresa palabras clave, filtra por categoría, y encuentra las soluciones que se 
        adaptan a tus necesidades.
      </p>
      <router-link to="/services">Buscar servicios</router-link>
    </div>
    <div class="item">
      <h3>Ver los servicios que ofrece cada institución</h3>
      <p>
        Explora la diversidad de servicios ofrecidos por cada institución asociada. Desde 
        investigaciones innovadoras hasta prácticas ecológicas, cada institución contribuye de 
        manera única a la industria de recubrimientos.
      </p>
    </div>
    <div class="item">
      <h3>Solicitar un servicio</h3>
      <p>
        Inicia una solicitud de servicio para reservar turnos, utilizar equipamiento 
        especializado o simplemente establecer contacto con las instituciones. Facilitamos el 
        proceso para que puedas obtener los servicios que necesitas de manera eficiente.
      </p>
    </div>
    <div class="item">
      <h3>Ver estadisticas</h3>
      <p>
        Explora las diferentes estadisticas que se generan a partir de los servicios ofrecidos por
        las instituciones asociadas.
      </p>
      <router-link to="/stats">Ver estadisticas</router-link>
    </div>
    
  </div>
  <footer >
    Información de contacto: {{ contact_information }}
  </footer>
  
</template>

  
<script lang="js">
import axios from 'axios'

export default {
  name: 'HomeView',
  data () {
    return {
      contact_information: ''
    }
  },
  methods: {
    async contactInformation () {
      try {
        const response = await axios.get('http://127.0.0.1:5000/api/configuration/getconfig')
        this.contact_information = response.data.contact_information
      } catch (error) {
        console.log(error)
      }
    }
  },
  mounted () {
    this.contactInformation()
  }
}
</script>
<style scoped>
body {
  font-family: 'Arial', sans-serif;
  background-color: #f7f7f7;
  color: #333;
  margin: 0;
  padding: 0;
  min-height: 100vh; 
  display: flex;
  flex-direction: column;
}

.container {
  max-width: 800px;
  margin: 20px auto;
  background-color: #fff;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  flex: 1; 
}

h1 {
  color: #007BFF;
  text-align: center;
}

h2, h3 {
  color: #333;
}

p {
  line-height: 1.6;
  padding: 1%;
}

.item {
  margin-top: 20px;
}

.item h3 {
  color: #007BFF;
  margin-bottom: 10px;
}

a {
  display: inline-block;
  margin-top: 10px;
  padding: 10px;
  background-color: #007BFF;
  color: #fff;
  text-decoration: none;
  border-radius: 4px;
  transition: background-color 0.3s;
}

a:hover {
  background-color: #0069D9;
}

footer {
  padding: 20px;
  background-color: #007BFF;
  color: #fff;
  text-align: center;
  width: 100%;
}
</style>
