<template>
  <div class="butterfly-scene" aria-hidden="true">
    <div
      v-for="butterfly in butterflies"
      :key="butterfly.id"
      class="butterfly-tracker"
      :class="`flight-path-${butterfly.path}`"
      :style="{
        '--flight-duration': `${butterfly.duration}s`,
        '--flight-delay': `${butterfly.delay}s`,
        '--butterfly-scale': butterfly.scale,
        '--flutter-speed': `${butterfly.flapSpeed}s`
      }"
    >
      <div class="butterfly-body-wrapper">
        <!-- Delicate Sparkle Trail -->
        <div
          class="butterfly-stardust"
          :class="butterfly.color === 'white' ? 'stardust-white' : 'stardust-gold'"
        ></div>

        <!-- 3D Fluttering Butterfly -->
        <div class="butterfly-3d">
          <!-- Left Wings -->
          <div class="wing wing-left">
            <svg viewBox="0 0 50 60" class="wing-svg">
              <defs>
                <!-- Gold Gradient -->
                <linearGradient
                  v-if="butterfly.color !== 'white'"
                  :id="`wingGradLeft-${butterfly.id}`"
                  x1="0%"
                  y1="0%"
                  x2="100%"
                  y2="100%"
                >
                  <stop offset="0%" stop-color="#fff8db" />
                  <stop offset="35%" stop-color="#f59e0b" />
                  <stop offset="70%" stop-color="#d97706" />
                  <stop offset="100%" stop-color="#78350f" />
                </linearGradient>

                <!-- Pearlescent White Gradient -->
                <linearGradient
                  v-else
                  :id="`wingGradLeft-${butterfly.id}`"
                  x1="0%"
                  y1="0%"
                  x2="100%"
                  y2="100%"
                >
                  <stop offset="0%" stop-color="#ffffff" />
                  <stop offset="40%" stop-color="#f8fafc" />
                  <stop offset="75%" stop-color="#e2e8f0" />
                  <stop offset="100%" stop-color="#cbd5e1" />
                </linearGradient>
              </defs>
              <!-- Forewing -->
              <path
                d="M48 32 C40 10, 15 2, 2 12 C-4 22, 10 38, 48 34 Z"
                :fill="`url(#wingGradLeft-${butterfly.id})`"
                :stroke="butterfly.color === 'white' ? 'rgba(255, 255, 255, 0.95)' : 'rgba(255, 255, 255, 0.7)'"
                stroke-width="1.2"
              />
              <!-- Hindwing -->
              <path
                d="M48 34 C38 36, 12 42, 16 52 C20 60, 42 56, 48 36 Z"
                :fill="`url(#wingGradLeft-${butterfly.id})`"
                :stroke="butterfly.color === 'white' ? 'rgba(255, 255, 255, 0.85)' : 'rgba(255, 255, 255, 0.5)'"
                stroke-width="1.1"
                opacity="0.9"
              />
            </svg>
          </div>

          <!-- Central Body & Antennae -->
          <div class="butterfly-torso" :class="{ 'torso-white': butterfly.color === 'white' }">
            <div class="antennae antennae-left"></div>
            <div class="antennae antennae-right"></div>
            <div class="torso-core"></div>
          </div>

          <!-- Right Wings -->
          <div class="wing wing-right">
            <svg viewBox="0 0 50 60" class="wing-svg">
              <defs>
                <!-- Gold Gradient -->
                <linearGradient
                  v-if="butterfly.color !== 'white'"
                  :id="`wingGradRight-${butterfly.id}`"
                  x1="100%"
                  y1="0%"
                  x2="0%"
                  y2="100%"
                >
                  <stop offset="0%" stop-color="#fff8db" />
                  <stop offset="35%" stop-color="#f59e0b" />
                  <stop offset="70%" stop-color="#d97706" />
                  <stop offset="100%" stop-color="#78350f" />
                </linearGradient>

                <!-- Pearlescent White Gradient -->
                <linearGradient
                  v-else
                  :id="`wingGradRight-${butterfly.id}`"
                  x1="100%"
                  y1="0%"
                  x2="0%"
                  y2="100%"
                >
                  <stop offset="0%" stop-color="#ffffff" />
                  <stop offset="40%" stop-color="#f8fafc" />
                  <stop offset="75%" stop-color="#e2e8f0" />
                  <stop offset="100%" stop-color="#cbd5e1" />
                </linearGradient>
              </defs>
              <!-- Forewing -->
              <path
                d="M2 32 C10 10, 35 2, 48 12 C54 22, 40 38, 2 34 Z"
                :fill="`url(#wingGradRight-${butterfly.id})`"
                :stroke="butterfly.color === 'white' ? 'rgba(255, 255, 255, 0.95)' : 'rgba(255, 255, 255, 0.7)'"
                stroke-width="1.2"
              />
              <!-- Hindwing -->
              <path
                d="M2 34 C12 36, 38 42, 34 52 C30 60, 8 56, 2 36 Z"
                :fill="`url(#wingGradRight-${butterfly.id})`"
                :stroke="butterfly.color === 'white' ? 'rgba(255, 255, 255, 0.85)' : 'rgba(255, 255, 255, 0.5)'"
                stroke-width="1.1"
                opacity="0.9"
              />
            </svg>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  // 'white' | 'gold' | 'mixed'
  palette: {
    type: String,
    default: 'white'
  }
})

