import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'
import ServiceListView from '../views/ServiceListView.vue'
import ServiceDetail from '../views/ServiceDetail.vue'
import ChartView from '../views/ChartView.vue'

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
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    }
  ]
})

export default router
