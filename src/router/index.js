import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AboutView from '../views/AboutView.vue'
import WordView from '../views/WordView.vue';
import PoemView from '../views/PoemView.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/word/:word',
      name: 'word',
      component: WordView,
      props: true
    },
    {
      path: '/poem/:id/:l/:w',
      name: 'poem',
      component: PoemView,
      props: true
    },
    {
      path: '/about',
      name: 'about',
      component: AboutView // for lazy loading use () => import('../views/AboutView.vue')
    }
  ]
})


export default router
