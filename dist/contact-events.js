/* Optional, consent-gated integration hook. No network requests, cookies or storage.
   A consent manager must explicitly set window.silentZoneAnalyticsConsent = true.
   An approved analytics adapter can listen for silentzone:contact-intent.
   Click intent is NOT a submitted enquiry or confirmed membership. */
(() => {
  'use strict';
  document.addEventListener('click', (event) => {
    if (window.silentZoneAnalyticsConsent !== true || navigator.globalPrivacyControl === true || navigator.doNotTrack === '1') return;
    const link = event.target instanceof Element ? event.target.closest('a[data-contact-action]') : null;
    if (!link) return;
    const action = link.dataset.contactAction;
    const plan = link.dataset.membershipPlan;
    if (!['whatsapp', 'phone', 'directions'].includes(action)) return;
    if (!['none', 'single', 'double', 'triple', 'full'].includes(plan)) return;
    document.dispatchEvent(new CustomEvent('silentzone:contact-intent', {
      detail: { action, plan }
    }));
  });
})();
