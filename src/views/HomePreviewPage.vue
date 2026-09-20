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
              class="agenda-day-card"
            >
              <!-- Day Header Banner -->
              <div class="agenda-day-header anim-item anim-delay-3">
                <span class="agenda-header-ornament">❖</span>
                <h3 class="agenda-day-title">{{ day.dayTitle }}</h3>
                <span class="agenda-header-ornament">❖</span>
              </div>

              <!-- Timeline Items List -->
              <div class="agenda-timeline">
                <div
                  v-for="(item, sIndex) in day.schedule"
                  :key="sIndex"
                  class="agenda-timeline-row anim-item"
                  :class="`anim-delay-${sIndex + 4}`"
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
                    <img
                      src="@/assets/khmer_gold_rosette_trans.webp"
                      class="agenda-rosette-bullet"
                      alt="Ornament"
                      draggable="false"
                      decoding="async"
                    />
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

      <!-- ── Section 4: Wedding Location / Venue Map ────────────── -->
      <section class="snap-page section-location" id="page-location">
        <div class="location-content" :class="{ 'section-animate-in': isLocationInView }">

          <!-- 1. Location Header Title -->
          <div class="location-header-wrap anim-item anim-delay-1">
            <h2 class="location-title">{{ invitation.venueTitle }}</h2>
          </div>

          <!-- 2. Gold Ornate Divider -->
          <div class="location-divider-wrap anim-item anim-delay-2">
            <img
              src="@/assets/gold_divider_ornate.webp"
              class="location-ornate-divider"
              alt="Divider"
              draggable="false"
              decoding="async"
            />
          </div>

          <!-- 3. Venue Details Card -->
          <div class="location-info-card anim-item anim-delay-3">
            <div class="location-venue-badge">
              <img
                src="@/assets/khmer_gold_rosette_trans.webp"
                class="location-badge-icon"
                alt="Rosette"
                draggable="false"
                decoding="async"
              />
              <span class="location-venue-name">{{ invitation.venueName }}</span>
              <img
                src="@/assets/khmer_gold_rosette_trans.webp"
                class="location-badge-icon"
                alt="Rosette"
                draggable="false"
                decoding="async"
              />
            </div>

            <p class="location-address-text">{{ invitation.venueAddress }}</p>
            <p class="location-time-badge">{{ invitation.venueReceptionTime }}</p>
          </div>

          <!-- 4. Interactive Stylized Map Card -->
          <div class="location-map-container anim-item anim-delay-4">
            <div class="location-map-frame">
              <iframe
                title="Wedding Venue Location Map"
                :src="invitation.venueEmbedUrl || 'https://maps.google.com/maps?q=13.489456,102.368097&hl=km&z=16&output=embed'"
                class="location-map-iframe"
                loading="lazy"
                allowfullscreen
              ></iframe>
              <div class="location-map-overlay" @click="openGoogleMaps" title="Open in Google Maps">
                <img
                  src="@/assets/gold_map_marker_pin_trans.webp"
                  class="location-pin-pulse-img"
                  alt="Map Location Pin"
                  draggable="false"
                  decoding="async"
                />
              </div>
            </div>
          </div>

          <!-- 5. Open in Google Maps Action Button -->
          <div class="location-action-wrap anim-item anim-delay-5">
            <button
              type="button"
              class="location-directions-btn"
              @click="openGoogleMaps"
              aria-label="Open in Google Maps"
            >
              <img
                src="@/assets/gold_wedding_pin_trans.webp"
                class="location-btn-pin-icon"
                alt="Location Pin"
                draggable="false"
                decoding="async"
              />
              <span class="location-btn-text">{{ invitation.venueButtonText }}</span>
            </button>
          </div>

          <!-- 6. Warm Closing Wish -->
          <p class="location-closing-wish anim-item anim-delay-6">
            « {{ invitation.venueClosingWish }} »
          </p>

        </div>
      </section>

      <!-- ── Section 5: Photo Gallery (វិចិត្រសាល) ──────────────── -->
      <section class="snap-page section-gallery" id="page-gallery">
        <div class="gallery-content" :class="{ 'section-animate-in': isGalleryInView }">

          <!-- 1. Header Title & Subtitle -->
          <div class="gallery-header-wrap anim-item anim-delay-1">
            <h2 class="gallery-title">{{ invitation.galleryTitle || 'វិចិត្រសាល' }}</h2>
          </div>

          <!-- 2. Gold Ornate Divider -->
          <div class="gallery-divider-wrap anim-item anim-delay-2">
            <img
              src="@/assets/gold_divider_ornate.webp"
              class="gallery-ornate-divider"
              alt="Divider"
              draggable="false"
              decoding="async"
            />
          </div>

          <!-- 3. Featured Photo Showcase Card with Smooth Slide Animation -->
          <div class="gallery-showcase-card anim-item anim-delay-3">
            <div
              class="gallery-main-frame"
              @touchstart="handleTouchStart"
              @touchmove="handleTouchMove"
              @touchend="handleTouchEnd"
              @mousedown="handleMouseDown"
              @mousemove="handleMouseMove"
              @mouseup="handleMouseUp"
              @mouseleave="handleMouseUp"
            >
              <!-- Sliding Track with Smooth Hardware-Accelerated Physics -->
              <div
                class="gallery-slider-track"
                :style="trackStyle"
              >
                <div
                  v-for="(photo, pIdx) in galleryPhotos"
                  :key="pIdx"
                  class="gallery-slide"
                  :class="{ 'is-active-slide': pIdx === currentPhotoIndex }"
                  @click="openLightbox(pIdx)"
                >
                  <img
                    :src="photo.src"
                    class="gallery-slide-img"
                    :class="{ 'is-kenburns': pIdx === currentPhotoIndex }"
                    :alt="photo.title"
                    draggable="false"
                  />
                  <!-- Subtle romantic vignette overlay -->
                  <div class="gallery-slide-overlay"></div>
                </div>
              </div>

              <!-- Golden Shimmer Light Sweep on active frame -->
              <div class="gallery-gold-sheen" :key="currentPhotoIndex"></div>

              <!-- Counter badge with smooth flip animation -->
              <div class="gallery-counter-badge">
                <transition name="count-flip" mode="out-in">
                  <span :key="currentPhotoIndex" class="count-num">{{ currentPhotoIndex + 1 }}</span>
                </transition>
                <span> / {{ galleryPhotos.length }}</span>
              </div>


              <!-- Navigation arrows on photo using Khmer Gold Rosette -->
              <button
                type="button"
                class="gallery-nav-arrow gallery-nav-prev"
                @click.stop="prevPhoto"
                aria-label="Previous photo"
              >
                <img
                  src="@/assets/khmer_gold_rosette_trans.webp"
                  class="gallery-nav-rosette-img"
                  alt=""
                  aria-hidden="true"
                  draggable="false"
                />
                <svg viewBox="0 0 24 24" class="gallery-nav-chevron" fill="none" stroke="currentColor" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M14.5 17.5L9 12l5.5-5.5" />
                </svg>
              </button>
              <button
                type="button"
                class="gallery-nav-arrow gallery-nav-next"
                @click.stop="nextPhoto"
                aria-label="Next photo"
              >
                <img
                  src="@/assets/khmer_gold_rosette_trans.webp"
                  class="gallery-nav-rosette-img"
                  alt=""
                  aria-hidden="true"
                  draggable="false"
                />
                <svg viewBox="0 0 24 24" class="gallery-nav-chevron" fill="none" stroke="currentColor" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M9.5 17.5L15 12 9.5 6.5" />
                </svg>
              </button>
            </div>

            <!-- Current Photo Caption with Glide Transition -->
            <div class="gallery-photo-caption">
              <transition name="caption-glide" mode="out-in">
                <span :key="currentPhotoIndex" class="gallery-caption-title">
                  {{ galleryPhotos[currentPhotoIndex].title }}
                </span>
              </transition>
            </div>
          </div>

          <!-- 4. Interactive Thumbnail Strip -->
          <div class="gallery-thumbs-row anim-item anim-delay-4">
            <button
              v-for="(photo, pIdx) in galleryPhotos"
              :key="pIdx"
              type="button"
              class="gallery-thumb-btn"
              :class="{ 'is-active': pIdx === currentPhotoIndex }"
              @click="selectPhoto(pIdx)"
              :aria-label="`Photo ${pIdx + 1}`"
            >
              <img
                :src="photo.src"
                class="gallery-thumb-img"
                alt="Thumbnail"
                draggable="false"
                loading="lazy"
              />
            </button>
          </div>

          <!-- 5. Warm Blessing / Romantic Quote -->
          <p class="gallery-closing-wish anim-item anim-delay-5">
            « {{ invitation.galleryWishes || 'ស្នាមញញឹមនៃក្តីស្រឡាញ់ និងអនុស្សាវរីយ៍ដ៏ផ្អែមល្ហែម' }} »
          </p>

        </div>
      </section>

      <!-- ── Section 6: Photo Album Grid (កម្រងរូបភាពអនុស្សាវរីយ៍) ────── -->
      <section class="snap-page section-album" id="page-album">
        <div class="album-content" :class="{ 'section-animate-in': isAlbumInView }">

          <!-- 1. Header Title & Subtitle -->
          <div class="album-header-wrap anim-item anim-delay-1">
            <h2 class="album-title">{{ invitation.albumTitle || 'កម្រងរូបភាពអនុស្សាវរីយ៍' }}</h2>
          </div>

          <!-- 2. Gold Ornate Divider -->
          <div class="album-divider-wrap anim-item anim-delay-2">
            <img
              src="@/assets/gold_divider_ornate.webp"
              class="album-ornate-divider"
              alt="Divider"
              draggable="false"
              decoding="async"
            />
          </div>

          <!-- 3. Photo Album Collage Grid with One-by-One Staggered Animation -->
          <div class="album-photo-grid">
            <div
              v-for="(photo, idx) in albumGridPhotos"
              :key="idx"
              class="album-grid-card anim-item"
              :class="[
                photo.wide ? 'album-card-wide' : (photo.tall ? 'album-card-tall' : 'album-card-medium'),
                `album-seq-${idx + 1}`
              ]"
              @click="openAlbumLightbox(idx)"
              role="button"
              :aria-label="photo.title"
            >
              <div class="album-card-inner">
                <img
                  :src="photo.src"
                  class="album-card-img"
                  :alt="photo.title"
                  draggable="false"
                  loading="lazy"
                />
                <div class="album-card-glint"></div>
              </div>
            </div>
          </div>

          <!-- 4. Warm Blessing / Romantic Quote -->
          <p class="album-closing-wish anim-item album-seq-8">
            « {{ invitation.albumWishes || 'ស្នាមញញឹម និងអនុស្សាវរីយ៍ដ៏មានតម្លៃមិនអាចបំភ្លេចបាន' }} »
          </p>

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

    <!-- ── Fullscreen Gallery Lightbox Modal ──────────────────── -->
    <teleport to="body">
      <transition name="lightbox-fade">
        <div
          v-if="isLightboxOpen"
          class="gallery-lightbox-backdrop"
          @click.self="closeLightbox"
        >
          <button
            type="button"
            class="lightbox-close-btn"
            @click="closeLightbox"
            aria-label="Close fullscreen view"
          >
            ✕
          </button>

          <div class="lightbox-content">
            <transition name="lightbox-zoom" mode="out-in">
              <img
                :key="lightboxIndex"
                :src="activeLightboxList[lightboxIndex].src"
                class="lightbox-img"
                :alt="activeLightboxList[lightboxIndex].title"
              />
            </transition>
            <div class="lightbox-caption">
              <span class="lightbox-title">{{ activeLightboxList[lightboxIndex].title }}</span>
              <span class="lightbox-counter">{{ lightboxIndex + 1 }} / {{ activeLightboxList.length }}</span>
            </div>
          </div>

          <button
            type="button"
            class="lightbox-nav-btn lightbox-prev"
            @click.stop="prevLightboxPhoto"
            aria-label="Previous photo"
          >
            ‹
          </button>
          <button
            type="button"
            class="lightbox-nav-btn lightbox-next"
            @click.stop="nextLightboxPhoto"
            aria-label="Next photo"
          >
            ›
          </button>
        </div>
      </transition>
    </teleport>

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

