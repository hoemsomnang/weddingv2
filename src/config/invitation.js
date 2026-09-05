/**
 * invitation.js
 * ─────────────────────────────────────────────────────────────
 * ALL editable content for the digital wedding invitation.
 * Change only this file to customise names, dates, text & venue.
 * ─────────────────────────────────────────────────────────────
 */

const invitation = {

  /* ── Couple ──────────────────────────────────────────────── */
  groomName: 'Piseth',
  brideName: 'Sreypov',

  /** Two initials shown inside the golden monogram crest */
  initials: ['P', 'S'],

  /* ── Wedding Date ────────────────────────────────────────── */
  /**
   * ISO date-time string used by the countdown timer.
   * Format: 'YYYY-MM-DDTHH:mm:ss'
   */
  targetDate: '2026-11-24T08:00:00',

  /** Human-readable date shown on the invitation card */
  dateDisplay: 'Sunday, November 24, 2026',

  /* ── Venue ───────────────────────────────────────────────── */
  venue: 'The Grand Hall · Phnom Penh, Cambodia',

  /* ── Khmer Text ──────────────────────────────────────────── */
  /** Main heading in Khmer (top of card) */
  khmerGreeting: 'សិរីមង្គលអាពាហ៍ពិពាហ៍',

  /** Subtitle lines in Khmer (shown below couple names) */
  khmerSubtitle: [
    'សូមគោរពអញ្ជើញចូលរួម',
    'អភិពិធីខួប​ស្នេហ៍',
  ],

  /** "Save The Date" label above the date (change language here if needed) */
  saveTheDateLabel: 'Save The Date',

  /* ── Visual Assets ───────────────────────────────────────── */
  /** Bottom floral background (Left & Right SVGs follow wedding_meadow_transparent) */
  bottomFloralLeft: '/wedding_bottom_left.svg',
  bottomFloralRight: '/wedding_bottom_right.svg',
  bottomFloralImage: '/background.png',

  /* ── Studio Branding ─────────────────────────────────────── */
  watermark: 'E-Invitation by SAMBOT ONLINE',

  /* ── Countdown Unit Labels ───────────────────────────────── */
  countdownLabels: {
    days: 'Days',
    hours: 'Hours',
    mins: 'Mins',
    secs: 'Secs',
  },

  /* ── UI Strings & Alerts ─────────────────────────────────── */
  scrollHintText: 'Scroll',
  rsvpAlertMessage: 'RSVP page coming soon! 💌',
  calendarDetails: 'You are cordially invited to celebrate our special day!',

  /* ── RSVP Button ─────────────────────────────────────────── */
  /** Text labels for the action buttons */
  btnRsvpLabel:     '💌 RSVP Now',
  btnCalendarLabel: '📅 Add to Calendar',

  /**
   * Google Calendar event duration in hours (from targetDate).
   * Default: 6 hours.
   */
  eventDurationHours: 6,
}

export default invitation
