/**
 * invitation.js
 * ─────────────────────────────────────────────────────────────
 * ALL editable content for the digital wedding invitation.
 * Change only this file to customise names, dates, text & venue.
 * ─────────────────────────────────────────────────────────────
 */

const invitation = {

  /* ── Couple ──────────────────────────────────────────────── */
  groomName: 'ពិសិដ្ឋ',
  brideName: 'ស្រីពៅ',

  /** Two initials shown inside the golden monogram crest */
  initials: ['ព', 'ស'],

  /* ── Wedding Date ────────────────────────────────────────── */
  /**
   * ISO date-time string used by the countdown timer.
   * Format: 'YYYY-MM-DDTHH:mm:ss'
   */
  targetDate: '2026-11-24T08:00:00',

  /** Human-readable date shown on the invitation card */
  dateDisplay: 'ថ្ងៃអាទិត្យ ទី២៤ ខែវិច្ឆិកា ឆ្នាំ២០២៦',

  /* ── Venue ───────────────────────────────────────────────── */
  venue: 'សាល ដឹ ហ្គ្រេន ហល · រាជធានីភ្នំពេញ',

  /* ── Khmer Text ──────────────────────────────────────────── */
  /** Main heading in Khmer (above logo) */
  khmerGreeting: 'សិរីមង្គលអាពាហ៍ពិពាហ៍',

  /** Subtitle lines in Khmer (below logo) */
  khmerSubtitle: [
    'សូមគោរពអញ្ជើញចូលរួម',
  ],

  /** "Save The Date" label above the date (in Khmer) */
  saveTheDateLabel: 'កាលបរិច្ឆេទថ្ងៃមង្គល',

  /* ── Honored Guest & Open Invitation ─────────────────────── */
  guestHonorLabel: 'ភ្ញៀវកិត្តិយស',
  btnOpenInvitation: 'សូមចុចបើកសំបុត្រ',
  openInvitationAlert: 'សូមស្វាគមន៍មកកាន់ពិធីមង្គលការរបស់យើងខ្ញុំ! 💍✨',


  /* ── Studio Branding ─────────────────────────────────────── */
  watermark: 'សំបុត្រអញ្ជើញឌីជីថល ដោយ SAMBOT ONLINE',

  /* ── Countdown Unit Labels ───────────────────────────────── */
  countdownLabels: {
    days: 'ថ្ងៃ',
    hours: 'ម៉ោង',
    mins: 'នាទី',
    secs: 'វិនាទី',
  },

  /* ── UI Strings & Alerts ─────────────────────────────────── */
  scrollHintText: 'អូសចុះក្រោម',
  rsvpAlertMessage: 'ទំព័រឆ្លើយតប (RSVP) នឹងមកដល់ឆាប់ៗនេះ! 💌',
  calendarDetails: 'សូមគោរពអញ្ជើញចូលរួមអបអរសាទរក្នុងថ្ងៃមង្គលការដ៏វិសេសវិសាលរបស់យើងខ្ញុំ!',

  /* ── RSVP Button ─────────────────────────────────────────── */
  /** Text labels for the action buttons */
  btnRsvpLabel:     '💌 ឆ្លើយតបការចូលរួម',
  btnCalendarLabel: '📅 កត់ត្រាប្រតិទិន',

  /**
   * Google Calendar event duration in hours (from targetDate).
   * Default: 6 hours.
   */
  eventDurationHours: 6,
}

export default invitation
