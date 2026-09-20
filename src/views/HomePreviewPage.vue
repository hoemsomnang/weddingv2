<template>
  <div class="home-preview-page">

    <FloatingPetals />
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
        src="@/assets/new_burgundy_cascade_trans.webp"
        class="top-burgundy-cascade-left"
        alt="Top Left Burgundy Cascade Bouquet"
        draggable="false"
        decoding="async"
      />
      <img
        src="@/assets/new_purple_top_left_trans.webp"
        class="top-flower-left"
        alt="Top Left Floral Corner"
        draggable="false"
        decoding="async"
      />
      <img
        src="@/assets/new_burgundy_cascade_trans.webp"
        class="top-burgundy-cascade-right"
        alt="Top Right Burgundy Cascade Bouquet"
        draggable="false"
        decoding="async"
      />
      <img
        src="@/assets/new_purple_top_left_trans.webp"
        class="top-flower-right"
        alt="Top Right Floral Corner"
        draggable="false"
        decoding="async"
      />
    </div>
       
   <section
      class="chandelier-section fade-in"
      :class="{ visible: entered }"
      style="--delay: 0.2s"
      aria-hidden="true"
    >
      <div class="chandelier-glow-backdrop"></div>
      <img
        src="@/assets/chandelier_trans.webp"
        class="chandelier-img"
        alt="Crystal Wedding Chandelier"
        draggable="false"
        decoding="async"
        fetchpriority="high"
        @load="onImgLoad"
      />
    </section> 
    

    <div class="scrollable-snap-wrapper" ref="scrollContainer" @scroll.passive="onContainerScroll">
      
      <section class="snap-page section-invitation-cover" id="page-invite">
        <div class="invitation-content" :class="{ 'section-animate-in': isInviteInView }">

          <h1 class="main-wedding-title anim-item anim-delay-1">{{ invitation.pageTitle }}</h1>

          <div class="parents-grid anim-item anim-delay-2">
            <div class="parent-col left-col">
              <div class="parent-row">
                <span class="role-text">{{ invitation.groomFather.role }}</span>
                <span class="name-text">{{ invitation.groomFather.name }}</span>
              </div>
              <div class="parent-row">
                <span class="role-text">{{ invitation.groomMother.role }}</span>
                <span class="name-text">{{ invitation.groomMother.name }}</span>
              </div>
            </div>

            <div class="parent-col right-col">
              <div class="parent-row">
                <span class="role-text">{{ invitation.brideFather.role }}</span>
                <span class="name-text">{{ invitation.brideFather.name }}</span>
              </div>
              <div class="parent-row">
                <span class="role-text">{{ invitation.brideMother.role }}</span>
                <span class="name-text">{{ invitation.brideMother.name }}</span>
              </div>
            </div>
          </div>

          <div class="honor-invite-title anim-item anim-delay-3">
            <img
              src="@/assets/gold_baroque_pediment_trans.webp"
              class="honor-ornament-wing honor-ornament-left"
              alt="Gold Ornament Left"
              draggable="false"
              decoding="async"
            />
            <span class="honor-invite-text">{{ invitation.honorInviteText }}</span>
            <img
              src="@/assets/gold_baroque_pediment_trans.webp"
              class="honor-ornament-wing honor-ornament-right"
              alt="Gold Ornament Right"
              draggable="false"
              decoding="async"
            />
          </div>

          <div class="formal-invitation-text anim-item anim-delay-4">
            <p v-for="(line, i) in invitation.invitationLines" :key="i">{{ line }}</p>
          </div>

          <div class="couple-names-grid anim-item anim-delay-5">
            <div class="couple-col groom-col">
              <span class="couple-role">{{ invitation.groomRole }}</span>
              <h2 class="couple-name">{{ invitation.groomName }}</h2>
            </div>
            <div class="couple-crest-center">
              <img
                src="@/assets/wedding_monogram_crest_sr_trans.webp"
                class="couple-monogram-crest"
                alt="Wedding Monogram Crest"
                draggable="false"
                decoding="async"
              />
            </div>
            <div class="couple-col bride-col">
              <span class="couple-role">{{ invitation.brideRole }}</span>
              <h2 class="couple-name">{{ invitation.brideName }}</h2>
            </div>
          </div>

          <div class="wedding-datetime-section anim-item anim-delay-6">
            <p class="khmer-lunar-date">{{ invitation.lunarDate }}</p>
            <p class="solar-date-highlight">{{ invitation.solarDate }}</p>
            <p class="reception-time">{{ invitation.receptionTime }}</p>
          </div>

          <div class="venue-section anim-item anim-delay-7">
            <h3 class="venue-main-name">{{ invitation.venueName }}</h3>
            <p class="venue-address-line">{{ invitation.venueAddress }}</p>
            <p class="venue-closing-wish">{{ invitation.venueClosingWish }}</p>
          </div>
        </div>
      </section>

      <!-- ── Section 2: Countdown & Couple Portrait ────────────── -->
      <section class="snap-page section-countdown" id="page-countdown">
        <div class="countdown-content" :class="{ 'section-animate-in': isCountdownInView }">

          <!-- 1. Countdown Title -->
          <div class="countdown-plaque-wrap anim-item anim-delay-1">
            <h2 class="countdown-plaque-title">ចំនួនថ្ងៃរាប់ថយក្រោយ</h2>
          </div>

          <!-- 2. Gold Ornate Divider -->
          <div class="countdown-divider-wrap anim-item anim-delay-2">
            <img
              src="@/assets/gold_divider_ornate.webp"
              class="countdown-diamond-divider"
              alt="Divider"
              draggable="false"
              decoding="async"
            />
          </div>

          <!-- 3. Four Countdown Unit Boxes -->
          <div class="countdown-boxes-row" role="timer" aria-live="polite">
            <div class="countdown-box anim-item anim-delay-3">
              <span class="countdown-number">{{ countdown.days }}</span>
              <span class="countdown-unit-name">{{ countdownLabels.days }}</span>
            </div>

            <span class="countdown-colon anim-item anim-delay-3">:</span>

            <div class="countdown-box anim-item anim-delay-4">
              <span class="countdown-number">{{ countdown.hours }}</span>
              <span class="countdown-unit-name">{{ countdownLabels.hours }}</span>
            </div>

            <span class="countdown-colon anim-item anim-delay-4">:</span>

            <div class="countdown-box anim-item anim-delay-5">
              <span class="countdown-number">{{ countdown.mins }}</span>
              <span class="countdown-unit-name">{{ countdownLabels.mins }}</span>
            </div>

            <span class="countdown-colon anim-item anim-delay-5">:</span>

            <div class="countdown-box anim-item anim-delay-6">
              <span class="countdown-number">{{ countdown.secs }}</span>
              <span class="countdown-unit-name">{{ countdownLabels.secs }}</span>
            </div>
          </div>

          <!-- 4. Subtitle / Blessing line -->
          <p class="countdown-blessing-text anim-item anim-delay-7">សូមអបអរសាទរគូស្វាមីភរិយាថ្មី</p>

          <!-- 5. Couple Portrait Photo Card -->
          <div class="couple-portrait-card anim-item anim-delay-8">
            <img
              src="@/assets/couple_wedding_portrait.jpg"
              class="couple-portrait-img"
              alt="Bride and Groom Wedding Portrait"
              draggable="false"
              decoding="async"
            />
          </div>

        </div>
      </section>

      <!-- ── Section 3: Event Agenda / Wedding Schedule ────────── -->
      <section class="snap-page section-agenda" id="page-agenda">
        <div class="agenda-content" :class="{ 'section-animate-in': isAgendaInView }">

          <!-- 1. Agenda Header Title -->
          <div class="agenda-header-wrap anim-item anim-delay-1">
            <h2 class="agenda-title">{{ invitation.agendaTitle }}</h2>
          </div>

          <!-- 2. Gold Ornate Divider -->
          <div class="agenda-divider-wrap anim-item anim-delay-2">
            <img
              src="@/assets/gold_divider_ornate.webp"
              class="agenda-ornate-divider"
              alt="Divider"
              draggable="false"
              decoding="async"
            />
          </div>

          <!-- 3. Agenda Days Program Cards -->
          <div class="agenda-days-container">
            <div
              v-for="(day, dIndex) in invitation.agendaDays"
              :key="dIndex"
              class="agenda-day-card anim-item"
              :class="`anim-delay-${dIndex + 3}`"
            >
              <!-- Day Header Banner -->
              <div class="agenda-day-header">
                <span class="agenda-header-ornament">❖</span>
                <h3 class="agenda-day-title">{{ day.dayTitle }}</h3>
                <span class="agenda-header-ornament">❖</span>
              </div>

              <!-- Timeline Items List -->
              <div class="agenda-timeline">
                <div
                  v-for="(item, sIndex) in day.schedule"
                  :key="sIndex"
                  class="agenda-timeline-row"
                >
                  <!-- Left: Time -->
                  <div class="agenda-time-col">
                    <span class="agenda-time-text">{{ item.time }}</span>
                  </div>

                  <!-- Center: Golden Ceremonial Icon -->
                  <div class="agenda-icon-col">
                    <img
                      :src="getAgendaIcon(item.icon)"
                      class="agenda-ceremony-icon-img"
                      :alt="item.title"
                      draggable="false"
                      decoding="async"
                    />
                  </div>

                  <!-- Right: Ceremony Name -->
                  <div class="agenda-detail-col">
                    <span class="agenda-colon">:</span>
                    <span class="agenda-ceremony-name">{{ item.title }}</span>
                  </div>
                </div>
              </div>

              <!-- Day Notice / Guest Invitation Callout -->
              <div v-if="day.notice" class="agenda-day-notice">
                <span class="agenda-notice-text">« {{ day.notice }} »</span>
              </div>
            </div>
          </div>

        </div>
      </section>
    </div>

    <!-- ── Fixed Bottom Action Dock (Persistent on scroll) ─────── -->
    <div class="bottom-action-dock">
      <div
        class="scroll-up-indicator"
        @click="onScrollUpIndicatorClick"
        role="button"
        tabindex="0"
        aria-label="Scroll to next section"
      >
        <svg class="scroll-up-chevron" viewBox="0 0 24 20" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M5 9L12 3L19 9" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>
          <path d="M5 16L12 10L19 16" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
        <span class="scroll-up-text">{{ invitation.scrollUpText }}</span>
      </div>

      <div class="bottom-nav-buttons-row">
        <button
          type="button"
          class="bottom-nav-btn"
          @click="onCalendarClick"
          aria-label="Wedding Program & Calendar"
        >
          <img
            src="@/assets/btn_calendar.svg"
            alt="Calendar"
            draggable="false"
            decoding="async"
          />
        </button>

        <button
          type="button"
          class="bottom-nav-btn"
          @click="onLocationClick"
          aria-label="Venue Location Map"
        >
          <img
            src="@/assets/btn_location.svg"
            alt="Location"
            draggable="false"
            decoding="async"
          />
        </button>

        <button
          type="button"
          class="bottom-nav-btn"
          @click="onGalleryClick"
          aria-label="Photo & Video Gallery"
        >
          <img
            src="@/assets/btn_gallery.svg"
            alt="Gallery"
            draggable="false"
            decoding="async"
          />
        </button>

        <button
          type="button"
          class="bottom-nav-btn"
          @click="onWishesClick"
          aria-label="Guest Wishes & Comments"
        >
          <img
            src="@/assets/btn_wishes.svg"
            alt="Wishes"
            draggable="false"
            decoding="async"
          />
        </button>
      </div>
    </div>

    <!-- Bottom Floral Background -->
    <div class="bottom-page-background" aria-hidden="true">
      <img
        src="@/assets/bottom_background.webp"
        class="bottom-background-img"
        alt="Bottom Floral Background"
        draggable="false"
        decoding="async"
      />
    </div>




    <!-- Bottom Left Purple Flower Bouquet Accent -->
    <img
      src="@/assets/purple_flower_bouquet_v2.webp"
      class="bottom-left-purple-bouquet"
      alt="Bottom Left Floral Bouquet"
      draggable="false"
      decoding="async"
    />

    <img
      src="@/assets/purple_cosmos_original_trans.webp"
      class="purple_cosmos_original_trans"
      alt="Bottom Right Floral Bouquet"
      draggable="false"
      decoding="async"
    />

        <img
      src="@/assets/purple_watercolor_original_trans.webp"
      class="purple_watercolor_original_trans"
      alt="Bottom Right Floral Bouquet"
      draggable="false"
      decoding="async"
    />

        <img
      src="@/assets/purple_floral_spray_trans.webp"
      class="purple_flower_bloom_trans"
      alt="Bottom Right Floral Bouquet"
      draggable="false"
      decoding="async"
    />

    <img
      src="@/assets/purple_delphinium_reference_nobg.webp"
      class="purple_delphinium_reference_nobg"
      alt="Bottom Right Floral Bouquet"
      draggable="false"
      decoding="async"
    />

    <img
      src="@/assets/purple_delphinium_reference_nobg.webp"
      class="purple_watercolor_corner_trans"
      alt="Bottom Left Floral Bouquet"
      draggable="false"
      decoding="async"
    />


    <!-- Bottom right Purple Flower Bouquet Accent -->
    <img
      src="@/assets/purple_flower_bouquet_v2.webp"
      class="right-bottom-purple-bouquet"
      alt="Bottom Right Floral Bouquet"
      draggable="false"
      decoding="async"
    />

    <img
      src="@/assets/purple_cosmos_original_trans.webp"
      class="right-purple_cosmos_original_trans"
      alt="Bottom Right Floral Bouquet"
      draggable="false"
      decoding="async"
    />
    
    <img
      src="@/assets/purple_watercolor_original_trans.webp"
      class="right-purple_watercolor_original_trans"
      alt="Bottom Right Floral Bouquet"
      draggable="false"
      decoding="async"
    />

        <img
      src="@/assets/purple_floral_spray_trans.webp"
      class="right-purple_flower_bloom_trans"
      alt="Bottom Right Floral Bouquet"
      draggable="false"
      decoding="async"
    />

            <img
      src="@/assets/purple_delphinium_reference_nobg.webp"
      class="right-purple_delphinium_reference_nobg"
      alt="Bottom Right Floral Bouquet"
      draggable="false"
      decoding="async"
    />

    <img
      src="@/assets/purple_delphinium_reference_nobg.webp"
      class="right-purple_watercolor_corner_trans"
      alt="Bottom Right Floral Bouquet"
      draggable="false"
      decoding="async"
    /> 

    <!-- Bottom Right Romantic Gazebo Accent -->
    <img
      src="@/assets/purple_wedding_gazebo_trans.webp"
      class="bottom-right-wedding-gazebo"
      alt="Purple Wedding Gazebo"
      draggable="false"
      decoding="async"
    />

    <!-- Bottom Ground Garden Flowers (Connecting Gazebo & Landscape) -->
    <img
      src="@/assets/purple_ground_flowers_trans.webp"
      class="bottom-ground-garden-flowers"
      alt="Ground Garden Flowers"
      draggable="false"
      decoding="async"
    />

    <!-- Bottom Center Purple Flower Bouquet Accent -->
    <img
      src="@/assets/purple_floral_bouquet_new_trans.webp"
      class="bottom-center-purple-bouquet"
      alt="Bottom Center Floral Bouquet"
      draggable="false"
      decoding="async"
    />

  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'
