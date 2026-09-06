<!--
  GoldDivider.vue
  An ornate luxury golden flourish divider line with filigree scrollwork and fleur-de-lis finials.
  Props:
    - variant: 'short' (default) | 'full'
    - design: 'flourish' (default, matches user reference) | 'ornate' (3D baroque)
-->
<template>
  <div class="gold-divider-wrap" :class="variant">
    <img
      :src="dividerSrc"
      class="gold-divider-flourish-img"
      alt="Golden Flourish Divider"
      draggable="false"
      decoding="async"
    />
  </div>
</template>

<script setup>
import { computed } from 'vue'
import flourishWebp from '@/assets/gold_divider_flourish.webp'
import ornateWebp from '@/assets/gold_divider_ornate.webp'

const props = defineProps({
  variant: { type: String, default: 'short' },
  design: { type: String, default: 'flourish' },
})

const dividerSrc = computed(() => {
  return props.design === 'ornate' ? ornateWebp : flourishWebp
})
</script>

<style scoped>
.gold-divider-wrap {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  margin: 0 auto;
  padding: 4px 0;
  pointer-events: none;
}

.gold-divider-flourish-img {
  width: clamp(145px, 42vw, 215px);
  height: auto;
  object-fit: contain;
  filter: drop-shadow(0 1px 2px rgba(180, 130, 30, 0.25));
  user-select: none;
  transition: transform 0.3s ease;
}

.gold-divider-wrap.full .gold-divider-flourish-img {
  width: clamp(200px, 58vw, 290px);
}

@media (min-width: 600px) {
  .gold-divider-flourish-img {
    width: clamp(210px, 32vw, 290px);
  }
  .gold-divider-wrap.full .gold-divider-flourish-img {
    width: clamp(280px, 45vw, 400px);
  }
}
</style>