// ── Romantic Wedding Gallery & Album Photos ──
import albumBanner from '@/assets/gallery/album_01_banner.webp'
import galleryPhoto1 from '@/assets/gallery/gallery_01_royal.webp'
import galleryPhoto2 from '@/assets/gallery/gallery_02_traditional.webp'
import galleryPhoto3 from '@/assets/gallery/gallery_03_modern.webp'
import galleryPhoto4 from '@/assets/gallery/gallery_04_sunset.webp'
import galleryPhoto5 from '@/assets/gallery/gallery_05_intimate.webp'
import couplePortrait from '@/assets/couple_wedding_portrait.jpg'

const galleryPhotos = [
  { src: galleryPhoto1, title: 'រាជសិរីមង្គល', desc: 'Royal Elegance' },
  { src: galleryPhoto2, title: 'បុប្ផាជួបជុំ', desc: 'Garden of Love' },
  { src: galleryPhoto3, title: 'វិមានសុភមង្គល', desc: 'Palace Romance' },
  { src: galleryPhoto4, title: 'សន្ធ្យារស្មីស្នេហ៍', desc: 'Golden Sunset' },
  { src: galleryPhoto5, title: 'ចំណងស្នេហ៍និរន្តរ៍', desc: 'Everlasting Promise' },
]

