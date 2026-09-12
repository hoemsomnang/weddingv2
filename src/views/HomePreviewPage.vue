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
    <div class="left-flower-wrap" aria-hidden="true">
      <img
        src="@/assets/flower_tulip_lilac_spring_trans.webp"
        class="left-tulip-bg-extra-img"
        alt="Left Spring Tulip Accent"
        draggable="false"
        decoding="async"
      />
      <img
        src="@/assets/flower_lavender_purple_ribbon_trans.webp"
        class="left-lavender-ribbon-img"
        alt="Left Lavender Purple Ribbon Bouquet"
        draggable="false"
        decoding="async"
      />
      <img
        src="@/assets/purple_white_tulip_ribbon_trans.webp"
        class="left-tulip-ribbon-bg-img"
        alt="Left Purple White Tulip Ribbon Bouquet"
        draggable="false"
        decoding="async"
      />
      <img
        src="@/assets/anemone_colorful_bouquet_trans.webp"
        class="left-anemone-bg-img"
        alt="Left Colorful Anemone Bouquet"
        draggable="false"
        decoding="async"
      />
      <img
        src="@/assets/flower_pink_lisianthus_branch_trans.webp"
        class="left-lisianthus-bg-img"
        alt="Left Pink Lisianthus Branch"
        draggable="false"
        decoding="async"
      />
      <img
        src="@/assets/flower_tulip_lilac_spring_trans.webp"
        class="left-flower-img"
        alt="Left Spring Tulip & Lilac Flower"
        draggable="false"
        decoding="async"
      />
      <img
        src="@/assets/flower_tulip_purple_pink_bouquet_trans.webp"
        class="left-calla-flower-img"
        alt="Left Calla Lily & Purple Rose Bouquet"
        draggable="false"
        decoding="async"
      />
      <img
        src="@/assets/flower_purple_tulip_cluster_trans.webp"
        class="left-purple-tulip-cluster-img"
        alt="Left Purple Tulip Cluster"
        draggable="false"
        decoding="async"
      />
    </div>

    <!-- ── Right Side Floral Accent ── -->
    <div class="right-flower-wrap" aria-hidden="true">
      <img
        src="@/assets/flower_tulip_lilac_spring_trans.webp"
        class="right-tulip-bg-extra-img"
        alt="Right Spring Tulip Accent"
        draggable="false"
        decoding="async"
      />
      <img
        src="@/assets/flower_lavender_purple_ribbon_trans.webp"
        class="right-lavender-ribbon-img"
        alt="Right Lavender Purple Ribbon Bouquet"
        draggable="false"
        decoding="async"
      />
      <img
        src="@/assets/purple_white_tulip_ribbon_trans.webp"
        class="right-tulip-ribbon-bg-img"
        alt="Right Purple White Tulip Ribbon Bouquet"
        draggable="false"
        decoding="async"
      />
      <img
        src="@/assets/anemone_colorful_bouquet_trans.webp"
        class="right-anemone-bg-img"
        alt="Right Colorful Anemone Bouquet"
        draggable="false"
        decoding="async"
      />
      <img
        src="@/assets/flower_pink_lisianthus_branch_trans.webp"
        class="right-lisianthus-bg-img"
        alt="Right Pink Lisianthus Branch"
        draggable="false"
        decoding="async"
      />
      <img
        src="@/assets/flower_tulip_lilac_spring_trans.webp"
        class="right-flower-img"
        alt="Right Spring Tulip & Lilac Flower"
        draggable="false"
        decoding="async"
      />
      <img
        src="@/assets/flower_tulip_purple_pink_bouquet_trans.webp"
        class="right-calla-flower-img"
        alt="Right Tulip & Lilac Bouquet"
        draggable="false"
        decoding="async"
      />
      <img
        src="@/assets/flower_purple_tulip_cluster_trans.webp"
        class="right-purple-tulip-cluster-img"
        alt="Right Purple Tulip Cluster"
        draggable="false"
        decoding="async"
      />
    </div>

    <!-- ── Center Floral Accent ── -->
    <div class="center-flower-wrap" aria-hidden="true">
      <img
        src="@/assets/flower_yellow_purple_bouquet_trans.webp"
        class="center-flower-img"
        alt="Center Yellow & Purple Flower"
        draggable="false"
        decoding="async"
      />
    </div>

    <!-- ── Bottom Purple Floral Border Background ── -->
    <div class="bottom-floral-bg-wrap" aria-hidden="true">
      <img
        src="@/assets/purple_floral_border_trans.webp"
        class="bottom-floral-bg-img"
        alt="Purple Floral Border Background"
        draggable="false"
        decoding="async"
      />
    </div>

  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import FloatingPetals from '@/components/FloatingPetals.vue'
import ButterflyEffect from '@/components/ButterflyEffect.vue'
import CountdownTimer from '@/components/CountdownTimer.vue'
import GoldDivider from '@/components/GoldDivider.vue'
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
