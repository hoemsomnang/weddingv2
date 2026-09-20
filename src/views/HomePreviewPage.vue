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
       
   <!-- <section
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
    </section> -->
    

    <div class="scrollable-snap-wrapper" ref="scrollContainer">
      
      <section class="snap-page section-invitation-cover" id="page-invite">
        <div class="invitation-content fade-in" :class="{ visible: entered }" style="--delay: 0.35s">

          <h1 class="main-wedding-title">{{ invitation.pageTitle }}</h1>

          <div class="parents-grid">
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

          <div class="honor-invite-title">
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

          <div class="formal-invitation-text">
            <p v-for="(line, i) in invitation.invitationLines" :key="i">{{ line }}</p>
          </div>

          <div class="couple-names-grid">
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

          <div class="wedding-datetime-section">
            <p class="khmer-lunar-date">{{ invitation.lunarDate }}</p>
            <p class="solar-date-highlight">{{ invitation.solarDate }}</p>
            <p class="reception-time">{{ invitation.receptionTime }}</p>
          </div>

          <div class="venue-section">
            <h3 class="venue-main-name">{{ invitation.venueName }}</h3>
            <p class="venue-address-line">{{ invitation.venueAddress }}</p>
            <p class="venue-closing-wish">{{ invitation.venueClosingWish }}</p>
          </div>

          <button
            type="button"
            class="scroll-down-cue scroll-down-banner-btn"
            @click="scrollToPage('page-countdown')"
            aria-label="Scroll to next section"
          >
            <img
              src="@/assets/gold_flourish_3d_trans.webp"
              class="scroll-down-banner-img"
              alt="Scroll to details"
              draggable="false"
              decoding="async"
            />
            <div class="scroll-down-banner-inner">
              <span class="scroll-down-banner-text">{{ invitation.scrollUpText }}</span>
            </div>
          </button>

        </div>
      </section>
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
      src="@/assets/purple_watercolor_corner_trans.webp"
      class="purple_watercolor_corner_trans"
      alt="Bottom Right Floral Bouquet"
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
      src="@/assets/purple_watercolor_corner_trans.webp"
      class="right-purple_watercolor_corner_trans"
      alt="Bottom Right Floral Bouquet"
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
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import FloatingPetals from '@/components/FloatingPetals.vue'
import ButterflyEffect from '@/components/ButterflyEffect.vue'
import invitation from '@/config/invitation.js'

const router = useRouter()
const scrollContainer = ref(null)

// ── Entrance state (immediate 0ms visibility on mobile) ──
const entered = ref(true)

function onImgLoad() {
  entered.value = true
}

onMounted(() => {
  entered.value = true
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

function goBackToCover() {
  router.push({ name: 'cover' })
}
</script>

<style scoped src="./HomePreviewPage.css"></style>
