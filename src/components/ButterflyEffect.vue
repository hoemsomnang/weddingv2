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
                  <stop offset="45%" stop-color="#faf5ff" />
                  <stop offset="75%" stop-color="#f3e8ff" />
                  <stop offset="100%" stop-color="#c084fc" />
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
                stroke="rgba(192, 132, 252, 0.65)"
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
                  <stop offset="45%" stop-color="#faf5ff" />
                  <stop offset="75%" stop-color="#f3e8ff" />
                  <stop offset="100%" stop-color="#c084fc" />
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
                stroke="rgba(192, 132, 252, 0.65)"
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
// Graceful butterflies distributed across the whole invitation page
const butterflies = [
  // 1. Bottom meadow ascending to gazebo fountain and spiraling
  { id: 1,  path: 1,  duration: 18.0, delay: 0.0,  scale: 0.72, flapSpeed: 0.13 },
  // 2. Upper canopy wisteria dipping down past Khmer greeting & Save The Date
  { id: 2,  path: 2,  duration: 19.5, delay: 2.5,  scale: 0.78, flapSpeed: 0.14 },
  // 3. Full-page diagonal sweep: Bottom-Right to Upper-Left past countdown
  { id: 3,  path: 3,  duration: 22.0, delay: 5.0,  scale: 0.65, flapSpeed: 0.15 },
  // 4. Full-page diagonal sweep: Upper-Right to Lower-Left past gazebo pillars
  { id: 4,  path: 4,  duration: 23.5, delay: 8.0,  scale: 0.68, flapSpeed: 0.14 },
  // 5. Elegant figure-8 dance around gazebo rotunda and fountain
  { id: 5,  path: 5,  duration: 16.5, delay: 1.0,  scale: 0.75, flapSpeed: 0.13 },
  // 6. High sky flight across golden sunburst and top wisteria bridge
  { id: 6,  path: 6,  duration: 19.0, delay: 4.0,  scale: 0.60, flapSpeed: 0.15 },
  // 7. Middle page gentle S-curve drift across the countdown numbers
  { id: 7,  path: 7,  duration: 20.5, delay: 10.5, scale: 0.70, flapSpeed: 0.14 },
  // 8. Right floral edge spire climb up towards date and venue block
  { id: 8,  path: 8,  duration: 17.5, delay: 6.5,  scale: 0.65, flapSpeed: 0.14 },
  // 9. Left floral edge spire climb up towards Khmer subtitle
  { id: 9,  path: 9,  duration: 18.5, delay: 12.0, scale: 0.66, flapSpeed: 0.13 },
  // 10. Expansive whole-page wandering butterfly visiting all 4 quadrants
  { id: 10, path: 10, duration: 25.0, delay: 3.5,  scale: 0.74, flapSpeed: 0.14 },
  // 11. Low playful meadow flutter across bottom poppies and wildflowers
  { id: 11, path: 11, duration: 15.0, delay: 7.0,  scale: 0.72, flapSpeed: 0.15 },
  // 12. Top wisteria reverse canopy glider (right to left)
  { id: 12, path: 12, duration: 21.0, delay: 14.0, scale: 0.62, flapSpeed: 0.15 },
]
</script>

<style scoped>
/* ── Container covers the entire invitation page ── */
.butterfly-effect-layer {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  overflow: hidden;
  pointer-events: none;
  z-index: 6; /* Floats gracefully in front of gazebo rotunda & typography */
}

/* ── Flight Tracker: Positioned from top-left for full-page (vw, vh) coordinates ── */
.butterfly-tracker {
  position: absolute;
  top: 0;
  left: 0;
  will-change: transform, opacity;
  animation-iteration-count: infinite;
  animation-timing-function: cubic-bezier(0.42, 0, 0.58, 1);
  animation-duration: var(--flight-duration);
  animation-delay: var(--flight-delay);
}

/* Base scale reliably applied without animation conflict */
.butterfly-wrapper {
  position: relative;
  transform: scale(var(--scale, 0.7));
}

/* ── Butterfly Widget: Hover tilt animation ── */
.butterfly-widget {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  perspective: 260px;
  transform-style: preserve-3d;
  filter: drop-shadow(0 1px 4px rgba(255, 255, 255, 0.95))
          drop-shadow(0 2px 6px rgba(168, 85, 247, 0.38));
  animation: hoverTilt 1.2s ease-in-out infinite alternate;
}