import FloatingPetals from '@/components/FloatingPetals.vue'
import ButterflyEffect from '@/components/ButterflyEffect.vue'
import invitation from '@/config/invitation.js'

// ── 3D Golden Wedding Ceremony Agenda Icons ──
import iconWelcome from '@/assets/icons/agenda_01_welcome.webp'
import iconFruit from '@/assets/icons/agenda_02_fruit.webp'
import iconHall from '@/assets/icons/agenda_03_hall.webp'
import iconRings from '@/assets/icons/agenda_04_rings.webp'
import iconMonks from '@/assets/icons/agenda_05_monks.webp'
import iconHaircut from '@/assets/icons/agenda_06_haircut.webp'
import iconThread from '@/assets/icons/agenda_07_thread.webp'
import iconLunch from '@/assets/icons/agenda_08_lunch.webp'
import iconBanquet from '@/assets/icons/agenda_09_banquet.webp'

const agendaIconMap = {
  welcome: iconWelcome,
  fruit: iconFruit,
  hall: iconHall,
  rings: iconRings,
  monks: iconMonks,
  haircut: iconHaircut,
  thread: iconThread,
  lunch: iconLunch,
  banquet: iconBanquet,
}

function getAgendaIcon(key) {
  return agendaIconMap[key] || iconWelcome
}

