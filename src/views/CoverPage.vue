<!--
  CoverPage.vue
  The first (and currently only) page of the digital wedding invitation.
  Shows: corner florals, Khmer greeting, monogram crest, couple names,
         date, countdown, action buttons, and bottom floral meadow.
-->
<template>
  <div class="cover-page">

    <!-- ── Floating petals (decorative, behind everything) ── -->
    <FloatingPetals />

    <!-- ── Dainty Butterflies fluttering across the page ── -->
    <ButterflyEffect theme="white" />


    <!-- ── Top floral header arrangement ─────────────────── -->
    <div class="top-floral-header" aria-hidden="true">
      <img
        src="@/assets/horizontal_floral_bridge_trans.webp"
        class="top-floral-bridge-bg"
        alt="Top Floral Bridge"
        draggable="false"
        decoding="async"
        fetchpriority="high"
      />
      <img
        src="@/assets/purple_top_left_trans.webp"
        class="top-flower-left"
        alt="Top Left Floral Corner"
        draggable="false"
        decoding="async"
        @load="onImgLoad"
      />
      
            
      <img
        src="@/assets/purple_flower_bouquet_2.webp"
        class="top-flower-left-bg"
        alt="Top Left Background Bouquet"
        draggable="false"
        decoding="async"
      />

      <img
        src="@/assets/purple_flower_bouquet_2.webp"
        class="top-flower-center"
        alt="Top Center Floral Garland"
        draggable="false"
        decoding="async"
      />
      <img
        src="@/assets/purple_flower_bouquet_2.webp"
        class="top-flower-right-bg"
        alt="Top Right Background Bouquet"
        draggable="false"
        decoding="async"
      />
      <img
        src="@/assets/purple_top_right_trans.webp"
        class="top-flower-right"
        alt="Top Right Floral Corner"
        draggable="false"
        decoding="async"
      />
    </div>

    <!-- ── Main content ───────────────────────────────────── -->
    <main class="cover-content" role="main">
      <!-- Ceremony Heading above logo -->
      <h1
        class="greeting fade-in"
        :class="{ visible: entered }"
        style="--delay: 0.45s"
      >
        {{ invitation.khmerGreeting }}
      </h1>

      <!-- S&R Monogram Crest Logo -->
      <div
        class="crest-wrap fade-in"
        :class="{ visible: entered }"
        style="--delay: 0.52s"
      >
        <img
          src="@/assets/wedding_monogram_crest_sr_trans.webp"
          class="monogram-crest-img"
          alt="S&R Wedding Monogram Crest"
          draggable="false"
          decoding="async"
          fetchpriority="high"
        />
      </div>

      <!-- Khmer subtitle (lines from invitation.js) -->
      <p
        v-for="(line, i) in invitation.khmerSubtitle"
        :key="i"
        class="khmer-sub fade-in"
        :class="{ visible: entered, 'khmer-sub-bold': i === 1 }"
        :style="{ '--delay': (0.6 + i * 0.08) + 's' }"
      >
        {{ line }}
      </p>


      <!-- Ornate Gold Flourish Divider -->
      <GoldDivider
        class="fade-in"
        :class="{ visible: entered }"
        style="--delay: 0.78s; margin: clamp(18px, 4vw, 26px) auto clamp(20px, 4.5vw, 30px)"
      />

      <!-- ── Honored Guest & Open Invitation Section ── -->
      <div
        class="guest-open-wrap fade-in"
        :class="{ visible: entered }"
        style="--delay: 0.94s"
      >
        <p class="guest-title">{{ invitation.guestHonorLabel }}</p>

        <!-- Golden tapered divider with center motif (matching image) -->
        <svg class="guest-divider-svg" viewBox="0 0 200 10" fill="none" aria-hidden="true">
          <defs>
            <linearGradient id="goldLineGrad" x1="0%" y1="0%" x2="100%" y2="0%">
              <stop offset="0%" stop-color="#d4a43a" stop-opacity="0.1"/>
              <stop offset="20%" stop-color="#d4a43a"/>
              <stop offset="50%" stop-color="#f5d98e"/>
              <stop offset="80%" stop-color="#d4a43a"/>
              <stop offset="100%" stop-color="#d4a43a" stop-opacity="0.1"/>
            </linearGradient>
          </defs>
          <line x1="8" y1="5" x2="92" y2="5" stroke="url(#goldLineGrad)" stroke-width="1.2" stroke-linecap="round"/>
          <circle cx="100" cy="5" r="2.2" fill="#d4a43a"/>
          <circle cx="100" cy="5" r="1.2" fill="#fef3c7"/>
          <line x1="108" y1="5" x2="192" y2="5" stroke="url(#goldLineGrad)" stroke-width="1.2" stroke-linecap="round"/>
        </svg>

        <!-- Ornate Vintage Cartouche Plaque Button (matching reference image) -->
        <!-- Ornate Khmer Golden Frame Button -->
        <button
          type="button"
          class="btn-cartouche-plaque"
          @click="onOpenInvitation"
          aria-label="Open Invitation"
        >
          <img
            src="@/assets/golden_frame_button_trans.webp"
            class="cartouche-plaque-img"
            alt="Golden Frame"
            draggable="false"
            decoding="async"
            fetchpriority="high"
          />

          <!-- Button Text Labels matching reference image -->
          <div class="btn-open-labels">
            <span class="btn-open-text">{{ invitation.btnOpenInvitation }}</span>
          </div>
        </button>
      </div>



    </main>


    <!-- ── Bottom floral background ─────── -->
    <div class="bottom-floral" aria-hidden="true">
      <img
        src="@/assets/background.webp"
        class="bottom-bg-img"
        alt="Wedding bottom background"
        draggable="false"
        decoding="async"
      />
      <!-- ── Vertical side edge floral spires (Left & Right) ── -->
      <img
        src="@/assets/purple_edge_flowers_trans.webp"
        class="side-edge-flower side-edge-flower-left"
        alt="Wedding left edge floral spire"
        draggable="false"
        decoding="async"
      />
      <img
        src="@/assets/purple_edge_flowers_trans.webp"
        class="side-edge-flower side-edge-flower-right"
        alt="Wedding right edge floral spire"
        draggable="false"
        decoding="async"
      />

      <!-- Purpla FLower rgith -->
      <img
        src="@/assets/purple_flower_bouquet_2.webp"
        class="bottom-right-pillar-flower"
        alt="Wedding purple flower arrangement"
        draggable="false"
        decoding="async"
      />
      <img
        src="@/assets/purple_flower.webp"
        class="bottom-purple-flower"
        alt="Wedding purple flower"
        draggable="false"
        decoding="async"
      />

      <img
        src="@/assets/purple_flower bouquet_.webp"
        class="purple-flower-bouquet"
        alt="Wedding purple flower"
        draggable="false"
        decoding="async"
      />

      <img
        src="@/assets/bottom3.webp"
        class="bottom-bottom3"
        alt="Wedding purple flower"
        draggable="false"
        decoding="async"
      />

      <img
        src="@/assets/bottom18.webp"
        class="bottom-bottom18"
        alt="Wedding purple flower"
        draggable="false"
        decoding="async"
      />

      <!-- Purpla FLower left -->
      <img
        src="@/assets/purple_flower_bouquet_2.webp"
        class="bottom-left-pillar-flower"
        alt="Wedding purple flower arrangement"
        draggable="false"
        decoding="async"
      />
      <img
        src="@/assets/purple_flower.webp"
        class="bottom-purple-flower1"
        alt="Wedding purple flower"
        draggable="false"
        decoding="async"
      />
      <img
        src="@/assets/purple_flower bouquet_.webp"
        class="purple-flower-bouquet1"
        alt="Wedding purple flower"
        draggable="false"
        decoding="async"
      />

      <img
        src="@/assets/bottom3.webp"
        class="bottom-bottom3-1"
        alt="Wedding purple flower"
        draggable="false"
        decoding="async"
      />

      <img
        src="@/assets/bottom18.webp"
        class="bottom-bottom18-1"
        alt="Wedding purple flower"
        draggable="false"
        decoding="async"
      />

      <!-- Center flower in remaining slot -->
      <img
        src="@/assets/purple_flower_bouquet_v2.webp"
        class="bottom-center-flower"
        alt="Wedding center floral bouquet"
        draggable="false"
        decoding="async"
      />
      
    </div>

  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import FloatingPetals  from '@/components/FloatingPetals.vue'
