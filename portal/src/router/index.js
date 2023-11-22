import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'
import ServiceListView from '../views/ServiceListView.vue'
import ServiceDetail from '../views/ServiceDetail.vue'

import RequestView from '../views/RequestView.vue'
import RequestList from '../views/RequestList.vue'
import RequestInfoView from '../views/RequestInfoView.vue'
import RequestNotes from '../views/RequestNotes.vue'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path:'/stats',
      name: 'stats',
      component: () => import('../views/ChartView.vue')
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView,
    },
    {
      path: '/services',
      name: 'services',
      component: ServiceListView,
    },
    {
      path: '/service-detail',
      name: 'service-detail',
      component: ServiceDetail,
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/request-service',
      name: "request",
      component: RequestView,
    },
    {
      path: '/list-request',
      name: "RequestList",
      component: RequestList,
    },
    {
      // Ruta para la vista que muestra el detalle de una solicitud, RequestButton.vue la llama cuando se
      path:'/info-request',
      name:"RequestInfo",
      component:RequestInfoView,
    },
    {
      path:'/notes-request',
      name:"RequestNotes",
      component: RequestNotes,
    }
  ]
})

export default router
