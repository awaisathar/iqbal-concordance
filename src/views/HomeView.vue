<template>
  <div>
    <!-- Sorting Toggle -->
    <div style="text-align: end; font-size: 12pt; margin-top: 2em; margin-left: 2em;">
      <label for="sortToggle">تعددی </label>
      <label class="checkbox-slider">
        <input type="checkbox" id="sortToggle" v-model="sortByFrequency">
        <div class="slider-track">
          <div class="slider-thumb"></div>
        </div>
      </label>
      <label for="sortToggle">لفظی</label>
    </div>

    <!-- Letter Navigation -->
    <ul id="index" class="letter">
      <li v-for="(letter, index) in letters" @click="scrollToWordList(letter)" :key="index">{{ letter }}</li>
    </ul>

    <div class="top"><a href="#"><img width="20" src="@/assets/up.svg"></a></div>

    <!-- Sorted Words View -->
    <div v-for="(words, letter) in sortedWords" :key="letter">
      <div class="title" :id="`letter-${letter}`">{{ letter }}</div>
      <ul class="letter">
        <li v-for="wordObj in words" :key="wordObj.word">
          <RouterLink :to="`/word/${wordObj.word}`">
            {{ wordObj.word }}
            <!-- Conditionally display the frequency -->
            <span v-if="sortByFrequency">{{ ' (' + wordObj.frequency + ')' }}</span>
          </RouterLink>
        </li>
      </ul>
      <div class="top"><a href="#"><img width="20" src="@/assets/up.svg"></a></div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';
import wordsWithFrequencies from '@/assets/words.json';

const letters = ref([]);
const wordStartingWith = ref({});
const sortByFrequency = ref(false); // Controls sorting mode

// Organize words by their starting letter and include frequency
Object.entries(wordsWithFrequencies).forEach(([word, { frequency }]) => {
  const letter = word[0];
  if (!wordStartingWith.value[letter]) {
    wordStartingWith.value[letter] = [];
  }
  wordStartingWith.value[letter].push({ word, frequency });
});

letters.value = Object.keys(wordStartingWith.value).sort((a, b) => a.localeCompare(b));

// Compute sorted words based on toggle state
const sortedWords = computed(() => {
  let sorted = {};
  for (const [letter, words] of Object.entries(wordStartingWith.value)) {
    sorted[letter] = sortByFrequency.value
      ? [...words].sort((a, b) => b.frequency - a.frequency)
      : [...words].sort((a, b) => a.word.localeCompare(b.word));
  }
  return sorted;
});

const scrollToWordList = (letter) => {
  const element = document.getElementById(`letter-${letter}`);
  element?.scrollIntoView({ behavior: 'smooth' });
};
</script>


<style scoped>
ul#index {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
}

ul li {
  padding: 0 0.5em;
  text-align: center;
  cursor: pointer;
}

ul#index li a {
  display: block;
}

.word {
  cursor: pointer;
  margin-bottom: 5px;
  color: var(--B1);
}

.words {
  display: none;
  margin-left: 20px;
}

.letter {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  list-style-type: none;
}

.letter li {
  min-width: max-content;
}

.title {
  text-align: center;
  font-size: 16pt;
}

@media only screen and (max-device-width: 480px) {
  .title {
    font-size: 14pt;
  }
}

@media only screen and (max-device-width: 480px) {
  .title {
    font-size: 12pt;
  }
}


.word:hover,
.letter li:hover {
  background-color: var(--B2);
  border-radius: 5pt;
}

#container {
  display: block;
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