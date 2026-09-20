/**
 * invitation.js
 * ─────────────────────────────────────────────────────────────
 * ALL editable content for the digital wedding invitation.
 * Change only this file to customise names, dates, text & venue.
 * ─────────────────────────────────────────────────────────────
 */

const invitation = {

  /* ── Couple ──────────────────────────────────────────────── */
  groomName: 'ហ៊ឹម សំណាង',
  brideName: 'ឃន សារ៉េន',

  /** Two initials shown inside the golden monogram crest */
  initials: ['ព', 'ស'],

  /* ── Parents ─────────────────────────────────────────────── */
  groomFather: { role: 'លោក',    name: 'ហ៊ឹម លាង' },
  groomMother: { role: 'លោកស្រី', name: 'អ៊ុំ ស្រ៊ឺ' },
  brideFather: { role: 'លោក',    name: 'អ៊ុង សារ៉េត' },
  brideMother: { role: 'លោកស្រី', name: 'ធា ម៉ុំ' },

  /* ── Couple Roles ────────────────────────────────────────── */
  groomRole: 'កូនប្រុសនាម',
  brideRole: 'កូនស្រីនាម',

  /* ── Page Heading ────────────────────────────────────────── */
  pageTitle: 'សិរីមង្គលអាពាហ៍ពិពាហ៍',

  /* ── Honor Invite Subtitle ───────────────────────────────── */
  honorInviteText: 'មានកិត្តិយសសូមគោរពអញ្ជើញ',

  /* ── Formal Invitation Body ──────────────────────────────── */
  invitationLines: [
    'សម្តេច ទ្រង់ ឯកឧត្តម អ្នកឧកញ៉ា ឧកញ៉ា លោកជំទាវ លោក លោកស្រី អ្នកនាងកញ្ញា អញ្ជើញចូលរួមជាអធិបតី និងជាភ្ញៀវកិត្តិយស ដើម្បីប្រសិទ្ធពរជ័យ សិរីសួស្តី ជ័យមង្គល ក្នុងពិធីរៀបអាពាហ៍ពិពាហ៍ កូនប្រុស-កូនស្រី របស់យើងខ្ញុំ',
  ],

  /* ── Wedding Date ────────────────────────────────────────── */
  /**
   * ISO date-time string used by the countdown timer.
   * Format: 'YYYY-MM-DDTHH:mm:ss'
   */
  targetDate: '2026-11-24T08:00:00',

  /** Khmer lunar calendar date line */
  lunarDate: 'នៅថ្ងៃសៅរ៍ ៦កើត ខែផល្គុន ឆ្នាំមមី អដ្ឋស័ក ពុទ្ធសករាជ ២៥៧០',

  /** Solar (Gregorian) date shown prominently */
  solarDate: 'ត្រូវនឹងថ្ងៃទី ១៣ ខែមីនា ឆ្នាំ ២០២៧',

  /** Time of the reception */
  receptionTime: 'វេលាម៉ោង ០៥ : ០០ ល្ងាចនៅ',

  /** Human-readable date shown on the invitation card */
  dateDisplay: 'ថ្ងៃអាទិត្យ ទី២៤ ខែវិច្ឆិកា ឆ្នាំ២០២៦',

  /* ── Venue ───────────────────────────────────────────────── */
  venue: 'សាល ដឹ ហ្គ្រេន ហល · រាជធានីភ្នំពេញ',
  venueName: 'គេហដ្ឋាននៃសិរីមង្គលអាពាហ៍ពិពាហ៍',
  venueAddress: 'ស្ថិតនៅ ភូមិអូរល្វា ឃុំជ្រៃសីម៉ា ស្រុកសំពៅលូន ខេត្តបាត់ដំបង',
  venueClosingWish: 'ដោយមេត្រីភាព។',

  scrollUpText: 'អូសឡើងទៅលើ',

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