import ButterflyEffect from '@/components/ButterflyEffect.vue'
import MonogramCrest   from '@/components/MonogramCrest.vue'
import CountdownTimer from '@/components/CountdownTimer.vue'
import GoldDivider    from '@/components/GoldDivider.vue'

// ── All content lives in one file — edit src/config/invitation.js ──
import invitation from '@/config/invitation.js'

// ── Entrance animation state ──────────────────────────────
const entered = ref(false)
const showScrollHint = ref(true)
let hintTimer = null

function onImgLoad() {
  entered.value = true
}

onMounted(() => {
  // Trigger entrance immediately on next tick for lightning-fast mobile perception
  requestAnimationFrame(() => {
    entered.value = true
  })
  hintTimer = setTimeout(() => { showScrollHint.value = false }, 6000)
})

onUnmounted(() => clearTimeout(hintTimer))

// ── Actions ───────────────────────────────────────────────
function onOpenInvitation() {
  alert(invitation.openInvitationAlert)
}

function onRSVP() {
  alert(invitation.rsvpAlertMessage)
}

function onCalendar() {
  const fmt = (d) => d.toISOString().replace(/[-:]/g, '').split('.')[0] + 'Z'
  const start = new Date(invitation.targetDate)
  const end   = new Date(start.getTime() + 3600000 * invitation.eventDurationHours)
  const url = [
    'https://calendar.google.com/calendar/render?action=TEMPLATE',
    `&text=Wedding+of+${invitation.groomName}+%26+${invitation.brideName}`,
    `&dates=${fmt(start)}/${fmt(end)}`,
    `&details=${encodeURIComponent(invitation.calendarDetails)}`,
    `&location=${encodeURIComponent(invitation.venue)}`,
  ].join('')
  window.open(url, '_blank')
}
</script>

<style scoped src="./CoverPage.css"></style>
