<template>
  <div class="vp-root">

    <!-- ══ CINEMATIC ANIMATION STAGE ══════════════════════════ -->
    <div class="vp-stage" aria-label="Wedding invitation animation">

      <!-- SCENE 1: Palace Gate -->
      <div class="vp-scene vp-scene-gate">
        <div class="vp-scene-bg vp-gate-bg"></div>
      </div>

      <!-- SCENE 2: Courtyard -->
      <div class="vp-scene vp-scene-courtyard">
        <div class="vp-scene-bg vp-courtyard-bg"></div>

        <!-- Satin curtains draping from top -->
        <div class="vp-curtain-left"></div>
        <div class="vp-curtain-right"></div>
        <div class="vp-lace-border"></div>

        <!-- Text reveal -->
        <div class="vp-text-overlay">
          <p class="vp-text-script">The Wedding of</p>
          <h1 class="vp-text-names">
            <span class="vp-name-line vp-name-tiara">TIARA</span>
            <span class="vp-name-amp">&amp;</span>
            <span class="vp-name-line vp-name-vega">VEGA</span>
          </h1>
        </div>
      </div>

      <!-- Floating petals overlay -->
      <div class="vp-petals" aria-hidden="true">
        <span v-for="i in 18" :key="i" class="vp-petal" :class="`vp-petal-${i}`"></span>
      </div>

    </div>

    <!-- ══ INFO PANEL ══════════════════════════════════════════ -->
    <div class="vp-info-panel">

      <header class="vp-info-header">
        <button class="vp-back-btn" @click="goBack" aria-label="Go Back">
          <span>&#8592;</span> Back
        </button>
        <span class="vp-info-tag">&#127916; CSS Animation &#8212; 20s Loop</span>
      </header>

      <div class="vp-info-block">
        <h2 class="vp-info-title"><span>&#128204;</span> Overview</h2>
        <p class="vp-info-text">
          A <strong>luxury baroque wedding invitation</strong> animation &#8212; recreated entirely in CSS.
          A cinematic zoom takes the viewer through an ornate palace gate into a grand courtyard,
          revealing the couple&#39;s names in deep navy serif typography.
        </p>
      </div>

      <div class="vp-info-block">
        <h2 class="vp-info-title"><span>&#128444;&#65039;</span> Scene Breakdown</h2>
        <div class="vp-timeline">
          <div class="vp-timeline-item" v-for="s in sceneInfo" :key="s.time">
            <div class="vp-tl-time">{{ s.time }}</div>
            <div class="vp-tl-bar"></div>
            <div class="vp-tl-body">
              <strong>{{ s.name }}</strong>
              <p>{{ s.desc }}</p>
            </div>
          </div>
        </div>
      </div>

      <div class="vp-info-block">
        <h2 class="vp-info-title"><span>&#127807;</span> Visual Elements</h2>
        <div class="vp-tags">
          <span class="vp-tag" v-for="el in elements" :key="el">{{ el }}</span>
        </div>
      </div>

    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

const sceneInfo = [
  { time: '0:00-0:08', name: 'Palace Gate - Ken Burns Zoom',  desc: 'Baroque gate zooms slowly inward. Pastel florals gently sway. Petals drift across the scene.' },
  { time: '0:08-0:14', name: 'Zoom-Through Transition',       desc: 'Gate scales up to fill the frame, crossfading into the grand courtyard with peacocks and fountain.' },
  { time: '0:14-0:18', name: 'Courtyard & Name Reveal',       desc: '"The Wedding of" fades in first in italic script, followed by "TIARA & VEGA" scaling up in bold navy.' },
  { time: '0:18-0:20', name: 'Fade Return - Loop',            desc: 'Courtyard gently fades back to the gate scene, creating a seamless 20-second loop.' },
]

const elements = [
  '&#127963;&#65039; Baroque Gate', '&#127800; Pastel Florals', '&#129412; Peacocks',
  '&#9842; Marble Fountain', '&#127919; Satin Curtains', '&#129697; Lace Overlay',
  '&#10024; Gold Accents', '&#128153; Powder Blue Sky', '&#127807; Botanical Gardens',
]

function goBack() {
  router.back()
}
</script>

<style scoped src="./VideoPreView.css"></style>
