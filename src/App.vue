<script setup>
import { RouterLink, RouterView } from 'vue-router';
import router from './router';

const goto = async (ev, dst) => {
  ev.target.className = 'flipper';
  setTimeout(async () => {
    await router.push(dst);
    ev.target.className = '';
  }, 50);
}
</script>

<template>
  <div>
    <header>
      <RouterLink to="/"><img src="@/assets/logo.svg" /></RouterLink>
    </header>
    <nav>
      <a href="#"><img src="@/assets/home.svg" @click="(e)=>goto(e,'/')" /></a>
      <a href="#"><img src="@/assets/help.svg" @click="(e)=>goto(e,'/about')" /></a>
    </nav>
  </div>
  <router-view v-slot="{ Component }">
    <keep-alive include="HomeView">
      <component :is="Component" />
    </keep-alive>
  </router-view>
</template>

<style scoped>
.flipper {
  animation: flip-animation 1s infinite;
}

@keyframes flip-animation {
  0% {
    transform: scaleX(1);
  }

  50% {
    transform: scaleX(-1);
  }

  100% {
    transform: scaleX(1);
  }
}
</style>