const router = useRouter()
const scrollContainer = ref(null)

// ── Entrance & Scroll Section Observation State ──
const entered = ref(true)
const isInviteInView = ref(true)
const isCountdownInView = ref(false)
const isAgendaInView = ref(false)

function onImgLoad() {
  entered.value = true
}

function onContainerScroll() {
  if (!scrollContainer.value) return
  const top = scrollContainer.value.scrollTop
  const h = scrollContainer.value.clientHeight || window.innerHeight
  // When top is less than 45% of page height, page-invite is in view
  isInviteInView.value = top < h * 0.45
  // When top reaches 30% of page height, page-countdown triggers its entrance
  isCountdownInView.value = top >= h * 0.3
  // When top reaches 130% of page height, page-agenda triggers its entrance
  isAgendaInView.value = top >= h * 1.3
}

// ── Live Countdown State & Logic ──
const now = ref(Date.now())
let countdownTimer = null
let sectionObserver = null

onMounted(() => {
  entered.value = true
  countdownTimer = setInterval(() => {
    now.value = Date.now()
  }, 1000)

  // IntersectionObserver for snap sections
  if (typeof window !== 'undefined' && 'IntersectionObserver' in window) {
    sectionObserver = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.target.id === 'page-countdown') {
            if (entry.isIntersecting) {
              isCountdownInView.value = true
            } else if (scrollContainer.value && scrollContainer.value.scrollTop < 100) {
              isCountdownInView.value = false
            }
          } else if (entry.target.id === 'page-agenda') {
            if (entry.isIntersecting) {
              isAgendaInView.value = true
            } else if (scrollContainer.value && scrollContainer.value.scrollTop < window.innerHeight * 0.5) {
              isAgendaInView.value = false
            }
          } else if (entry.target.id === 'page-invite') {
            if (entry.isIntersecting) {
              isInviteInView.value = true
            }
          }
        })
      },
      {
        root: scrollContainer.value,
        threshold: 0.25,
      }
    )

    const inviteEl = document.getElementById('page-invite')
    const countdownEl = document.getElementById('page-countdown')
    const agendaEl = document.getElementById('page-agenda')
    if (inviteEl) sectionObserver.observe(inviteEl)
    if (countdownEl) sectionObserver.observe(countdownEl)
    if (agendaEl) sectionObserver.observe(agendaEl)
  }
})

