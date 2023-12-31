<template>
  <div>
    <div id="container">
      <table id="lines">
        <tr v-for="(line, index) in lines" :key="index" class="verse">
          <td :id="`line-${index + 1}`" :class="{ highlight: index + 1 === parseInt(props.l) }">{{ line || '&nbsp;' }}
          </td>
        </tr>
      </table>
    </div>
    <div class="top"><a href="#"><img width="20" src="@/assets/up.svg" /></a></div>
  </div>
</template>
<script setup>
const highlight = (elementId) => {
  const intervalId = setInterval(function () {
    const element = document.getElementById(elementId);
    if (element) {
      clearInterval(intervalId);
      element.scrollIntoView({ behavior: 'smooth' });
      element.innerHTML = element.innerHTML.split(' ').map((word, i) => {
        return i + 1 === parseInt(props.w) ? `<span style="color:var(--P2)">${word}</span>` : word;
      }).join(' ');
    }
  }, 300);
};

import axios from 'axios';
import { defineProps, onMounted, ref } from 'vue';

const props = defineProps(['id', 'w', 'l']);
const lines = ref([]);
onMounted(async () => {
  const url = `/text/${props.id}.txt`;
  const response = await axios.get(url);
  lines.value = await response.data.split('\n');
  highlight(`line-${props.l}`, props.w);
});

</script>
<style scoped> #words {
   border-collapse: collapse;
   border: none;
 }

 #words tr {
   cursor: pointer;
 }

 #words tr td {
   padding: 0 0.4em;
 }

 #lines tr:nth-child(1) {
   font-size: 14pt;
   text-align: center;
 }

 .highlight {
   background-color: var(--B2);
   border-radius: 3pt;
 }
</style>
