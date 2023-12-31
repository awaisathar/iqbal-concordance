<template>
  <div v-once>
    <ul id="index" class="letter">
      <li v-for="(letter, index) in letters" @click="scrollToWordList(letter)" :key="index">{{ letter }}</li>
    </ul>

    <div class="top"><a href="#"><img width="20" src="@/assets/up.svg"></a></div>

    <div v-for="(words, letter) in wordStartingWith" :key="letter">
      <div class="title" :id="`letter-${letter}`">{{ letter }}</div>
      <ul class="letter">
        <li v-for="(word, index) in words" :key="index">
          <RouterLink :to="`/word/${word}`">{{ word }}</RouterLink>
        </li>
      </ul>
      <div class="top"><a href="#"><img width="20" src="@/assets/up.svg"></a></div>
    </div>
  </div>
</template>


<script setup>
import { ref } from 'vue';
import words from '@/assets/words.json';
const letters = ref([]);
const wordStartingWith = ref({});
const l2w = {};
words.forEach(word => {
  const letter = word[0];
  if (!l2w[letter]) {
    l2w[letter] = [];
  }
  l2w[letter].push(word);
});
wordStartingWith.value = l2w;
letters.value = Object.keys(l2w);


const scrollToWordList = (letter) => {
  const element = document.getElementById(`letter-${letter}`);
  element.scrollIntoView({ behavior: 'smooth' });
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
</style>