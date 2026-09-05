<!--
  GoldDivider.vue
  A decorative golden divider line with diamond/dot accents.
  Props:
    - variant: 'full' (default) | 'short'
-->
<template>
  <div class="gold-divider" :class="variant">
    <div class="line" />
    <div class="dot" />
    <div v-if="variant !== 'short'" class="diamond" />
    <div class="dot" />
    <div class="line" />
  </div>
</template>

<script setup>
defineProps({
  variant: { type: String, default: 'full' },
})
</script>

<style scoped>
.gold-divider {
  display: flex;
  align-items: center;
  gap: 10px;
  width: clamp(220px, 60%, 440px);
  margin: 0 auto;
}

.gold-divider.short { width: clamp(140px, 40%, 260px); }

.line {
  flex: 1;
  height: 1px;
  background: linear-gradient(90deg, transparent, var(--gold-mid), transparent);
}

.diamond {
  width: 7px;
  height: 7px;
  background: var(--gold-gradient);
  transform: rotate(45deg);
  flex-shrink: 0;
}

.dot {
  width: 4px;
  height: 4px;
  border-radius: 50%;
  background: var(--gold-mid);
  flex-shrink: 0;
}
</style>
