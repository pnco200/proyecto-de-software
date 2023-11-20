<template>
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
        <div class="container-fluid">

            <router-link to="/" class="navbar-brand">
                <img src="../assets/cidepint.png" alt="Logo">
            </router-link>


            <!-- <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <form class="d-flex" role="search">
                    <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
                    <button class="btn btn-outline-primary" type="submit">Search</button>
                </form>
            </div> -->
            
            <router-link to="/login">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-person-circle" viewBox="0 0 16 16">
                    <path d="M11 6a3 3 0 1 1-6 0 3 3 0 0 1 6 0z"/>
                    <path fill-rule="evenodd" d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8zm8-7a7 7 0 0 0-5.468 11.37C3.242 11.226 4.805 10 8 10s4.757 1.225 5.468 2.37A7 7 0 0 0 8 1z"/>
                </svg>
            </router-link>
        </div>
    </nav>
</template>

<style scoped>
.navbar-brand img {
    width: 250px;
    height: 100px;
    margin: 0;
    padding: 0;
}
.navbar {
    padding: 0;
    margin: 0;
    height: 100px;
    background-color: #fff;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
}

svg {
    width: 30px;
    height: 50px;
    margin: 0 20px;
    padding: 0;
}

/* Need the input longer */
form {
    width: 80%;
}
</style>