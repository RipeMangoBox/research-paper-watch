/* The generated reader works offline; no fetch, telemetry, dependencies, or storage. */
(function (global) {
  'use strict';
  function isEditable(target) {
    return !!(target && (target.isContentEditable ||
      (target.closest && target.closest('input, textarea, select, [contenteditable]:not([contenteditable="false"]), [role="textbox"], [role="combobox"]'))));
  }
  function shortcutAction(event, enabled) {
    if (!enabled || event.defaultPrevented || event.isComposing || event.repeat ||
        event.ctrlKey || event.metaKey || event.altKey || event.shiftKey || isEditable(event.target)) return null;
    const key = String(event.key || '').toLowerCase();
    return key === 'e' ? 'expand' : key === 'c' ? 'collapse' : null;
  }
  function matches(searchText, category, query, selected) {
    const words = query.trim().toLocaleLowerCase().split(/\s+/).filter(Boolean);
    return (!selected || selected === category) && words.every(word => searchText.toLocaleLowerCase().includes(word));
  }
  function setAll(cards, open) {
    cards.forEach(card => { card.querySelector('details').open = open; });
  }
  function init(doc) {
    const cards = Array.from(doc.querySelectorAll('.paper'));
    const search = doc.getElementById('search');
    const category = doc.getElementById('category');
    const priority = doc.getElementById('priority');
    const count = doc.getElementById('result-count');
    const filter = () => {
      let visible = 0;
      cards.forEach(card => {
        card.hidden = !matches(card.dataset.search, card.dataset.category, search.value, category.value) || !!(priority && priority.value && priority.value !== card.dataset.priority);
        if (!card.hidden) visible++;
      });
      count.textContent = `${visible} / ${cards.length} 篇论文`;
      doc.getElementById('empty').hidden = visible !== 0;
    };
    search.addEventListener('input', filter);
    category.addEventListener('change', filter);
    if (priority) priority.addEventListener('change', filter);
    doc.getElementById('expand').addEventListener('click', () => setAll(cards, true));
    doc.getElementById('collapse').addEventListener('click', () => setAll(cards, false));
    doc.addEventListener('keydown', event => {
      const action = shortcutAction(event, doc.getElementById('shortcuts').checked);
      if (action) { event.preventDefault(); setAll(cards, action === 'expand'); }
    });
    filter();
    return {filter, cards};
  }
  const api = {isEditable, shortcutAction, matches, setAll, init};
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
  if (global.document) init(global.document);
})(typeof window !== 'undefined' ? window : globalThis);
