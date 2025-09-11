<script setup>
// 1. 생성한 ColorChanger 컴포넌트를 import 합니다.
import ColorChanger from './components/ColorChanger.vue'
</script>

<template>
  <header>
    <h1>글자색 바꾸기</h1>
  </header>

  <main>
    <!-- 2. 불러온 컴포넌트를 템플릿 안에서 사용합니다. -->
    <ColorChanger />
  </main>
</template>

<style scoped>
/* 기본 스타일링 (선택사항) */
header {
  line-height: 1.5;
}
</style>
