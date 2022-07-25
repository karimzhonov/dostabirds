import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/components/main/main.vue'
import register from "@/components/register";
import login from "@/components/login";

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/register',
    name: "register",
    component: register
  },
  {
    path: '/login',
    name: 'login',
    component: login
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