// Small, dainty butterflies tuned for natural garden flight around bottom flowers
const baseButterflies = [
  // 1. Dancing around left purple bouquet & flowers
  { id: 1, path: 1, duration: 11, delay: 0, scale: 0.22, flapSpeed: 0.14, defaultColor: 'white' },
  // 2. Hovering right above the center bouquet
  { id: 2, path: 2, duration: 13, delay: 3.5, scale: 0.19, flapSpeed: 0.15, defaultColor: 'white' },
  // 3. Circling right purple flowers & poppy blossoms
  { id: 3, path: 3, duration: 12, delay: 7.2, scale: 0.24, flapSpeed: 0.13, defaultColor: 'white' },
  // 4. Gliding smoothly across the flower garden
  { id: 4, path: 4, duration: 15, delay: 10.8, scale: 0.18, flapSpeed: 0.15, defaultColor: 'white' }
]

const butterflies = computed(() => {
  return baseButterflies.map(b => ({
    ...b,
    color: props.palette === 'mixed' ? b.defaultColor : props.palette
  }))
})
</script>

<style scoped>
.butterfly-scene {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: clamp(140px, 32vw, 220px);
  overflow: visible;
  pointer-events: none;
  z-index: 12;
}

.butterfly-tracker {
  position: absolute;
  bottom: 0;
  left: 0;
  will-change: transform, opacity;
  animation-iteration-count: infinite;
  animation-timing-function: cubic-bezier(0.42, 0, 0.58, 1);
  animation-duration: var(--flight-duration);
  animation-delay: var(--flight-delay);
}

.butterfly-body-wrapper {
  position: relative;
  transform: scale(var(--butterfly-scale));
  animation: gentleBob 1.2s ease-in-out infinite alternate;
}

/* 3D Butterfly Wings Container */
.butterfly-3d {
  display: flex;
  align-items: center;
  justify-content: center;
  perspective: 350px;
  transform-style: preserve-3d;
  filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.12))
          drop-shadow(0 0 6px rgba(255, 255, 255, 0.8));
}

/* Wings Fluttering */
.wing {
  width: 32px;
  height: 40px;
  transform-style: preserve-3d;
  will-change: transform;
}

.wing-svg {
  width: 100%;
  height: 100%;
  display: block;
}

.wing-left {
  transform-origin: right center;
  animation: flapLeft var(--flutter-speed) ease-in-out infinite alternate;
}

.wing-right {
  transform-origin: left center;
  animation: flapRight var(--flutter-speed) ease-in-out infinite alternate;
}

@keyframes flapLeft {
  0% {
    transform: rotateY(0deg);
  }
  100% {
    transform: rotateY(68deg);
  }
}

@keyframes flapRight {
  0% {
    transform: rotateY(0deg);
  }
  100% {
    transform: rotateY(-68deg);
  }
}

/* Torso & Antennae */
.butterfly-torso {
  width: 3px;
  height: 22px;
  position: relative;
  z-index: 2;
  margin: 0 -1.5px;
}

