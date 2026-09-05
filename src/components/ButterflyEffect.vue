<template>
  <div class="butterfly-effect-layer" aria-hidden="true">
    <div
      v-for="b in butterflies"
      :key="b.id"
      class="butterfly-tracker"
      :class="`flight-path-${b.path}`"
      :style="{
        '--flight-duration': `${b.duration}s`,
        '--flight-delay': `${b.delay}s`,
        '--scale': b.scale,
        '--flap-speed': `${b.flapSpeed}s`
      }"
    >
      <!-- Wrapper carries the scale -->
      <div class="butterfly-wrapper">
        <!-- Delicate Pollen Sparkles -->
        <div class="butterfly-stardust"></div>

        <!-- 3D Fluttering Butterfly Widget -->
        <div class="butterfly-widget">
          <!-- Left Wing (Forewing + Hindwing + Veins) -->
          <div class="wing wing-left">
            <svg viewBox="0 0 38 46" class="wing-svg">
              <defs>
                <linearGradient :id="`gradLeft-${b.id}`" x1="100%" y1="10%" x2="0%" y2="100%">
                  <stop offset="0%" stop-color="#ffffff" />
                  <stop offset="50%" stop-color="#faf5ff" />
                  <stop offset="80%" stop-color="#f3e8ff" />
                  <stop offset="100%" stop-color="#d8b4fe" />
                </linearGradient>
              </defs>
              <!-- Forewing -->
              <path
                d="M36 24 C30 5, 12 1, 2 8 C-3 16, 6 28, 36 26 Z"
                :fill="`url(#gradLeft-${b.id})`"
                stroke="rgba(255, 255, 255, 0.95)"
                stroke-width="0.9"
              />
              <!-- Hindwing -->
              <path
                d="M36 25 C28 27, 8 31, 12 40 C16 46, 32 42, 36 27 Z"
                :fill="`url(#gradLeft-${b.id})`"
                stroke="rgba(255, 255, 255, 0.9)"
                stroke-width="0.8"
                opacity="0.95"
              />
              <!-- Wing veins matching floral tone -->
              <path
                d="M36 25 C24 14, 12 12, 4 10 M36 25 C22 21, 11 23, 6 21 M36 26 C25 29, 17 35, 15 39"
                fill="none"
                stroke="rgba(216, 180, 254, 0.7)"
                stroke-width="0.7"
              />
            </svg>
          </div>

          <!-- Central Torso & Curved Antennae -->
          <div class="butterfly-torso">
            <div class="antennae antennae-left"></div>
            <div class="antennae antennae-right"></div>
            <div class="torso-core"></div>
          </div>

          <!-- Right Wing (Forewing + Hindwing + Veins) -->
          <div class="wing wing-right">
            <svg viewBox="0 0 38 46" class="wing-svg">
              <defs>
                <linearGradient :id="`gradRight-${b.id}`" x1="0%" y1="10%" x2="100%" y2="100%">
                  <stop offset="0%" stop-color="#ffffff" />
                  <stop offset="50%" stop-color="#faf5ff" />
                  <stop offset="80%" stop-color="#f3e8ff" />
                  <stop offset="100%" stop-color="#d8b4fe" />
                </linearGradient>
              </defs>
              <!-- Forewing -->
              <path
                d="M2 24 C8 5, 26 1, 36 8 C41 16, 32 28, 2 26 Z"
                :fill="`url(#gradRight-${b.id})`"
                stroke="rgba(255, 255, 255, 0.95)"
                stroke-width="0.9"
              />
              <!-- Hindwing -->
              <path
                d="M2 25 C10 27, 30 31, 26 40 C22 46, 6 42, 2 27 Z"
                :fill="`url(#gradRight-${b.id})`"
                stroke="rgba(255, 255, 255, 0.9)"
                stroke-width="0.8"
                opacity="0.95"
              />
              <!-- Wing veins matching floral tone -->
              <path
                d="M2 25 C14 14, 26 12, 34 10 M2 25 C16 21, 27 23, 32 21 M2 26 C13 29, 21 35, 23 39"
                fill="none"
                stroke="rgba(216, 180, 254, 0.7)"
                stroke-width="0.7"
              />
            </svg>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
// 8 dainty butterflies, visibly smaller than the flower blossoms
const butterflies = [
  // 1. Dipping into left purple bouquet
  { id: 1, path: 1, duration: 11.0, delay: 0.0, scale: 0.75, flapSpeed: 0.14 },
  // 2. Hovering over center centerpiece bouquet
  { id: 2, path: 3, duration: 12.5, delay: 4.2, scale: 0.80, flapSpeed: 0.15 },
  // 3. Flitting around right floral corner
  { id: 3, path: 6, duration: 11.8, delay: 1.8, scale: 0.70, flapSpeed: 0.13 },
  // 4. Dancing over left-center greenery
  { id: 4, path: 2, duration: 13.0, delay: 7.5, scale: 0.65, flapSpeed: 0.15 },
  // 5. Dipping into right-center poppies
  { id: 5, path: 5, duration: 12.2, delay: 9.8, scale: 0.75, flapSpeed: 0.14 },
  // 6. Fluttering slightly higher above center flowers
  { id: 6, path: 4, duration: 14.0, delay: 3.0, scale: 0.60, flapSpeed: 0.16 },
  // 7. Slow glider across meadow (left to right)
  { id: 7, path: 7, duration: 16.0, delay: 6.0, scale: 0.68, flapSpeed: 0.15 },
  // 8. Gentle glider across meadow (right to left)
  { id: 8, path: 8, duration: 17.0, delay: 11.5, scale: 0.65, flapSpeed: 0.14 }
]
</script>