const albumGridPhotos = [
  { src: albumBanner, title: 'ដង្ហែជំនូនមុខប្រាសាទអង្គរវត្ត', desc: 'Angkor Wat Royal Procession', wide: true },
  { src: galleryPhoto1, title: 'រាជសិរីមង្គល', desc: 'Royal Elegance' },
  { src: galleryPhoto2, title: 'បុប្ផាជួបជុំ', desc: 'Garden of Love' },
  { src: galleryPhoto4, title: 'សន្ធ្យារស្មីស្នេហ៍', desc: 'Golden Sunset' },
  { src: galleryPhoto5, title: 'ចំណងស្នេហ៍និរន្តរ៍', desc: 'Everlasting Promise' },
  { src: galleryPhoto3, title: 'វិមានសុភមង្គល', desc: 'Palace Romance', tall: true },
  { src: couplePortrait, title: 'សេចក្តីស្រឡាញ់ដ៏ស្មោះស្ម័គ្រ', desc: 'True Love', tall: true },
]

const currentPhotoIndex = ref(0)
const isLightboxOpen = ref(false)
const activeLightboxList = ref(galleryPhotos)
const lightboxIndex = ref(0)
const isDragging = ref(false)
const dragOffset = ref(0)
const slideDirection = ref('next')

const trackStyle = computed(() => {
  if (isDragging.value) {
    return {
      transform: `translateX(calc(-${currentPhotoIndex.value * 100}% + ${dragOffset.value}px))`,
      transition: 'none',
    }
  }
  return {
    transform: `translateX(-${currentPhotoIndex.value * 100}%)`,
    transition: 'transform 0.55s cubic-bezier(0.19, 1, 0.22, 1)',
  }
})