.torso-core {
  width: 100%;
  height: 100%;
  background: linear-gradient(to bottom, #78350f, #292524);
  border-radius: 3px;
}

.butterfly-torso.torso-white .torso-core {
  background: linear-gradient(to bottom, #cbd5e1, #64748b);
}

.antennae {
  position: absolute;
  top: -5px;
  width: 5px;
  height: 6px;
  border-top: 1.2px solid #78350f;
  border-radius: 50%;
}

.butterfly-torso.torso-white .antennae {
  border-top-color: #64748b;
}

.antennae-left {
  left: -3px;
  border-left: 1.2px solid #78350f;
  transform: rotate(-15deg);
}

.butterfly-torso.torso-white .antennae-left {
  border-left-color: #64748b;
}

.antennae-right {
  right: -3px;
  border-right: 1.2px solid #78350f;
  transform: rotate(15deg);
}

.butterfly-torso.torso-white .antennae-right {
  border-right-color: #64748b;
}

/* Delicate Fairy Stardust Trail */
.butterfly-stardust {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 2.5px;
  height: 2.5px;
  border-radius: 50%;
  animation: sparkleFlicker 0.45s ease-in-out infinite alternate;
}

.stardust-gold {
  background: radial-gradient(circle, #fef08a 0%, transparent 80%);
  box-shadow: 
    -3px 5px 4px rgba(254, 240, 138, 0.8),
    -6px 10px 7px rgba(245, 158, 11, 0.5);
}

.stardust-white {
  background: radial-gradient(circle, #ffffff 0%, transparent 80%);
  box-shadow: 
    -2px 4px 5px rgba(255, 255, 255, 0.95),
    -5px 8px 7px rgba(226, 232, 240, 0.7);
}

@keyframes gentleBob {
  0% { transform: translateY(-2px) rotate(-3deg); }
  100% { transform: translateY(2px) rotate(3deg); }
}

@keyframes sparkleFlicker {
  0% { opacity: 0.3; transform: scale(0.7); }
  100% { opacity: 1; transform: scale(1.2); }
}

/* ══════════════════════════════════════════════════════════════
   FLIGHT TRAJECTORIES SPECIFICALLY AROUND BOTTOM FLOWERS
   Coordinates are relative to bottom flowers
   ══════════════════════════════════════════════════════════════ */

.flight-path-1 {
  animation-name: flightAroundLeftFlowers;
}

.flight-path-2 {
  animation-name: flightAroundCenterBouquet;
}

.flight-path-3 {
  animation-name: flightAroundRightFlowers;
}

.flight-path-4 {
  animation-name: flightAcrossMeadow;
}

/* 1. Flutters around left floral bouquet */
@keyframes flightAroundLeftFlowers {
  0% {
    transform: translate3d(5vw, -60px, 0) rotate(8deg);
    opacity: 0;
  }
  12% { opacity: 0.95; }
  30% {
    transform: translate3d(16vw, -125px, 0) rotate(-10deg);
  }
  55% {
    transform: translate3d(25vw, -80px, 0) rotate(8deg);
  }
  75% {
    transform: translate3d(14vw, -95px, 0) rotate(-6deg);
  }
  90% { opacity: 0.95; }
  100% {
    transform: translate3d(5vw, -60px, 0) rotate(8deg);
    opacity: 0;
  }
}

/* 2. Dances and hovers right above the center bouquet */
@keyframes flightAroundCenterBouquet {
  0% {
    transform: translate3d(36vw, -85px, 0) rotate(-6deg);
    opacity: 0;
  }
  12% { opacity: 1; }
  35% {
    transform: translate3d(48vw, -145px, 0) rotate(10deg);
  }
  55% {
    transform: translate3d(58vw, -100px, 0) rotate(-8deg);
  }
  75% {
    transform: translate3d(44vw, -120px, 0) rotate(6deg);
  }
  90% { opacity: 1; }
  100% {
    transform: translate3d(36vw, -85px, 0) rotate(-6deg);
    opacity: 0;
  }
}

/* 3. Circles the right purple flower bouquet */
@keyframes flightAroundRightFlowers {
  0% {
    transform: translate3d(92vw, -70px, 0) scaleX(-1) rotate(-6deg);
    opacity: 0;
  }
  12% { opacity: 0.95; }
  32% {
    transform: translate3d(78vw, -135px, 0) scaleX(-1) rotate(12deg);
  }
  55% {
    transform: translate3d(68vw, -85px, 0) scaleX(-1) rotate(-6deg);
  }
  78% {
    transform: translate3d(84vw, -110px, 0) scaleX(-1) rotate(8deg);
  }
  90% { opacity: 0.95; }
  100% {
    transform: translate3d(92vw, -70px, 0) scaleX(-1) rotate(-6deg);
    opacity: 0;
  }
}

/* 4. Glides smoothly across the meadow dipping near blossoms */
@keyframes flightAcrossMeadow {
  0% {
    transform: translate3d(-6vw, -75px, 0) rotate(6deg);
    opacity: 0;
  }
  10% { opacity: 1; }
  28% {
    transform: translate3d(22vw, -115px, 0) rotate(-6deg);
  }
  50% {
    transform: translate3d(50vw, -85px, 0) rotate(8deg);
  }
  75% {
    transform: translate3d(75vw, -130px, 0) rotate(-8deg);
  }
  92% { opacity: 1; }
  100% {
    transform: translate3d(106vw, -80px, 0) rotate(4deg);
    opacity: 0;
  }
}
</style>
