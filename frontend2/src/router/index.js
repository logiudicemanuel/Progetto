import { createRouter, createWebHistory } from 'vue-router'
import SignUp from '../views/SignUp'
import Home from '../views/Home'
import Gestisci from '../views/Gestisci'
const routes = [
  {
    path: '/',
    name: 'SignUp',
    component: SignUp
  }, 
  {
    path: '/Home',
    name: 'Home',
    component: Home
  },
  {
    path: '/Gestisci',
    name: 'Gestisci',
    component: Gestisci
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
