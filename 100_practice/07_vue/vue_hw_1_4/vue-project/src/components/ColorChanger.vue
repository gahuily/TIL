<script setup>
import { ref } from 'vue'

// 사용자의 입력을 저장할 반응형 변수 선언
const colorClass = ref('')
</script>

<template>
  <div>
    <!-- v-model을 사용해 input의 값과 colorClass 변수를 양방향으로 바인딩 -->
    <input type="text" v-model="colorClass">

    <!-- :class를 사용해 p 태그의 클래스를 colorClass 변수와 단방향으로 바인딩 -->
    <p :class="colorClass">입력창에 올바른 색상 명을 입력하면 글자색이 바껴요.</p>
  </div>
</template>

<style scoped>
/* 요구사항에 명시된 클래스들 */
.red {
  color: red;
}

.blue {
  color: blue;
}

.green {
  color: green;
}
</style>
