<!--
  FloatingPetals.vue
  Purely decorative CSS-animated floating petals layer.
  Fixed-position, pointer-events: none.
-->
<template>
  <div class="petals-layer" aria-hidden="true">
    <div
      v-for="p in petals"
      :key="p.id"
      class="petal"
      :style="{
        left:             p.left + '%',
        width:            p.size + 'px',
        height:           p.size * 0.62 + 'px',
        background:       p.color,
        animationDuration:  p.duration + 's',
        animationDelay:     p.delay + 's',
      }"
    />
  </div>
</template>

<script setup>
const COLORS = [
  'rgba(242,150,170,0.72)',
  'rgba(252,205,215,0.68)',
  'rgba(245,218,228,0.60)',
  'rgba(200,170,240,0.52)',
  'rgba(255,255,255,0.55)',
  'rgba(240,208,148,0.42)',
]

const petals = Array.from({ length: 24 }, (_, i) => ({
  id:       i,
  left:     Math.random() * 100,
  size:     6 + Math.random() * 14,
  color:    COLORS[Math.floor(Math.random() * COLORS.length)],
  duration: 10 + Math.random() * 14,
  delay:    -(Math.random() * 22),
}))
</script>

<style scoped>
.petals-layer {
  position: fixed;
  inset: 0;
  pointer-events: none;
  z-index: 0;
  overflow: hidden;
}

.petal {
  position: absolute;
  top: -40px;
  border-radius: 50% 0 50% 0;
  opacity: 0;
  animation: petalFall linear infinite;
  will-change: transform, opacity;
}
</style>
