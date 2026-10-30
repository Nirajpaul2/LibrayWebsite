import vm from 'node:vm';
import fs from 'node:fs';
import assert from 'node:assert/strict';
const source = fs.readFileSync(new URL('../dist/contact-events.js', import.meta.url), 'utf8');
function run({ consent, dnt, gpc, action = 'whatsapp', plan = 'single', match = true }) {
  let click; const events = [];
  class Element { closest() { return match ? { dataset: { contactAction: action, membershipPlan: plan } } : null; } }
  const context = { window: { silentZoneAnalyticsConsent: consent }, navigator: { doNotTrack: dnt, globalPrivacyControl: gpc }, Element,
    CustomEvent: class { constructor(type, options) { this.type = type; this.detail = options.detail; } },
    document: { addEventListener(name, fn) { assert.equal(name, 'click'); click = fn; }, dispatchEvent(e) { events.push(e); } } };
  vm.runInNewContext(source, context);
  click({ target: new Element() });
  return JSON.parse(JSON.stringify(events));
}
assert.deepEqual(run({}), []);
assert.deepEqual(run({consent:false}), []);
assert.deepEqual(run({consent:true, dnt:'1'}), []);
assert.deepEqual(run({consent:true, gpc:true}), []);
assert.deepEqual(run({consent:true, action:'invalid'}), []);
assert.deepEqual(run({consent:true, plan:'personal-data'}), []);
assert.deepEqual(run({consent:true, match:false}), []);
assert.deepEqual(run({consent:true}), [{type:'silentzone:contact-intent',detail:{action:'whatsapp',plan:'single'}}]);
for (const action of ['phone','directions']) assert.equal(run({consent:true,action,plan:'none'})[0].detail.action,action);
console.log('PASS: contact-intent consent, privacy signals, payload allowlist and action behavior.');
