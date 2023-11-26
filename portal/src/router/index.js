import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'
import ServiceListView from '../views/ServiceListView.vue'
import ServiceDetail from '../views/ServiceDetail.vue'
import ChartView from '../views/ChartView.vue'
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
      component: ChartView
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
      path: '/request-service/:serviceId',
      name: "request",
      component: RequestView,
      props: true,
    },
    {
      path: '/list-request',
      name: "RequestList",
      component: RequestList,
    },
    {
      // Ruta para la vista que muestra el detalle de una solicitud, RequestButton.vue la llama cuando se
      path:'/info-request/:requestId',
      name:"RequestInfo",
      component:RequestInfoView,
    },
    {
      path:'/notes-request/:requestId',
      name:"RequestNotes",
      component: RequestNotes,
    }
  ]
})

export default router