<style scoped>
/* ── Container anchored to bottom flowers ── */
.butterfly-effect-layer {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: clamp(140px, 32vw, 220px);
  overflow: visible;
  pointer-events: none;
  z-index: 12;
}

/* ── Flight Tracker & Movement ── */
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

/* Base scale reliably applied here without animation conflict */
.butterfly-wrapper {
  position: relative;
  transform: scale(var(--scale, 0.7));
}

/* ── Butterfly Widget: Hover tilt animation runs here ── */
.butterfly-widget {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  perspective: 250px;
  transform-style: preserve-3d;
  cursor: pointer;
  filter: drop-shadow(0 1px 3px rgba(255, 255, 255, 0.95))
          drop-shadow(0 1.5px 3px rgba(168, 85, 247, 0.35));
  animation: hoverTilt 1.2s ease-in-out infinite alternate;
}

@keyframes hoverTilt {
  0%   { transform: translateY(-2px) rotate(-3deg); }
  100% { transform: translateY(2px) rotate(3deg); }
}

/* ── Wings: Truly smaller than flower blossoms (10px x 13px) ── */
.wing {
  width: 10px;
  height: 13px;
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
  animation: flapLeft var(--flap-speed, 0.14s) ease-in-out infinite alternate;
}

.wing-right {
  transform-origin: left center;
  animation: flapRight var(--flap-speed, 0.14s) ease-in-out infinite alternate;
}

@keyframes flapLeft {
  0%   { transform: rotateY(0deg); }
  100% { transform: rotateY(60deg); }
}

@keyframes flapRight {
  0%   { transform: rotateY(0deg); }
  100% { transform: rotateY(-60deg); }
}

/* ── Central Torso & Antennae (Miniature proportions) ── */
.butterfly-torso {
  width: 1.4px;
  height: 8.5px;
  position: relative;
  z-index: 2;
  margin: 0 -0.8px;
}