onUnmounted(() => {
  if (countdownTimer) clearInterval(countdownTimer)
  if (sectionObserver) sectionObserver.disconnect()
})

const countdownLabels = invitation.countdownLabels || {
  days: 'ថ្ងៃ',
  hours: 'ម៉ោង',
  mins: 'នាទី',
  secs: 'វិនាទី',
}

const countdown = computed(() => {
  const target = new Date(invitation.targetDate || '2026-11-24T08:00:00').getTime()
  const diff = target - now.value
  if (diff <= 0) {
    return { days: '00', hours: '00', mins: '00', secs: '00' }
  }
  const days = Math.floor(diff / (1000 * 60 * 60 * 24))
  const hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60))
  const mins = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60))
  const secs = Math.floor((diff % (1000 * 60)) / 1000)

  return {
    days: String(days).padStart(2, '0'),
    hours: String(hours).padStart(2, '0'),
    mins: String(mins).padStart(2, '0'),
    secs: String(secs).padStart(2, '0'),
  }
})

function scrollToPage(targetId) {
  if (!targetId) return
  const targetEl = document.getElementById(targetId)
  if (targetEl) {
    targetEl.scrollIntoView({ behavior: 'smooth' })
  } else if (scrollContainer.value) {
    scrollContainer.value.scrollBy({ top: window.innerHeight, behavior: 'smooth' })
  }
}

