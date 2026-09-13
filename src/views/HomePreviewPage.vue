<template>
  <div class="home-preview-page">

    <FloatingPetals />
    <ButterflyEffect theme="white" />
       
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

    

    <div class="scrollable-snap-wrapper" ref="scrollContainer">
      
      <section class="snap-page section-invitation-cover" id="page-invite">
        <div class="invitation-content fade-in" :class="{ visible: entered }" style="--delay: 0.35s">
          
          <h1 class="main-wedding-title">សិរីមង្គលអាពាហ៍ពិពាហ៍</h1>

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

          <div class="honor-invite-title">
            <img
              src="@/assets/gold_baroque_pediment_trans.webp"
              class="honor-ornament-wing honor-ornament-left"
              alt="Gold Ornament Left"
              draggable="false"
              decoding="async"
            />
            <span class="honor-invite-text">មានកិត្តិយសសូមគោរពអញ្ជើញ</span>
            <img
              src="@/assets/gold_baroque_pediment_trans.webp"
              class="honor-ornament-wing honor-ornament-right"
              alt="Gold Ornament Right"
              draggable="false"
              decoding="async"
            />
          </div>

          <div class="formal-invitation-text">
            <p>ឯកឧត្តម លោកជំទាវ អ្នកឧកញ៉ា ឧកញ៉ា លោក លោកស្រី អ្នកនាង កញ្ញា</p>
            <p>អញ្ជើញចូលរួមជាអធិបតី និងភ្ញៀវកិត្តិយស ដើម្បីប្រសិទ្ធពរជ័យ សិរីសួស្តីជ័យមង្គលក្នុង</p>
            <p>ពិធីសិរីមង្គលអាពាហ៍ពិពាហ៍កូនប្រុស កូនស្រីរបស់យើងខ្ញុំ</p>
          </div>

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

          <div class="wedding-datetime-section">
            <p class="khmer-lunar-date">នៅថ្ងៃសៅរ៍ ៦កើត ខែផល្គុន ឆ្នាំមមី អដ្ឋស័ក ពុទ្ធសករាជ ២៥៧០</p>
            <p class="solar-date-highlight">ត្រូវនឹងថ្ងៃទី ១៣ ខែមីនា ឆ្នាំ ២០២៧</p>
            <p class="reception-time">វេលាម៉ោង ០៥ : ០០ ល្ងាចនៅ</p>
          </div>

          <div class="venue-section">
            <h3 class="venue-main-name">គេហដ្ឋាននៃសិរីមង្គលអាពាហ៍ពិពាហ៍</h3>
            <p class="venue-address-line">ស្ថិតនៅ ស្រុកសំពៅលូន ខេត្តបាត់ដំបង</p>
            <p class="venue-closing-wish">ដោយមេត្រីភាព។</p>
          </div>

          <button
            type="button"
            class="scroll-down-cue scroll-down-banner-btn"
            @click="scrollToPage('page-countdown')"
            aria-label="Scroll to next section"
          >
            <img
              src="@/assets/gold_ribbon_banner_new_trans.webp"
              class="scroll-down-banner-img"
              alt="Scroll to details"
              draggable="false"
              decoding="async"
            />
            <div class="scroll-down-banner-inner">
              <span class="scroll-down-banner-text">អូសឡើងទៅលើ</span>
            </div>
          </button>

        </div>
      </section> 
    </div>

    <div class="bottom-page-wildflower-bg" aria-hidden="true">
      <img
        src="@/assets/wildflower_border_uploaded_trans.webp"
        class="bottom-wildflower-tile bottom-wildflower-1"
        alt="Bottom Wildflower Background Border"
        draggable="false"
        decoding="async"
      />
      <img
        src="@/assets/wildflower_border_uploaded_trans.webp"
        class="bottom-wildflower-tile bottom-wildflower-2"
        alt="Bottom Wildflower Background Border"
        draggable="false"
        decoding="async"
      />
      <img
        src="@/assets/wildflower_border_uploaded_trans.webp"
        class="bottom-wildflower-tile bottom-wildflower-3"
        alt="Bottom Wildflower Background Border"
        draggable="false"
        decoding="async"
      />
      <img
        src="@/assets/wildflower_border_uploaded_trans.webp"
        class="bottom-wildflower-tile bottom-wildflower-4"
        alt="Bottom Wildflower Background Border"
        draggable="false"
        decoding="async"
      />
    </div>

    <img
        src="@/assets/wedding_flower_cluster_trans.webp"
        class="wedding_flower_cluster_trans"
        alt="Left Floral Accent"
        draggable="false"
        decoding="async"
      />

      <img
        src="@/assets/purple_carnation_uploaded_trans.webp"
        class="purple_carnation_uploaded_trans"
        alt="Left Floral Accent"
        draggable="false"
        decoding="async"
      />

      <img
        src="@/assets/purple_roses_bouquet_bloom_reverted_trans.webp"
        class="purple_roses_bouquet_bloom_trans"
        alt="Left Floral Accent"
        draggable="false"
        decoding="async"
      />

      <img
        src="@/assets/pink_lisianthus_uploaded_trans.webp"
        class="pink_lisianthus_uploaded_trans"
        alt="Left Floral Accent"
        draggable="false"
        decoding="async"
      />


<!--Right bottom  Image -->

    <img
        src="@/assets/pink_carnation_trio_uploaded_trans.webp"
        class="bicolor_roses_original_upright_right_trans"
        alt="Left Floral Accent"
        draggable="false"
        decoding="async"
      />

    <img
        src="@/assets/purple_peonies_bloom_trans.webp"
        class="purple_roses_hanging_chandelier_right_trans"
        alt="Left Floral Accent"
        draggable="false"
        decoding="async"
      />
    
    <img
        src="@/assets/wedding_flower_cluster_trans.webp"
        class="right-wedding_flower_cluster_trans"
        alt="Right Floral Accent"
        draggable="false"
        decoding="async"
      />
    
      <img
        src="@/assets/purple_carnation_uploaded_trans.webp"
        class="right-purple_carnation_uploaded_trans"
        alt="Left Floral Accent"
        draggable="false"
        decoding="async"
      />
      <img
        src="@/assets/pink_carnation_trio_uploaded_trans.webp"
        class="right-bicolor_roses_original_upright_right_trans"
        alt="Left Floral Accent"
        draggable="false"
        decoding="async"
      />

    <img
        src="@/assets/purple_peonies_bloom_trans.webp"
        class="right-purple_roses_hanging_chandelier_trans"
        alt="Left Floral Accent"
        draggable="false"
        decoding="async"
      />

      
      <img
        src="@/assets/purple_roses_bouquet_bloom_trans.webp"
        class="right-purple_roses_bouquet_bloom_trans"
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