.torso-core {
  width: 100%;
  height: 100%;
  background: linear-gradient(to bottom, #a78bfa, #581c87);
  border-radius: 1.5px;
}

.antennae {
  position: absolute;
  top: -2.5px;
  width: 2.5px;
  height: 3px;
  border-top: 0.8px solid #7e22ce;
  border-radius: 50%;
}

.antennae-left {
  left: -1.5px;
  border-left: 0.8px solid #7e22ce;
  transform: rotate(-15deg);
}

.antennae-right {
  right: -1.5px;
  border-right: 0.8px solid #7e22ce;
  transform: rotate(15deg);
}

/* ── Delicate Pollen & Stardust Sparkles ── */
.butterfly-stardust {
  position: absolute;
  top: 55%;
  left: 50%;
  width: 1.8px;
  height: 1.8px;
  background: radial-gradient(circle, #ffffff 0%, #fef08a 60%, transparent 100%);
  border-radius: 50%;
  box-shadow:
    -2px 4px 3px rgba(255, 255, 255, 0.95),
    -4px 7px 5px rgba(233, 213, 255, 0.7),
    -8px 10px 6px rgba(192, 132, 252, 0.3);
  animation: sparkleFlicker 0.4s ease-in-out infinite alternate;
}

@keyframes sparkleFlicker {
  0%   { opacity: 0.3; transform: scale(0.7); }
  100% { opacity: 1; transform: scale(1.2); }
}

/* ══════════════════════════════════════════════════════════════
   FLIGHT TRAJECTORIES DISTRIBUTED ACROSS FLOWERS & DEPTHS
   ══════════════════════════════════════════════════════════════ */

.flight-path-1 { animation-name: flightLeftBouquet; }
.flight-path-2 { animation-name: flightLeftCenter; }
.flight-path-3 { animation-name: flightCenterBouquet; }
.flight-path-4 { animation-name: flightCenterHigh; }
.flight-path-5 { animation-name: flightRightCenter; }
.flight-path-6 { animation-name: flightRightCorner; }
.flight-path-7 { animation-name: flightCrossLeftRight; }
.flight-path-8 { animation-name: flightCrossRightLeft; }

/* 1. Dipping into left purple bouquet */
@keyframes flightLeftBouquet {
  0% {
    transform: translate3d(5vw, -80px, 0) rotate(8deg);
    opacity: 0;
  }
  15% { opacity: 0.95; }
  35% {
    transform: translate3d(14vw, -125px, 0) rotate(-10deg);
  }
  60% {
    transform: translate3d(20vw, -90px, 0) rotate(8deg);
  }
  80% {
    transform: translate3d(10vw, -105px, 0) rotate(-6deg);
  }
  90% { opacity: 0.95; }
  100% {
    transform: translate3d(5vw, -80px, 0) rotate(8deg);
    opacity: 0;
  }
}

/* 2. Left-center floral transition */
@keyframes flightLeftCenter {
  0% {
    transform: translate3d(18vw, -95px, 0) rotate(-6deg);
    opacity: 0;
  }
  15% { opacity: 0.95; }
  35% {
    transform: translate3d(27vw, -135px, 0) rotate(10deg);
  }
  65% {
    transform: translate3d(34vw, -100px, 0) rotate(-8deg);
  }
  85% {
    transform: translate3d(22vw, -115px, 0) rotate(6deg);
  }
  92% { opacity: 0.95; }
  100% {
    transform: translate3d(18vw, -95px, 0) rotate(-6deg);
    opacity: 0;
  }
}

/* 3. Center centerpiece bouquet */
@keyframes flightCenterBouquet {
  0% {
    transform: translate3d(38vw, -90px, 0) rotate(-6deg);
    opacity: 0;
  }
  15% { opacity: 1; }
  35% {
    transform: translate3d(49vw, -135px, 0) rotate(10deg);
  }
  60% {
    transform: translate3d(56vw, -100px, 0) rotate(-8deg);
  }
  80% {
    transform: translate3d(43vw, -120px, 0) rotate(6deg);
  }
  90% { opacity: 1; }
  100% {
    transform: translate3d(38vw, -90px, 0) rotate(-6deg);
    opacity: 0;
  }
}

/* 4. Center fluttering higher in air */
@keyframes flightCenterHigh {
  0% {
    transform: translate3d(42vw, -125px, 0) rotate(6deg);
    opacity: 0;
  }
  15% { opacity: 0.85; }
  40% {
    transform: translate3d(54vw, -165px, 0) rotate(-8deg);
  }
  70% {
    transform: translate3d(45vw, -140px, 0) rotate(6deg);
  }
  90% { opacity: 0.85; }
  100% {
    transform: translate3d(42vw, -125px, 0) rotate(6deg);
    opacity: 0;
  }
}

/* 5. Right-center poppies */
@keyframes flightRightCenter {
  0% {
    transform: translate3d(60vw, -85px, 0) rotate(8deg);
    opacity: 0;
  }
  15% { opacity: 0.95; }
  35% {
    transform: translate3d(69vw, -130px, 0) rotate(-10deg);
  }
  65% {
    transform: translate3d(76vw, -95px, 0) rotate(8deg);
  }
  85% {
    transform: translate3d(64vw, -110px, 0) rotate(-6deg);
  }
  92% { opacity: 0.95; }
  100% {
    transform: translate3d(60vw, -85px, 0) rotate(8deg);
    opacity: 0;
  }
}

/* 6. Right floral corner */
@keyframes flightRightCorner {
  0% {
    transform: translate3d(92vw, -85px, 0) scaleX(-1) rotate(-6deg);
    opacity: 0;
  }
  15% { opacity: 0.95; }
  35% {
    transform: translate3d(81vw, -125px, 0) scaleX(-1) rotate(12deg);
  }
  60% {
    transform: translate3d(73vw, -95px, 0) scaleX(-1) rotate(-8deg);
  }
  80% {
    transform: translate3d(85vw, -110px, 0) scaleX(-1) rotate(6deg);
  }
  90% { opacity: 0.95; }
  100% {
    transform: translate3d(92vw, -85px, 0) scaleX(-1) rotate(-6deg);
    opacity: 0;
  }
}

/* 7. Cross-meadow glider (left to right) */
@keyframes flightCrossLeftRight {
  0% {
    transform: translate3d(-5vw, -100px, 0) rotate(6deg);
    opacity: 0;
  }
  10% { opacity: 0.95; }
  30% {
    transform: translate3d(24vw, -135px, 0) rotate(-6deg);
  }
  50% {
    transform: translate3d(50vw, -105px, 0) rotate(8deg);
  }
  75% {
    transform: translate3d(76vw, -140px, 0) rotate(-8deg);
  }
  92% { opacity: 0.95; }
  100% {
    transform: translate3d(105vw, -100px, 0) rotate(4deg);
    opacity: 0;
  }
}

/* 8. Cross-meadow glider (right to left) */
@keyframes flightCrossRightLeft {
  0% {
    transform: translate3d(105vw, -95px, 0) scaleX(-1) rotate(6deg);
    opacity: 0;
  }
  10% { opacity: 0.95; }
  30% {
    transform: translate3d(74vw, -135px, 0) scaleX(-1) rotate(-6deg);
  }
  50% {
    transform: translate3d(47vw, -105px, 0) scaleX(-1) rotate(8deg);
  }
  75% {
    transform: translate3d(21vw, -140px, 0) scaleX(-1) rotate(-8deg);
  }
  92% { opacity: 0.95; }
  100% {
    transform: translate3d(-5vw, -95px, 0) scaleX(-1) rotate(4deg);
    opacity: 0;
  }
}
</style>