// ── Touch & Mouse Drag Physics for Gallery Slider ──
let dragStartX = 0
let dragCurrentX = 0

function handleTouchStart(e) {
  if (!e.touches || e.touches.length === 0) return
  isDragging.value = true
  dragStartX = e.touches[0].clientX
  dragCurrentX = dragStartX
  dragOffset.value = 0
}

function handleTouchMove(e) {
  if (!isDragging.value || !e.touches || e.touches.length === 0) return
  dragCurrentX = e.touches[0].clientX
  const diff = dragCurrentX - dragStartX
  // Elastic edge resistance
  if (
    (currentPhotoIndex.value === 0 && diff > 0) ||
    (currentPhotoIndex.value === galleryPhotos.length - 1 && diff < 0)
  ) {
    dragOffset.value = diff * 0.35
  } else {
    dragOffset.value = diff
  }
}

function handleTouchEnd() {
  if (!isDragging.value) return
  isDragging.value = false
  const diff = dragCurrentX - dragStartX
  const threshold = 38
  if (diff < -threshold) {
    nextPhoto()
  } else if (diff > threshold) {
    prevPhoto()
  }
  dragOffset.value = 0
}

function handleMouseDown(e) {
  isDragging.value = true
  dragStartX = e.clientX
  dragCurrentX = dragStartX
  dragOffset.value = 0
}

function handleMouseMove(e) {
  if (!isDragging.value) return
  dragCurrentX = e.clientX
  const diff = dragCurrentX - dragStartX
  if (
    (currentPhotoIndex.value === 0 && diff > 0) ||
    (currentPhotoIndex.value === galleryPhotos.length - 1 && diff < 0)
  ) {
    dragOffset.value = diff * 0.35
  } else {
    dragOffset.value = diff
  }
}

function handleMouseUp() {
  if (!isDragging.value) return
  isDragging.value = false
  const diff = dragCurrentX - dragStartX
  const threshold = 38
  if (diff < -threshold) {
    nextPhoto()
  } else if (diff > threshold) {
    prevPhoto()
  }
  dragOffset.value = 0
}

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

