import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Inventory from '../views/Inventory.vue'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/inventory',
      name: 'inventory',
      component: Inventory
    }
  ]
})

export default router