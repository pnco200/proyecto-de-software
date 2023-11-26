<template>
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
        <div class="container-fluid">

            <router-link to="/" class="navbar-brand">
                <img src="../assets/cidepint.png" alt="Logo" class="img-fluid">
            </router-link>

            <div v-if="!logged" class="d-flex flex-row">
                <router-link to="/login" class="btn btn-primary ml-auto">
                    Iniciar Sesion
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-person-circle" viewBox="0 0 16 16">
                        <path d="M11 6a3 3 0 1 1-6 0 3 3 0 0 1 6 0z"/>
                        <path fill-rule="evenodd" d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8zm8-7a7 7 0 0 0-5.468 11.37C3.242 11.226 4.805 10 8 10s4.757 1.225 5.468 2.37A7 7 0 0 0 8 1z"/>
                    </svg>
                </router-link>
            </div>
            <div v-else class="d-flex flex-row">
                <span @click="see_requests" class="btn btn-primary ml-auto">Ver Solicitudes</span>
                <span @click="close_session" class="btn btn-danger ml-2">Cerrar Sesion</span>
            </div>
        </div>
    </nav>
</template>

<style scoped>
.navbar-brand img {
    width: 100%;
    height: auto;
}

.navbar {
    padding: 10px;
    background-color: #fff;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
}

svg {
    width: 1.5em;
    height: 1.5em;
    margin-right: 0.5em;
}

.btn {
    white-space: nowrap;
}

@media (max-width: 360px) {
    .navbar-brand img {
        width: 80%;
    }
}

@media (min-width: 361px) and (max-width: 767px) {
    .navbar-brand img {
        width: 150px;
    }
}

@media (min-width: 768px) {
    .navbar-brand img {
        width: 250px;
    }
}
</style>

<script>
    import Cookies from 'js-cookie';
    export default {
    data() {
      return {
        logged:this.check_login()
      };
    },
    
    created() {
        this.logged = this.check_login();
    },

    methods: {
        check_login() {
            const token = Cookies.get('token')
            if(token){
                return true
            }else{
                return false
            }
        },
        close_session() {
            Cookies.remove('token')
            this.logged = this.check_login()
            this.$router.push({ name: 'home' });
        },
        see_requests(){
            this.$router.push({ name: 'RequestList' });
        }
    },
  };
</script>