@keyframes hoverTilt {
  0%   { transform: translateY(-2px) rotate(-3deg); }
  100% { transform: translateY(2px) rotate(3deg); }
}

/* ── Wings: Fine dainty proportion ── */
.wing {
  width: 11px;
  height: 14px;
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
  100% { transform: rotateY(62deg); }
}

@keyframes flapRight {
  0%   { transform: rotateY(0deg); }
  100% { transform: rotateY(-62deg); }
}

/* ── Central Torso & Curved Antennae ── */
.butterfly-torso {
  width: 1.5px;
  height: 9px;
  position: relative;
  z-index: 2;
  margin: 0 -0.8px;
}

.torso-core {
  width: 100%;
  height: 100%;
  background: linear-gradient(to bottom, #c084fc, #581c87);
  border-radius: 1.5px;
}

.antennae {
  position: absolute;
  top: -2.8px;
  width: 2.8px;
  height: 3.2px;
  border-top: 0.9px solid #7e22ce;
  border-radius: 50%;
}

.antennae-left {
  left: -1.6px;
  border-left: 0.9px solid #7e22ce;
  transform: rotate(-15deg);
}

.antennae-right {
  right: -1.6px;
  border-right: 0.9px solid #7e22ce;
  transform: rotate(15deg);
}

/* ── Delicate Fairy Dust Sparkles Trailing ── */
.butterfly-stardust {
  position: absolute;
  top: 55%;
  left: 50%;
  width: 2px;
  height: 2px;
  background: radial-gradient(circle, #ffffff 0%, #fef08a 60%, transparent 100%);
  border-radius: 50%;
  box-shadow:
    -2px 4px 4px rgba(255, 255, 255, 0.95),
    -5px 8px 6px rgba(233, 213, 255, 0.75),
    -9px 12px 7px rgba(192, 132, 252, 0.35);
  animation: sparkleFlicker 0.4s ease-in-out infinite alternate;
}

@keyframes sparkleFlicker {
  0%   { opacity: 0.3; transform: scale(0.7); }
  100% { opacity: 1; transform: scale(1.3); }
}

/* ══════════════════════════════════════════════════════════════
   FLIGHT TRAJECTORIES ACROSS THE ENTIRE PAGE
   ══════════════════════════════════════════════════════════════ */

.flight-path-1  { animation-name: pathMeadowToGazebo; }
.flight-path-2  { animation-name: pathCanopyToGreeting; }
.flight-path-3  { animation-name: pathBottomRightToTopLeft; }
.flight-path-4  { animation-name: pathTopRightToBottomLeft; }
.flight-path-5  { animation-name: pathGazeboFigureEight; }
.flight-path-6  { animation-name: pathSkylineSunburst; }
.flight-path-7  { animation-name: pathMidPageSCurve; }
.flight-path-8  { animation-name: pathRightSpireAscent; }
.flight-path-9  { animation-name: pathLeftSpireAscent; }
.flight-path-10 { animation-name: pathWholePageWander; }
.flight-path-11 { animation-name: pathBottomMeadowHover; }
.flight-path-12 { animation-name: pathTopCanopyGlider; }

/* 1. Meadow ascending past gazebo fountain and spiraling */
@keyframes pathMeadowToGazebo {
  0% {
    transform: translate3d(8vw, 90vh, 0) rotate(12deg);
    opacity: 0;
  }
  10% { opacity: 1; }
  28% {
    transform: translate3d(22vw, 72vh, 0) rotate(-8deg);
  }
  48% {
    transform: translate3d(48vw, 56vh, 0) rotate(10deg);
  }
  65% {
    transform: translate3d(58vw, 52vh, 0) rotate(-6deg);
  }
  80% {
    transform: translate3d(42vw, 68vh, 0) rotate(8deg);
  }
  92% { opacity: 1; }
  100% {
    transform: translate3d(28vw, 88vh, 0) rotate(-10deg);
    opacity: 0;
  }
}

/* 2. Top canopy wisteria dipping down past Khmer greeting & Save The Date */
@keyframes pathCanopyToGreeting {
  0% {
    transform: translate3d(12vw, 8vh, 0) rotate(15deg);
    opacity: 0;
  }
  12% { opacity: 1; }
  30% {
    transform: translate3d(44vw, 14vh, 0) rotate(-6deg);
  }
  50% {
    transform: translate3d(54vw, 25vh, 0) rotate(12deg);
  }
  70% {
    transform: translate3d(36vw, 32vh, 0) rotate(-10deg);
  }
  88% {
    transform: translate3d(78vw, 12vh, 0) rotate(8deg);
    opacity: 1;
  }
  100% {
    transform: translate3d(88vw, 6vh, 0) rotate(12deg);
    opacity: 0;
  }
}

/* 3. Full-page diagonal sweep: Bottom-Right to Upper-Left past countdown */
@keyframes pathBottomRightToTopLeft {
  0% {
    transform: translate3d(90vw, 92vh, 0) scaleX(-1) rotate(10deg);
    opacity: 0;
  }
  10% { opacity: 1; }
  30% {
    transform: translate3d(70vw, 65vh, 0) scaleX(-1) rotate(-8deg);
  }
  55% {
    transform: translate3d(45vw, 42vh, 0) scaleX(-1) rotate(12deg);
  }
  78% {
    transform: translate3d(24vw, 22vh, 0) scaleX(-1) rotate(-6deg);
  }
  92% { opacity: 1; }
  100% {
    transform: translate3d(8vw, 10vh, 0) scaleX(-1) rotate(8deg);
    opacity: 0;
  }
}

/* 4. Full-page diagonal sweep: Upper-Right to Lower-Left past gazebo pillars */
@keyframes pathTopRightToBottomLeft {
  0% {
    transform: translate3d(92vw, 12vh, 0) scaleX(-1) rotate(-10deg);
    opacity: 0;
  }
  10% { opacity: 1; }
  32% {
    transform: translate3d(56vw, 30vh, 0) scaleX(-1) rotate(8deg);
  }
  58% {
    transform: translate3d(26vw, 58vh, 0) scaleX(-1) rotate(-12deg);
  }
  80% {
    transform: translate3d(14vw, 84vh, 0) scaleX(-1) rotate(6deg);
  }
  92% { opacity: 1; }
  100% {
    transform: translate3d(5vw, 94vh, 0) scaleX(-1) rotate(-8deg);
    opacity: 0;
  }
}

/* 5. Elegant figure-8 dance around gazebo rotunda and fountain */
@keyframes pathGazeboFigureEight {
  0% {
    transform: translate3d(32vw, 54vh, 0) rotate(8deg);
    opacity: 0;
  }
  12% { opacity: 1; }
  25% {
    transform: translate3d(50vw, 48vh, 0) rotate(-10deg);
  }
  45% {
    transform: translate3d(68vw, 56vh, 0) rotate(12deg);
  }
  65% {
    transform: translate3d(50vw, 64vh, 0) rotate(-8deg);
  }
  85% {
    transform: translate3d(30vw, 58vh, 0) rotate(10deg);
  }
  94% { opacity: 1; }
  100% {
    transform: translate3d(32vw, 54vh, 0) rotate(8deg);
    opacity: 0;
  }
}

/* 6. High sky flight across golden sunburst and top wisteria bridge */
@keyframes pathSkylineSunburst {
  0% {
    transform: translate3d(-5vw, 10vh, 0) rotate(8deg);
    opacity: 0;
  }
  12% { opacity: 1; }
  30% {
    transform: translate3d(28vw, 6vh, 0) rotate(-6deg);
  }
  52% {
    transform: translate3d(52vw, 12vh, 0) rotate(10deg);
  }
  75% {
    transform: translate3d(76vw, 7vh, 0) rotate(-8deg);
  }
  92% { opacity: 1; }
  100% {
    transform: translate3d(105vw, 11vh, 0) rotate(6deg);
    opacity: 0;
  }
}

/* 7. Middle page gentle S-curve drift across the countdown numbers */
@keyframes pathMidPageSCurve {
  0% {
    transform: translate3d(-5vw, 36vh, 0) rotate(6deg);
    opacity: 0;
  }
  10% { opacity: 1; }
  28% {
    transform: translate3d(26vw, 32vh, 0) rotate(-8deg);
  }
  50% {
    transform: translate3d(50vw, 42vh, 0) rotate(10deg);
  }
  72% {
    transform: translate3d(74vw, 34vh, 0) rotate(-6deg);
  }
  92% { opacity: 1; }
  100% {
    transform: translate3d(105vw, 40vh, 0) rotate(8deg);
    opacity: 0;
  }
}

/* 8. Right floral edge spire climb up towards date and venue block */
@keyframes pathRightSpireAscent {
  0% {
    transform: translate3d(92vw, 86vh, 0) scaleX(-1) rotate(-8deg);
    opacity: 0;
  }
  12% { opacity: 1; }
  32% {
    transform: translate3d(84vw, 62vh, 0) scaleX(-1) rotate(10deg);
  }
  55% {
    transform: translate3d(72vw, 40vh, 0) scaleX(-1) rotate(-8deg);
  }
  76% {
    transform: translate3d(85vw, 55vh, 0) scaleX(-1) rotate(10deg);
  }
  90% { opacity: 1; }
  100% {
    transform: translate3d(92vw, 86vh, 0) scaleX(-1) rotate(-8deg);
    opacity: 0;
  }
}

/* 9. Left floral edge spire climb up towards Khmer subtitle */
@keyframes pathLeftSpireAscent {
  0% {
    transform: translate3d(8vw, 86vh, 0) rotate(8deg);
    opacity: 0;
  }
  12% { opacity: 1; }
  32% {
    transform: translate3d(16vw, 60vh, 0) rotate(-10deg);
  }
  55% {
    transform: translate3d(28vw, 38vh, 0) rotate(8deg);
  }
  76% {
    transform: translate3d(15vw, 52vh, 0) rotate(-10deg);
  }
  90% { opacity: 1; }
  100% {
    transform: translate3d(8vw, 86vh, 0) rotate(8deg);
    opacity: 0;
  }
}

/* 10. Expansive whole-page wandering butterfly visiting all 4 quadrants */
@keyframes pathWholePageWander {
  0% {
    transform: translate3d(20vw, 82vh, 0) rotate(10deg);
    opacity: 0;
  }
  8% { opacity: 1; }
  25% {
    transform: translate3d(76vw, 62vh, 0) rotate(-12deg);
  }
  48% {
    transform: translate3d(65vw, 22vh, 0) rotate(8deg);
  }
  68% {
    transform: translate3d(22vw, 28vh, 0) rotate(-10deg);
  }
  88% {
    transform: translate3d(45vw, 75vh, 0) rotate(12deg);
    opacity: 1;
  }
  100% {
    transform: translate3d(20vw, 82vh, 0) rotate(10deg);
    opacity: 0;
  }
}

/* 11. Low playful meadow flutter across bottom poppies and wildflowers */
@keyframes pathBottomMeadowHover {
  0% {
    transform: translate3d(32vw, 88vh, 0) rotate(-6deg);
    opacity: 0;
  }
  12% { opacity: 1; }
  35% {
    transform: translate3d(48vw, 80vh, 0) rotate(10deg);
  }
  60% {
    transform: translate3d(64vw, 85vh, 0) rotate(-8deg);
  }
  82% {
    transform: translate3d(44vw, 82vh, 0) rotate(6deg);
  }
  92% { opacity: 1; }
  100% {
    transform: translate3d(32vw, 88vh, 0) rotate(-6deg);
    opacity: 0;
  }
}

/* 12. Top wisteria reverse canopy glider (right to left) */
@keyframes pathTopCanopyGlider {
  0% {
    transform: translate3d(105vw, 8vh, 0) scaleX(-1) rotate(6deg);
    opacity: 0;
  }
  12% { opacity: 1; }
  35% {
    transform: translate3d(70vw, 14vh, 0) scaleX(-1) rotate(-8deg);
  }
  60% {
    transform: translate3d(40vw, 9vh, 0) scaleX(-1) rotate(10deg);
  }
  82% {
    transform: translate3d(18vw, 15vh, 0) scaleX(-1) rotate(-6deg);
  }
  92% { opacity: 1; }
  100% {
    transform: translate3d(-5vw, 8vh, 0) scaleX(-1) rotate(4deg);
    opacity: 0;
  }
}
</style>