function prevPhoto() {
  slideDirection.value = 'prev'
  currentPhotoIndex.value = (currentPhotoIndex.value - 1 + galleryPhotos.length) % galleryPhotos.length
}

function nextPhoto() {
  slideDirection.value = 'next'
  currentPhotoIndex.value = (currentPhotoIndex.value + 1) % galleryPhotos.length
}

function selectPhoto(index) {
  if (index === currentPhotoIndex.value) return
  slideDirection.value = index > currentPhotoIndex.value ? 'next' : 'prev'
  currentPhotoIndex.value = index
}

function openLightbox(index) {
  activeLightboxList.value = galleryPhotos
  if (typeof index === 'number') {
    currentPhotoIndex.value = index
    lightboxIndex.value = index
  }
  isLightboxOpen.value = true
}

function openAlbumLightbox(index) {
  activeLightboxList.value = albumGridPhotos
  if (typeof index === 'number') {
    lightboxIndex.value = index
  }
  isLightboxOpen.value = true
}

function prevLightboxPhoto() {
  lightboxIndex.value = (lightboxIndex.value - 1 + activeLightboxList.value.length) % activeLightboxList.value.length
}

function nextLightboxPhoto() {
  lightboxIndex.value = (lightboxIndex.value + 1) % activeLightboxList.value.length
}

function closeLightbox() {
  isLightboxOpen.value = false
}

const router = useRouter()
const scrollContainer = ref(null)

// ── Entrance & Scroll Section Observation State ──
const entered = ref(true)
const isInviteInView = ref(true)
const isCountdownInView = ref(false)
const isAgendaInView = ref(false)
const isLocationInView = ref(false)
const isGalleryInView = ref(false)
const isAlbumInView = ref(false)

function onImgLoad() {
  entered.value = true
}

function updateActiveSections() {
  if (!scrollContainer.value) return
  const top = scrollContainer.value.scrollTop
  const h = scrollContainer.value.clientHeight || window.innerHeight

  // Symmetrical midpoint boundaries for 6 pages:
  // Page 0 (Invite): [0, 0.5h)
  // Page 1 (Countdown): [0.5h, 1.5h)
  // Page 2 (Agenda): [1.5h, 2.5h)
  // Page 3 (Location): [2.5h, 3.5h)
  // Page 4 (Gallery Slider): [3.5h, 4.5h)
  // Page 5 (Album Grid): [4.5h, end]
  const inInvite = top < h * 0.5
  const inCountdown = top >= h * 0.5 && top < h * 1.5
  const inAgenda = top >= h * 1.5 && top < h * 2.5
  const inLocation = top >= h * 2.5 && top < h * 3.5
  const inGallery = top >= h * 3.5 && top < h * 4.5
  const inAlbum = top >= h * 4.5

  if (isInviteInView.value !== inInvite) isInviteInView.value = inInvite
  if (isCountdownInView.value !== inCountdown) isCountdownInView.value = inCountdown
  if (isAgendaInView.value !== inAgenda) isAgendaInView.value = inAgenda
  if (isLocationInView.value !== inLocation) isLocationInView.value = inLocation
  if (isGalleryInView.value !== inGallery) isGalleryInView.value = inGallery
  if (isAlbumInView.value !== inAlbum) isAlbumInView.value = inAlbum
}

function onContainerScroll() {
  updateActiveSections()
}

// ── Live Countdown State & Logic ──
const now = ref(Date.now())
let countdownTimer = null
let sectionObserver = null

