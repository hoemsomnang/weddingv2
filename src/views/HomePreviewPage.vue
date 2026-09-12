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
      <img
        src="@/assets/fairytale_palace_purple_stairs_trans.webp"
        class="preview-fullscreen-palace-img"
        alt="Fairytale Palace Purple Stairs Background"
        draggable="false"
        decoding="async"
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

    <!-- ── Top-Left Wisteria Hanging Accent ── -->
    <img
      src="@/assets/wisteria_hanging_clusters_trans.webp"
      class="top-left-wisteria-img"
      alt="Top Left Wisteria Hanging Blossom"
      draggable="false"
      decoding="async"
    />
    <img
      src="@/assets/wisteria_hanging_clusters_trans.webp"
      class="top-left-wisteria-img-1"
      alt="Top Left Wisteria Hanging Blossom"
      draggable="false"
      decoding="async"
    />

    <img
      src="@/assets/wisteria_hanging_clusters_trans.webp"
      class="top-left-wisteria-img-2"
      alt="Top Left Wisteria Hanging Blossom"
      draggable="false"
      decoding="async"
    />

    <img
      src="@/assets/purple_lavender_blooming_roses_down_right_trans.webp"
      class="top-left-purple_lavender"
      alt="Top Left Wisteria Hanging Blossom"
      draggable="false"
      decoding="async"
    />

    <img
      src="@/assets/purple_roses_hanging_chandelier_right_trans.webp"
      class="top-left-purple_roses"
      alt="Top Left Wisteria Hanging Blossom"
      draggable="false"
      decoding="async"
    />

    <img
      src="@/assets/original_dense_roses_reverted_down_right_trans.webp"
      class="top-left-purple_roses_1"
      alt="Top Left Wisteria Hanging Blossom"
      draggable="false"
      decoding="async"
    />

    <img
      src="@/assets/bicolor_roses_original_down_right_trans.webp"
      class="top-left-purple_roses_2"
      alt="Top Left Wisteria Hanging Blossom"
      draggable="false"
      decoding="async"
    />
    
    <img
      src="@/assets/blooming_roses_bouquet_down_right_trans.webp"
      class="top-left-purple_roses_3"
      alt="Top Left Wisteria Hanging Blossom"
      draggable="false"
      decoding="async"
    />

     <img
      src="@/assets/twotone_purple_roses_down_right_trans.webp"
      class="top-left-purple_roses_4"
      alt="Top Left Wisteria Hanging Blossom"
      draggable="false"
      decoding="async"
    />

    <!-- ── Top-Right Wisteria Hanging Accent ── -->
    <img
      src="@/assets/wisteria_hanging_clusters_right_trans.webp"
      class="top-right-wisteria-img"
      alt="Top Right Wisteria Hanging Blossom"
      draggable="false"
      decoding="async"
    />

    <img
      src="@/assets/wisteria_hanging_clusters_right_trans.webp"
      class="top-right-wisteria-img-1"
      alt="Top Right Wisteria Hanging Blossom"
      draggable="false"
      decoding="async"
    />
    
    <img
      src="@/assets/purple_lavender_blooming_roses_down_trans.webp"
      class="top-right-purple_lavender"
      alt="Top Left Wisteria Hanging Blossom"
      draggable="false"
      decoding="async"
    />

    <img
      src="@/assets/purple_roses_hanging_chandelier_trans.webp"
      class="top-right-purple_roses"
      alt="Top Left Wisteria Hanging Blossom"
      draggable="false"
      decoding="async"
    />

    <img
      src="@/assets/original_dense_roses_reverted_down_trans.webp"
      class="top-right-purple_roses_1"
      alt="Top Left Wisteria Hanging Blossom"
      draggable="false"
      decoding="async"
    />

    <img
      src="@/assets/bicolor_roses_original_down_trans.webp"
      class="top-right-purple_roses_2"
      alt="Top Left Wisteria Hanging Blossom"
      draggable="false"
      decoding="async"
    />

   <img
      src="@/assets/blooming_roses_bouquet_down_trans.webp"
      class="top-right-purple_roses_3"
      alt="Top Left Wisteria Hanging Blossom"
      draggable="false"
      decoding="async"
    />

    




    <!-- Scrollable Snap-Paged Container -->
    <div class="scrollable-snap-wrapper" ref="scrollContainer">
      
      <!-- ==========================================
           PAGE 1: MAIN INVITATION CARD (Photo 2)
           ========================================== -->
      <section class="snap-page section-invitation-cover" id="page-invite">
        <div class="invitation-content fade-in" :class="{ visible: entered }" style="--delay: 0.35s">
          
          <!-- Main Wedding Ceremony Title -->
          <h1 class="main-wedding-title">សិរីមង្គលអាពាហ៍ពិពាហ៍</h1>

          <!-- Parents Section (2 Columns) -->
          <div class="parents-grid">
            <div class="parent-col left-col">
              <div class="parent-row">
                <span class="role-text">លោក</span>
                <span class="name-text">ហ៊ឹម លាង</span>
              </div>
              <div class="parent-row">
                <span class="role-text">លោកស្រី</span>
                <span class="name-text">អ៊ុំ ស្រ៊ឺ</span>
              </div>
            </div>

            <div class="parent-col right-col">
              <div class="parent-row">
                <span class="role-text">លោក</span>
                <span class="name-text">ឃន សារ៉េត</span>
              </div>
              <div class="parent-row">
                <span class="role-text">លោកស្រី</span>
                <span class="name-text">ធា ម៉ុំ</span>
              </div>
            </div>
          </div>

          <!-- Invitation Subtitle -->
          <div class="honor-invite-title">
            មានកិត្តិយសសូមគោរពអញ្ជើញ
          </div>

          <!-- Formal Invitation Body Text -->
          <div class="formal-invitation-text">
            <p>ឯកឧត្តម លោកជំទាវ អ្នកឧកញ៉ា ឧកញ៉ា លោក លោកស្រី អ្នកនាង កញ្ញា</p>
            <p>អញ្ជើញចូលរួមជាអធិបតី និងភ្ញៀវកិត្តិយស ដើម្បីប្រសិទ្ធពរជ័យ សិរីសួស្តីជ័យមង្គលក្នុង</p>
            <p>ពិធីសិរីមង្គលអាពាហ៍ពិពាហ៍កូនប្រុស កូនស្រីរបស់យើងខ្ញុំ</p>
          </div>

          <!-- Groom & Bride Names (2 Columns) -->
          <div class="couple-names-grid">
            <div class="couple-col groom-col">
              <span class="couple-role">កូនប្រុសនាម</span>
              <h2 class="couple-name">ហ៊ឹម សំណាង</h2>
            </div>
            <div class="couple-col bride-col">
              <span class="couple-role">កូនស្រីនាម</span>
              <h2 class="couple-name">ឃន សារ៉េន</h2>
            </div>
          </div>

          <!-- Wedding Auspicious Date & Time -->
          <div class="wedding-datetime-section">
            <p class="khmer-lunar-date">នៅថ្ងៃសៅរ៍ ៦កើត ខែផល្គុន ឆ្នាំមមី អដ្ឋស័ក ពុទ្ធសករាជ ២៥៧០</p>
            <p class="solar-date-highlight">ត្រូវនឹងថ្ងៃទី ១៣ ខែមីនា ឆ្នាំ ២០២៧</p>
            <p class="reception-time">វេលាម៉ោង ០៥ : ០០ ល្ងាចនៅ</p>
          </div>

          <!-- Wedding Reception Venue -->
          <div class="venue-section">
            <h3 class="venue-main-name">គេហដ្ឋាននៃសិរីមង្គលអាពាហ៍ពិពាហ៍</h3>
            <p class="venue-address-line">ស្ថិតនៅ ស្រុកសំពៅលូន ខេត្តបាត់ដំបង</p>
            <p class="venue-closing-wish">ដោយមេត្រីភាព។</p>
          </div>

          <!-- Scroll Down Prompt Indicator -->
          <div class="scroll-down-cue" @click="scrollToPage('page-countdown')">
            <ChevronDown :size="22" class="bounce-down-icon" />
          </div>

        </div>
      </section> 
    </div>

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

      <img
        src="@/assets/purple_lily_vase_bouquet_trans.webp"
        class="left-purple_lily_vase_bouquet_trans" 
        alt="Left Floral Accent"
        draggable="false"
        decoding="async"
      />

      <img
        src="@/assets/magenta_purple_rose_dew_trans.webp"
        class="left-magenta_purple_rose_dew_trans" 
        alt="Left Floral Accent"
        draggable="false"
        decoding="async"
      />

    <img
        src="@/assets/magenta_purple_rose_dew_right_trans.webp"
        class="left-magenta_purple" 
        alt="Left Floral Accent"
        draggable="false"
        decoding="async"
      />

          <img
        src="@/assets/purple_rose_dew_bloom_right_trans.webp"
        class="left-magenta_purple_1" 
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
        src="@/assets/purple_rose_dew_ref2_right_trans.webp"
        class="right-purple_rose_dew_ref2_trans"
        alt="Right Floral Accent"
        draggable="false"
        decoding="async"
      />
      <img
        src="@/assets/purple_rose_dew_ref1_right_trans.webp"
        class="right-purple_rose_dew_ref1_trans" 
        alt="Right Floral Accent"
        draggable="false"
        decoding="async"
      />

      <img
        src="@/assets/purple_lily_vase_bouquet_right_trans.webp"
        class="right-purple_lily_vase_bouquet_trans" 
        alt="Right Floral Accent"
        draggable="false"
        decoding="async"
      />


    <img
        src="@/assets/magenta_purple_rose_dew_right_trans.webp"
        class="right-magenta_purple_rose_dew_trans" 
        alt="Right Floral Accent"
        draggable="false"
        decoding="async"
      />
     

     <img
        src="@/assets/magenta_purple_rose_dew_trans.webp"
        class="right-magenta_purple" 
        alt="Right Floral Accent"
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
import ChevronDown from '@/components/ChevronDown.vue'
import invitation from '@/config/invitation.js'

const router = useRouter()
const scrollContainer = ref(null)

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
