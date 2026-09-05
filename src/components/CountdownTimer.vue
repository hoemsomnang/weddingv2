<!--
  CountdownTimer.vue
  Live countdown to a target date. Updates every second.
  Props:
    - targetDate: String  (ISO date string, e.g. '2026-11-24T08:00:00')
-->
<template>
  <div class="countdown" role="timer" aria-live="polite">
    <template v-for="(unit, idx) in units" :key="unit.label">
      <div class="unit">
        <span class="num">{{ unit.value }}</span>
        <span class="unit-label">{{ unit.label }}</span>
      </div>
      <span v-if="idx < units.length - 1" class="sep" aria-hidden="true">:</span>
    </template>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import invitation from '@/config/invitation.js'

const props = defineProps({
  targetDate: { type: String, required: true },
})

const now = ref(Date.now())
let timer = null

onMounted(() => { timer = setInterval(() => { now.value = Date.now() }, 1000) })
onUnmounted(() => clearInterval(timer))

function pad(n) { return String(Math.max(0, n)).padStart(2, '0') }

const labels = invitation.countdownLabels || {
  days: 'Days',
  hours: 'Hours',
  mins: 'Mins',
  secs: 'Secs',
}

const units = computed(() => {
  const diff = new Date(props.targetDate) - now.value
  if (diff <= 0) return [
    { label: labels.days,  value: '00' }, { label: labels.hours, value: '00' },
    { label: labels.mins,  value: '00' }, { label: labels.secs,  value: '00' },
  ]
  return [
    { label: labels.days,  value: pad(Math.floor(diff / 86400000)) },
    { label: labels.hours, value: pad(Math.floor((diff % 86400000) / 3600000)) },
    { label: labels.mins,  value: pad(Math.floor((diff % 3600000)  / 60000)) },
    { label: labels.secs,  value: pad(Math.floor((diff % 60000)    / 1000)) },
  ]
})
</script>

<style scoped>
.countdown {
  display: flex;
  align-items: flex-start;
  gap: clamp(10px, 2.5vw, 22px);
}

.unit {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 4px;
  min-width: 11vw;           /* ~44px on 400px phone */
}

.num {
  font-family: var(--font-cap);
  font-size: 7vw;            /* ~28px on 400px phone */
  font-weight: 700;
  line-height: 1;
  background: var(--gold-gradient);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}
.num::after {
  content: '';
  display: block;
  height: 2px;
  margin-top: 5px;
  background: linear-gradient(90deg, transparent, var(--gold-mid), transparent);
  border-radius: 2px;
}

.unit-label {
  font-family: var(--font-cap);
  font-size: 2.5vw;          /* ~10px on 400px phone */
  letter-spacing: 2px;
  text-transform: uppercase;
  color: var(--text-lt);
}

.sep {
  font-family: var(--font-cap);
  font-size: 6vw;            /* ~24px on 400px phone */
  font-weight: 700;
  background: var(--gold-gradient);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  align-self: flex-start;
  margin-top: 3px;
  padding-bottom: 18px;
}
</style>
