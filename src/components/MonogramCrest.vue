<!--
  MonogramCrest.vue
  Golden ornamental crest with the couple's initials rendered as an inline SVG.
  Props:
    - initials: Array of two strings, e.g. ['P', 'S']
    - size: CSS width value (default '240px')
-->
<template>
  <svg
    class="crest-svg"
    :style="{ width: size }"
    viewBox="0 0 280 220"
    xmlns="http://www.w3.org/2000/svg"
    role="img"
    :aria-label="`Monogram crest for ${initials[0]} and ${initials[1]}`"
  >
    <defs>
      <linearGradient id="crest-gold" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%"   stop-color="#f5d98e"/>
        <stop offset="25%"  stop-color="#d4a43a"/>
        <stop offset="50%"  stop-color="#a07018"/>
        <stop offset="75%"  stop-color="#d4a43a"/>
        <stop offset="100%" stop-color="#f5d98e"/>
      </linearGradient>
      <filter id="crest-glow">
        <feGaussianBlur stdDeviation="2.5" result="blur"/>
        <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
      </filter>
      <filter id="crest-shadow">
        <feDropShadow dx="0" dy="3" stdDeviation="6" flood-color="#9e6e10" flood-opacity="0.25"/>
      </filter>
    </defs>

    <!-- Outer + inner rings -->
    <circle cx="140" cy="110" r="88" fill="none" stroke="url(#crest-gold)"
            stroke-width="2.5" filter="url(#crest-glow)"/>
    <circle cx="140" cy="110" r="80" fill="none" stroke="url(#crest-gold)"
            stroke-width="0.8" opacity="0.45"/>

    <!-- Crown top -->
    <polygon points="140,4 148,20 132,20" fill="url(#crest-gold)"/>
    <circle cx="140" cy="4"   r="4"   fill="url(#crest-gold)" filter="url(#crest-glow)"/>
    <circle cx="116" cy="14"  r="3"   fill="url(#crest-gold)"/>
    <circle cx="164" cy="14"  r="3"   fill="url(#crest-gold)"/>
    <!-- Crown arch -->
    <path d="M 90 38 C 108 15, 172 15, 190 38"
          fill="none" stroke="url(#crest-gold)" stroke-width="1.8" opacity="0.65"/>
    <!-- Top baroque flourishes -->
    <path d="M 78 46 C 82 28, 102 22, 108 32 C 110 37, 106 42, 102 40"
          fill="none" stroke="url(#crest-gold)" stroke-width="2" stroke-linecap="round"/>
    <path d="M 202 46 C 198 28, 178 22, 172 32 C 170 37, 174 42, 178 40"
          fill="none" stroke="url(#crest-gold)" stroke-width="2" stroke-linecap="round"/>

    <!-- Side scrolls -->
    <path d="M 40 110 C 22 95, 18 70, 36 58 C 48 50, 58 58, 52 68 C 46 78, 34 74, 38 62"
          fill="none" stroke="url(#crest-gold)" stroke-width="2" stroke-linecap="round"/>
    <path d="M 240 110 C 258 95, 262 70, 244 58 C 232 50, 222 58, 228 68 C 234 78, 246 74, 242 62"
          fill="none" stroke="url(#crest-gold)" stroke-width="2" stroke-linecap="round"/>

    <!-- Bottom swag -->
    <path d="M 68 185 C 90 207, 140 214, 212 185"
          fill="none" stroke="url(#crest-gold)" stroke-width="2" stroke-linecap="round"/>
    <path d="M 84 193 C 102 211, 140 216, 196 193"
          fill="none" stroke="url(#crest-gold)" stroke-width="1" opacity="0.55"/>
    <circle cx="140" cy="214" r="4"   fill="url(#crest-gold)"/>
    <circle cx="93"  cy="201" r="2.5" fill="url(#crest-gold)"/>
    <circle cx="187" cy="201" r="2.5" fill="url(#crest-gold)"/>

    <!-- Cream paper fill -->
    <circle cx="140" cy="110" r="76" fill="rgba(253,248,240,0.42)"/>

    <!-- Cardinal accent dots -->
    <circle cx="140" cy="30"  r="2.5" fill="url(#crest-gold)"/>
    <circle cx="52"  cy="110" r="2.5" fill="url(#crest-gold)"/>
    <circle cx="228" cy="110" r="2.5" fill="url(#crest-gold)"/>
    <circle cx="140" cy="190" r="2.5" fill="url(#crest-gold)"/>

    <!-- Monogram initials -->
    <text x="102" y="136"
          font-family="Cinzel, serif" font-size="60" font-weight="700"
          fill="url(#crest-gold)" filter="url(#crest-glow)"
          text-anchor="middle">{{ initials[0] }}</text>
    <text x="178" y="136"
          font-family="Cinzel, serif" font-size="60" font-weight="700"
          fill="url(#crest-gold)" filter="url(#crest-glow)"
          text-anchor="middle">{{ initials[1] }}</text>
    <!-- Ampersand between -->
    <text x="140" y="126"
          font-family="Alex Brush, cursive" font-size="28"
          fill="url(#crest-gold)" opacity="0.85"
          text-anchor="middle">&amp;</text>
  </svg>
</template>

<script setup>
defineProps({
  initials: { type: Array, default: () => ['P', 'S'] },
  // 52vw ≈ 208px on a 400px phone — fills nicely without crowding
  size:     { type: String, default: 'min(52vw, 210px)' },
})
</script>

<style scoped>
.crest-svg {
  display: block;
  height: auto;
  filter: drop-shadow(0 6px 20px rgba(160, 112, 24, 0.28));
}
</style>