function onScrollUpIndicatorClick() {
  if (!scrollContainer.value) return
  const top = scrollContainer.value.scrollTop
  const h = scrollContainer.value.clientHeight || window.innerHeight
  if (top < h * 0.5) {
    scrollToPage('page-countdown')
  } else if (top < h * 1.5) {
    scrollToPage('page-agenda')
  } else {
    scrollToPage('page-invite')
  }
}

function goBackToCover() {
  router.push({ name: 'cover' })
}

function onCalendarClick() {
  const agendaEl = document.getElementById('page-agenda')
  if (agendaEl && scrollContainer.value) {
    const isAtAgenda = scrollContainer.value.scrollTop >= (agendaEl.offsetTop - 120)
    if (isAtAgenda) {
      scrollToPage('page-invite')
      return
    }
  }
  scrollToPage('page-agenda')
}

function onLocationClick() {
  const query = encodeURIComponent(invitation.receptionTime || 'ភូមិអូរល្វា ឃុំជ្រៃសីម៉ា ស្រុកសំពៅលូន ខេត្តបាត់ដំបង')
  window.open(`https://www.google.com/maps/search/?api=1&query=${query}`, '_blank')
}

function onGalleryClick() {
  router.push({ name: 'videoPreView' })
}

function onWishesClick() {
  scrollToPage('page-agenda')
}
</script>

<style scoped src="./HomePreviewPage.css"></style>
