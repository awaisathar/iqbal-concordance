<template>
  <div style="font-size: 10pt; padding: 0.5em">
    <div style="color: var(--P2); font-size: 12pt;">کشف الالفاظ استعمال کرنے کا طریقہ</div>
    <ul>
      <li>کسی حرف پر کلک کر کے اس سے شروع ہونے والے الفاظ کی فہرست دیکھیں۔ </li>
      <li>کسی لفظ پر کلک کر کے اس پر مشتمل شعر/مصرعے دیکھیں۔</li>
      <li>کسی شعر یا مصرع پر کلک کر کے پوری نظم/غزل/قطعہ دیکھیں۔</li>
      <li>فہرست دیکھنے کے لیے <a href="/"><img width="16" src="@/assets/home.svg" /></a> پر کلک کریں۔ </li>
      <li>اس سائٹ پر کام جاری ہے اور تمام ٹیکسٹ اوپن سورس ہے۔ فرمائشوں کے لیے
        <a href="https://github.com/awaisathar/iqbal-concordance">گِٹ ہَب</a>
        پر نیا ایشو بنائیں۔اور اگر متن درست کر کے پُل ریکویسٹ ڈال دیں تو کیا ہی بات ہو!
      </li>
    </ul>
  </div>
</template>

<script setup>
</script>
<style scoped>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}

a {
  color: var(--P2);
}
</style>
