<template>
    <div class="container mt-5">
      <div class="row justify-content-center">
        <div class="col-md-6">
          <div class="card">
            <div class="card-header">Iniciar sesion</div>
            <div class="card-body">
              <form @submit.prevent="login">
                <div class="mb-3">
                  <label for="username" class="form-label">Email:</label>
                  <input type="text" class="form-control" v-model="username" required />
                </div>
                <div class="mb-3">
                  <label for="password" class="form-label">Contraseña:</label>
                  <input type="password" class="form-control" v-model="password" required />
                </div>
                <button type="submit" class="btn btn-primary">Confirmar</button>
              </form>
            </div>
            <div class="m-3">
              <img @click="redirigirUsuario" src="../assets/googleLogoOficial.png" alt="Logo">
            </div>
          </div>
        </div>
      </div>
      
    </div>
  </template>
  
  <script>
  import Cookies from 'js-cookie';
  import axios from 'axios';

  export default {
    data() {
      return {
        username: '',
        password: '',
      };
    },
    created() {
    const urlParams = new URLSearchParams(window.location.search);
    const token = urlParams.get('token_google');
    if (token) {
      if(token == "fail"){
        alert("Su cuenta se encuentra bloqueada!")
      }else{
        Cookies.set('token', token);
        this.$router.push({ name: 'home' });
      }
    }
    },
    methods: {
        async login() {
            try {
                if(!this.username || !this.password){
                    alert("Debe completar ambos campos!")
                    return
                }
                const response = await axios.post('http://localhost:5000/api/auth/', {
                  user: this.username,
                  password: this.password,
                 
                });
                if(response.status == 200){
                  Cookies.set('token', response.data.result);
                  alert("El logeo fue exitoso")
                  this.$router.push({ name: 'home' });
                }
            } catch (error) {
                console.error('Login failed:', error.message);
                alert("Error al iniciar sesion")
                return
            }
        },
        redirigirUsuario() {
          window.location.href = 'http://localhost:5000/auth/google?is_portal=True';
        }
    },
  };
  </script>
  
  