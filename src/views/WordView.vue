<template>
  <div>
    <div style="text-align: end; font-size: 8pt; margin-top: 2em; margin-left: 2em;">
      <label for="switch">مصرع</label>
      <label class="checkbox-slider">
        <input type="checkbox" id="switch" :checked="showSingleLine" @click="showSingleLine = !showSingleLine">
        <div class="slider-track">
          <div class="slider-thumb"></div>
        </div>
      </label>
      <label for="switch">شعر</label>
    </div>
    <div id="container">
      <div style="overflow-x: auto;">
        <table>
          <thead>
            <tr>
              <th>&nbsp;</th>
              <th id="title">{{ word }}</th>
              <th>&nbsp;</th>
            </tr>
          </thead>
          <tbody id="words" :class="{ single: showSingleLine }">
            <template v-for="(entry, index) in entries" :key="index">
              <tr class="word other" v-if="!entry.first && entry.other"
                @click.stop="showPoem(entry.file, entry.line, entry.before)">
                <td class="other" colspan="3">{{ entry.other }}</td>
              </tr>
              <tr class="word" @click.stop="showPoem(entry.file, entry.line, entry.before)">
                <td>{{ entry.before || '&nbsp;' }}</td>
                <td>{{ entry.word }}</td>
                <td>{{ entry.after || '&nbsp;' }}</td>
              </tr>
              <tr class="word other" v-if="entry.first && entry.other"
                @click.stop="showPoem(entry.file, entry.line, entry.before)">
                <td class="other" colspan="3">{{ entry.other }}</td>
              </tr>
              <tr class="spacer other">
                <td colspan="3">&nbsp;</td>
              </tr>
            </template>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>
<script setup>

import axios from 'axios';
import { defineProps, onMounted, ref } from 'vue';
import { useRouter } from 'vue-router';

const props = defineProps(['word']);
const entries = ref([]);
const showSingleLine = ref(true);
const router = useRouter();

onMounted(async () => {
  try {
  const url = `/words/${props.word[0]}/${props.word}.json`;
  const response = await axios.get(url);
  entries.value = await response.data;

} catch (error) {
  console.error('Error downloading JSON:', error);
}
});


const showPoem = (file, line, before) => {
  router.push({
    name: 'poem',
    params: { id: file, l: line, w: before.split(' ').length + 1 },
  });
};

</script>
<style scoped> table {
   border-collapse: collapse;
 }

 #words {
   width: max-content;
   -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
 }

 #words tr {
   cursor: pointer;
 }


 #words td {
   white-space: nowrap;
 }

 #words tr td:nth-child(1) {
   text-align: end;
 }

 #words tr td:nth-child(2) {
   color: var(--P2);
   text-align: center;
 }

 #title {
   color: black !important;
   background-color: none !important;
   font-size: 13pt;
   cursor: default !important;
   padding-bottom: 1em;
 }

 #words tr td:nth-child(1).other {
   text-align: center;
 }

 #words tr.other {
   transition: all 0.2s ease;
 }

 #words tr.spacer {
   font-size: 0.5em;
 }


 #words.single tr.other {
   font-size: 0;
 }

 .hidden {
   display: none;
 }

 label {
   direction: rtl;
   font-family: "Noto Nastaliq Urdu", Arial, sans-serif;
   font-size: 10pt;
   margin: 0 2pt;
   cursor: pointer;
 }

 /* The slider container */
 .checkbox-slider {
   position: relative;
   display: inline-block;
   width: 24px;
   height: 11px;
   vertical-align: middle;
 }

 /* The checkbox input */
 .checkbox-slider input {
   opacity: 0;
   width: 0;
   height: 0;
 }

 /* The slider track */
 .slider-track {
   position: absolute;
   cursor: pointer;
   top: 0;
   left: 0;
   right: 0;
   bottom: 0;
   -webkit-transition: .4s;
   transition: .4s;
   border: 1px solid var(--P2);
   border-radius: 5px;
 }

 /* Style for the slider's thumb (circle) */
 .slider-thumb {
   position: absolute;
   content: "";
   height: 7px;
   width: 7px;
   left: 2px;
   bottom: 1px;
   background-color: white;
   -webkit-transition: .4s;
   transition: .4s;
   border-radius: 5px;
   background-color: var(--P2);
 }


 /* Move the thumb to the right (on) when the input is checked */
 input:checked+.slider-track .slider-thumb {
   -webkit-transform: translateX(9px);
   -ms-transform: translateX(9px);
   transform: translateX(11px);
 }
</style>
