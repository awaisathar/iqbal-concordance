<script setup>
import { RouterLink, RouterView } from 'vue-router';
</script>

<template>
  <div>
    <header>
      <RouterLink to="/"><img src="@/assets/logo.svg" /></RouterLink>
    </header>
    <nav>
      <RouterLink to="/"><img src="@/assets/home.svg" class="flip-on-click" /></RouterLink>
      <RouterLink to="/about"><img src="@/assets/help.svg"  class="flip-on-click" /></RouterLink>
    </nav>
  </div>
  <router-view v-slot="{ Component }">
    <keep-alive include="HomeView">
      <component :is="Component" />
    </keep-alive>
  </router-view>
</template>

<style scoped>
.flip-on-click {
  transition: transform 0.5s;
}

.flip-on-click:active {
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
}</style>
