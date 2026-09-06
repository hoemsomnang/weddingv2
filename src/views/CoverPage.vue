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

    <!-- ── Background Wedding Gazebo Rotunda ─────────────── -->
    <div class="cover-bg-gazebo" aria-hidden="true">
      <img
        src="@/assets/purple_wedding_gazebo_trans.png"
        class="bg-gazebo-img"
        alt="Wedding Garden Gazebo"
        draggable="false"
      />
    </div>

    <!-- ── Top floral header arrangement ─────────────────── -->
    <div class="top-floral-header" aria-hidden="true">
      <img
        src="@/assets/horizontal_floral_bridge_trans.png"
        class="top-floral-bridge-bg"
        alt="Top Floral Bridge"
        draggable="false"
      />
      <img
        src="@/assets/purple_top_left_trans.png"
        class="top-flower-left"
        alt="Top Left Floral Corner"
        draggable="false"
        @load="onImgLoad"
      />
      
            
      <img
        src="@/assets/purple_flower_bouquet_2.png"
        class="top-flower-left-bg"
        alt="Top Left Background Bouquet"
        draggable="false"
      />

      <img
        src="@/assets/purple_flower_bouquet_2.png"
        class="top-flower-center"
        alt="Top Center Floral Garland"
        draggable="false"
      />
      <img
        src="@/assets/purple_flower_bouquet_2.png"
        class="top-flower-right-bg"
        alt="Top Right Background Bouquet"
        draggable="false"
      />
      <img
        src="@/assets/purple_top_right_trans.png"
        class="top-flower-right"
        alt="Top Right Floral Corner"
        draggable="false"
      />
    </div>

    <!-- ── Main content ───────────────────────────────────── -->
    <main class="cover-content" role="main">





      <!-- Khmer subtitle (lines from invitation.js) -->
      <p
        v-for="(line, i) in invitation.khmerSubtitle"
        :key="i"
        class="khmer-sub fade-in"
        :class="{ visible: entered }"
        :style="{ '--delay': (0.6 + i * 0.08) + 's' }"
      >
        {{ line }}
      </p>

      <!-- Date & venue -->
      <div
        class="date-block fade-in"
        :class="{ visible: entered }"
        style="--delay: 0.72s"
      >
        <p class="date-eyebrow">{{ invitation.saveTheDateLabel }}</p>
        <p class="date-main">{{ invitation.dateDisplay }}</p>
        <p class="date-venue">{{ invitation.venue }}</p>
      </div>

      <!-- Divider 2 -->
      <GoldDivider
        variant="short"
        class="fade-in"
        :class="{ visible: entered }"
        style="--delay: 0.78s; margin: 12px auto 18px"
      />

      <!-- Countdown -->
      <div
        class="countdown-wrap fade-in"
        :class="{ visible: entered }"
        style="--delay: 0.88s"
      >
        <CountdownTimer :target-date="invitation.targetDate" />
      </div>



    </main>


    <!-- ── Bottom floral background ─────── -->
    <div class="bottom-floral" aria-hidden="true">
      <!-- ── Dainty Butterflies fluttering around bottom flowers ── -->
      <ButterflyEffect theme="white" />

      <img
        src="@/assets/background.png"
        class="bottom-bg-img"
        alt="Wedding bottom background"
        draggable="false"
      />
      <!-- ── Vertical side edge floral spires (Left & Right) ── -->
      <img
        src="@/assets/purple_edge_flowers_trans.png"
        class="side-edge-flower side-edge-flower-left"
        alt="Wedding left edge floral spire"
        draggable="false"
      />
      <img
        src="@/assets/purple_edge_flowers_trans.png"
        class="side-edge-flower side-edge-flower-right"
        alt="Wedding right edge floral spire"
        draggable="false"
      />

      <!-- Purpla FLower rgith -->
      <img
        src="@/assets/purple_flower_bouquet_2.png"
        class="bottom-right-pillar-flower"
        alt="Wedding purple flower arrangement"
        draggable="false"
      />
      <img
        src="@/assets/purple_flower.png"
        class="bottom-purple-flower"
        alt="Wedding purple flower"
        draggable="false"
      />

      <img
        src="@/assets/purple_flower bouquet_.png"
        class="purple-flower-bouquet"
        alt="Wedding purple flower"
        draggable="false"
      />

      <img
        src="@/assets/bottom3.svg"
        class="bottom-bottom3"
        alt="Wedding purple flower"
        draggable="false"
      />

      <img
        src="@/assets/bottom18.svg"
        class="bottom-bottom18"
        alt="Wedding purple flower"
        draggable="false"
      />

      <!-- Purpla FLower left -->
      <img
        src="@/assets/purple_flower_bouquet_2.png"
        class="bottom-left-pillar-flower"
        alt="Wedding purple flower arrangement"
        draggable="false"
      />
      <img
        src="@/assets/purple_flower.png"
        class="bottom-purple-flower1"
        alt="Wedding purple flower"
        draggable="false"
      />
      <img
        src="@/assets/purple_flower bouquet_.png"
        class="purple-flower-bouquet1"
        alt="Wedding purple flower"
        draggable="false"
      />

      <img
        src="@/assets/bottom3.svg"
        class="bottom-bottom3-1"
        alt="Wedding purple flower"
        draggable="false"
      />

      <img
        src="@/assets/bottom18.svg"
        class="bottom-bottom18-1"
        alt="Wedding purple flower"
        draggable="false"
      />

      <!-- Center flower in remaining slot -->
      <img
        src="@/assets/purple_flower_bouquet_v2.png"
        class="bottom-center-flower"
        alt="Wedding center floral bouquet"
        draggable="false"
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
  // trigger animations after SVG corner images are ready
  setTimeout(() => { entered.value = true }, 150)
}

onMounted(() => {
  // Fallback: trigger even if image is cached (already loaded)
  setTimeout(() => { entered.value = true }, 500)
  hintTimer = setTimeout(() => { showScrollHint.value = false }, 6000)
})

onUnmounted(() => clearTimeout(hintTimer))

// ── Actions ───────────────────────────────────────────────
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
