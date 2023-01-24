import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home'
import Modifica from '../views/Modifica'

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/gestisci',
    name: 'about',
    
    component:Modifica
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
