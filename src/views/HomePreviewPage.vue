<!--
  HomePreviewPage.vue
  Digital Wedding Invitation Preview & Details Page
-->
<template>
  <div class="home-preview-page">

    <!-- ── Ambient Floating Petals & Butterflies ── -->
    <FloatingPetals />
    <ButterflyEffect theme="white" />

    <!-- ── Top Navigation Bar ── -->
    <header class="preview-nav-bar">
      <button
        type="button"
        class="btn-back-nav"
        @click="goBackToCover"
        aria-label="Back to Cover"
      >
        <span>←</span>
        <span>ទំព័រគម្រប</span>
      </button>

      <span class="preview-badge">Wedding Invitation</span>
    </header>

    <!-- ── Luxury Chandelier Hanging from Top ── -->
    <section class="chandelier-section" aria-hidden="true">
      <div class="chandelier-glow-backdrop"></div>
      <img
        src="@/assets/chandelier_trans.webp"
        class="chandelier-img"
        alt="Crystal Wedding Chandelier"
        draggable="false"
      />
    </section>

    <!-- ── Hero Greeting ── -->
    <section class="hero-greeting-block">
      <h1 class="khmer-ceremony-title">{{ invitation.khmerGreeting }}</h1>
      <p class="khmer-ceremony-sub">{{ invitation.khmerSubtitle[0] || 'សូមគោរពអញ្ជើញចូលរួម' }}</p>
    </section>



    <!-- ── Left Side Floral Accent ── -->
    <div class="left-flower-wrap" aria-hidden="true">
      <img
        src="@/assets/flower_pink_lisianthus_branch_trans.webp"
        class="left-lisianthus-bg-img"
        alt="Left Pink Lisianthus Branch"
        draggable="false"
      />
      <img
        src="@/assets/flower_tulip_lilac_spring_trans.webp"
        class="left-flower-img"
        alt="Left Spring Tulip & Lilac Flower"
        draggable="false"
      />
      <img
        src="@/assets/flower_tulip_purple_pink_bouquet_trans.webp"
        class="left-calla-flower-img"
        alt="Left Calla Lily & Purple Rose Bouquet"
        draggable="false"
      />
      <img
        src="@/assets/flower_purple_tulip_cluster_trans.webp"
        class="left-purple-tulip-cluster-img"
        alt="Left Purple Tulip Cluster"
        draggable="false"
      />
    </div>

    <!-- ── Right Side Floral Accent ── -->
    <div class="right-flower-wrap" aria-hidden="true">
      <img
        src="@/assets/flower_pink_lisianthus_branch_trans.webp"
        class="right-lisianthus-bg-img"
        alt="Right Pink Lisianthus Branch"
        draggable="false"
      />
      <img
        src="@/assets/flower_tulip_lilac_spring_trans.webp"
        class="right-flower-img"
        alt="Right Spring Tulip & Lilac Flower"
        draggable="false"
      />
      <img
        src="@/assets/flower_tulip_purple_pink_bouquet_trans.webp"
        class="right-calla-flower-img"
        alt="Right Tulip & Lilac Bouquet"
        draggable="false"
      />
      <img
        src="@/assets/flower_purple_tulip_cluster_trans.webp"
        class="right-purple-tulip-cluster-img"
        alt="Right Purple Tulip Cluster"
        draggable="false"
      />
    </div>

    <!-- ── Center Floral Accent ── -->
    <div class="center-flower-wrap" aria-hidden="true">
      <img
        src="@/assets/flower_yellow_purple_bouquet_trans.webp"
        class="center-flower-img"
        alt="Center Yellow & Purple Flower"
        draggable="false"
      />
    </div>

    <!-- ── Bottom Purple Floral Border Background ── -->
    <div class="bottom-floral-bg-wrap" aria-hidden="true">
      <img
        src="@/assets/purple_floral_border_trans.webp"
        class="bottom-floral-bg-img"
        alt="Purple Floral Border Background"
        draggable="false"
      />
    </div>

  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
import FloatingPetals from '@/components/FloatingPetals.vue'
import ButterflyEffect from '@/components/ButterflyEffect.vue'
import CountdownTimer from '@/components/CountdownTimer.vue'
import GoldDivider from '@/components/GoldDivider.vue'
import invitation from '@/config/invitation.js'

const router = useRouter()

function goBackToCover() {
  router.push({ name: 'cover' })
}

</script>

<style scoped src="./HomePreviewPage.css"></style>