onMounted(() => {
  entered.value = true
  updateActiveSections()

  countdownTimer = setInterval(() => {
    now.value = Date.now()
  }, 1000)

  // IntersectionObserver for snap sections
  if (typeof window !== 'undefined' && 'IntersectionObserver' in window) {
    sectionObserver = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting && entry.intersectionRatio >= 0.45) {
            if (entry.target.id === 'page-invite') {
              isInviteInView.value = true
              isCountdownInView.value = false
              isAgendaInView.value = false
              isLocationInView.value = false
              isGalleryInView.value = false
            } else if (entry.target.id === 'page-countdown') {
              isInviteInView.value = false
              isCountdownInView.value = true
              isAgendaInView.value = false
              isLocationInView.value = false
              isGalleryInView.value = false
            } else if (entry.target.id === 'page-agenda') {
              isInviteInView.value = false
              isCountdownInView.value = false
              isAgendaInView.value = true
              isLocationInView.value = false
              isGalleryInView.value = false
            } else if (entry.target.id === 'page-location') {
              isInviteInView.value = false
              isCountdownInView.value = false
              isAgendaInView.value = false
              isLocationInView.value = true
              isGalleryInView.value = false
            } else if (entry.target.id === 'page-gallery') {
              isInviteInView.value = false
              isCountdownInView.value = false
              isAgendaInView.value = false
              isLocationInView.value = false
              isGalleryInView.value = true
              isAlbumInView.value = false
            } else if (entry.target.id === 'page-album') {
              isInviteInView.value = false
              isCountdownInView.value = false
              isAgendaInView.value = false
              isLocationInView.value = false
              isGalleryInView.value = false
              isAlbumInView.value = true
            }
          }
        })
      },
      {
        root: scrollContainer.value,
        threshold: 0.45,
      }
    )

    const inviteEl = document.getElementById('page-invite')
    const countdownEl = document.getElementById('page-countdown')
    const agendaEl = document.getElementById('page-agenda')
    const locationEl = document.getElementById('page-location')
    const galleryEl = document.getElementById('page-gallery')
    const albumEl = document.getElementById('page-album')
    if (inviteEl) sectionObserver.observe(inviteEl)
    if (countdownEl) sectionObserver.observe(countdownEl)
    if (agendaEl) sectionObserver.observe(agendaEl)
    if (locationEl) sectionObserver.observe(locationEl)
    if (galleryEl) sectionObserver.observe(galleryEl)
    if (albumEl) sectionObserver.observe(albumEl)
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

const khmerDigits = ['០', '១', '២', '៣', '៤', '៥', '៦', '៧', '៨', '៩']
function toKhmerNum(num, pad = 2) {
  return String(num)
    .padStart(pad, '0')
    .split('')
    .map(ch => (ch >= '0' && ch <= '9' ? khmerDigits[Number(ch)] : ch))
    .join('')
}

const countdown = computed(() => {
  const target = new Date(invitation.targetDate || '2027-03-13T08:00:00').getTime()
  const diff = target - now.value
  if (diff <= 0) {
    return {
      days: toKhmerNum(0),
      hours: toKhmerNum(0),
      mins: toKhmerNum(0),
      secs: toKhmerNum(0),
    }
  }
  const days = Math.floor(diff / (1000 * 60 * 60 * 24))
  const hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60))
  const mins = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60))
  const secs = Math.floor((diff % (1000 * 60)) / 1000)

  return {
    days: toKhmerNum(days),
    hours: toKhmerNum(hours),
    mins: toKhmerNum(mins),
    secs: toKhmerNum(secs),
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
  } else if (top < h * 2.5) {
    scrollToPage('page-location')
  } else if (top < h * 3.5) {
    scrollToPage('page-gallery')
  } else if (top < h * 4.5) {
    scrollToPage('page-album')
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
    const isAtAgenda = scrollContainer.value.scrollTop >= (agendaEl.offsetTop - 120) && scrollContainer.value.scrollTop < (agendaEl.offsetTop + 120)
    if (isAtAgenda) {
      scrollToPage('page-invite')
      return
    }
  }
  scrollToPage('page-agenda')
}

function onLocationClick() {
  const locationEl = document.getElementById('page-location')
  if (locationEl && scrollContainer.value) {
    const isAtLocation = scrollContainer.value.scrollTop >= (locationEl.offsetTop - 120) && scrollContainer.value.scrollTop < (locationEl.offsetTop + 120)
    if (isAtLocation) {
      scrollToPage('page-invite')
      return
    }
  }
  scrollToPage('page-location')
}

function openGoogleMaps() {
  const url = invitation.venueMapsUrl || 'https://maps.app.goo.gl/TZE8CuT46X9Ze9r28'
  window.open(url, '_blank')
}

function onGalleryClick() {
  const galleryEl = document.getElementById('page-gallery')
  const albumEl = document.getElementById('page-album')
  if (scrollContainer.value) {
    const top = scrollContainer.value.scrollTop
    const h = scrollContainer.value.clientHeight || window.innerHeight
    if (top >= h * 3.5 && top < h * 4.5) {
      scrollToPage('page-album')
      return
    } else if (top >= h * 4.5) {
      scrollToPage('page-invite')
      return
    }
  }
  scrollToPage('page-gallery')
}

function onWishesClick() {
  scrollToPage('page-album')
}
</script>

<style scoped src="./HomePreviewPage.css"></style>
