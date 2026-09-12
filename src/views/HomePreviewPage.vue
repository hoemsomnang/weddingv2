<!--
  HomePreviewPage.vue
  Digital Wedding Invitation Preview & Details Page
-->
<template>
  <div class="home-preview-page">

    <!-- ── Full-Screen Sunset Sky Page Background ── -->
    <div class="preview-page-fullscreen-bg" aria-hidden="true">
      <img
        src="@/assets/islamic_wedding_arch.webp"
        class="preview-fullscreen-bg-img"
        alt="Fairytale Sunset Sky Page Background"
        draggable="false"
        decoding="async"
        fetchpriority="high"
      />
      <div class="preview-fullscreen-bg-overlay"></div>
    </div>

    <!-- ── Ambient Floating Petals & Butterflies ── -->
    <FloatingPetals />
    <ButterflyEffect theme="white" />

    <!-- ── Luxury Chandelier Hanging from Top ── -->
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

    <!-- ── Hero Greeting ── -->
    <section
      class="hero-greeting-block fade-in"
      :class="{ visible: entered }"
      style="--delay: 0.4s"
    >
      <h1 class="khmer-ceremony-title">{{ invitation.khmerGreeting }}</h1>
      <p class="khmer-ceremony-sub">{{ invitation.khmerSubtitle[0] || 'សូមគោរពអញ្ជើញចូលរួម' }}</p>
    </section>

    <!-- ── Background Fairytale Chateau & Garden ── -->
    <!--
    <div class="preview-bg-chateau-wrap" aria-hidden="true">
      <img
        src="@/assets/chateau_garden_original_trans.webp"
        class="preview-bg-chateau-img"
        alt="Fairytale Chateau & Garden Backdrop"
        draggable="false"
        decoding="async"
      />
    </div>-->

    <!-- ── Left Side Floral Accent ── -->     
    <img
        src="@/assets/calla_lily_purple_rose_ribbon_trans.webp"
        class="call-lily-left-img"
        alt="Left Floral Accent"
        draggable="false"
        decoding="async"
      />
    <img
        src="@/assets/purple_rose_dew_ref2_trans.webp"
        class="left-purple_rose_dew_ref2_trans"
        alt="Left Floral Accent"
        draggable="false"
        decoding="async"
      />
    <img
        src="@/assets/purple_rose_dew_ref1_trans.webp"
        class="left-purple_rose_dew_ref1_trans" 
        alt="Left Floral Accent"
        draggable="false"
        decoding="async"
      />


      
    <!-- ── Right Side Floral Accent ── -->
    <img
        src="@/assets/calla_lily_purple_rose_ribbon_trans.webp"
        class="call-lily-right-img"
        alt="Right Floral Accent"
        draggable="false"
        decoding="async"
      />
    <img
        src="@/assets/purple_rose_dew_ref2_trans.webp"
        class="right-purple_rose_dew_ref2_trans"
        alt="Left Floral Accent"
        draggable="false"
        decoding="async"
      />
      <img
        src="@/assets/purple_rose_dew_ref1_trans.webp"
        class="right-purple_rose_dew_ref1_trans" 
        alt="Left Floral Accent"
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

// ── Entrance animation state (matching CoverPage.vue) ──────
const entered = ref(false)

function onImgLoad() {
  entered.value = true
}

onMounted(() => {
  requestAnimationFrame(() => {
    entered.value = true
  })
})

function goBackToCover() {
  router.push({ name: 'cover' })
}
</script>

<style scoped src="./HomePreviewPage.css"></style>
