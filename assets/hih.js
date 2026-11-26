/* Home Improvement Hub: interaction layer. No dependencies. Every feature degrades to plain HTML. */
(() => {
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* Images fade in once decoded */
  const markLoaded = (img) => img.classList.add('is-loaded');
  document.querySelectorAll('img.hih-fade').forEach((img) => {
    if (img.complete) markLoaded(img);
    else {
      img.addEventListener('load', () => markLoaded(img), { once: true });
      img.addEventListener('error', () => markLoaded(img), { once: true });
    }
  });

  /* Header hairline once the page scrolls */
  const header = document.querySelector('.hih-header');
  if (header) {
    const sentinel = document.createElement('div');
    sentinel.setAttribute('aria-hidden', 'true');
    document.body.prepend(sentinel);
    new IntersectionObserver(([entry]) => header.classList.toggle('is-scrolled', !entry.isIntersecting)).observe(sentinel);
  }

  /* Spotlight: a soft glow follows the pointer across the card under it (mouse and trackpad only). */
  if (window.matchMedia('(hover: hover) and (pointer: fine)').matches && !reduceMotion) {
    document.querySelectorAll('[data-hih-spot]').forEach((grid) => {
      let frame = 0;
      grid.addEventListener('pointermove', (e) => {
        const media = e.target.closest('.hih-tile, .hih-card')?.querySelector('.hih-media');
        if (!media || frame) return;
        frame = requestAnimationFrame(() => {
          frame = 0;
          const r = media.getBoundingClientRect();
          media.style.setProperty('--hih-spot-x', `${((e.clientX - r.left) / r.width) * 100}%`);
          media.style.setProperty('--hih-spot-y', `${((e.clientY - r.top) / r.height) * 100}%`);
        });
      });
    });
  }

  /* Progress on guide cards: "Step 3 of 7" from the steps marked done on the guide page.
     In-progress guides move to the front of their grid (DOM order, so keyboard order matches). */
  const readJSON = (key, fallback) => {
    try { return JSON.parse(localStorage.getItem(key) || 'null') ?? fallback; } catch (e) { return fallback; }
  };
  /* "Pick up where you left off": the last guides opened in this browser (saved by the guide page). */
  const continueSection = document.querySelector('[data-hih-continue]');
  if (continueSection) {
    const recent = readJSON('hih:recent', []);
    const grid = continueSection.querySelector('[data-hih-continue-grid]');
    if (Array.isArray(recent) && recent.length && grid) {
      recent.slice(0, 3).forEach((g) => {
        const card = document.createElement('a');
        card.className = 'hih-card';
        card.href = g.u;
        card.setAttribute('data-guide-card', g.id);
        const media = document.createElement('span');
        media.className = 'hih-media';
        if (g.img) {
          const img = document.createElement('img');
          img.src = g.img; img.alt = ''; img.loading = 'lazy';
          media.append(img);
        }
        const label = document.createElement('span');
        label.className = 'hih-card__blog';
        label.textContent = g.b || '';
        const title = document.createElement('h3');
        title.className = 'hih-card__title';
        const titleText = document.createElement('span');
        titleText.className = 'hih-underline';
        titleText.textContent = g.t || '';
        title.append(titleText);
        card.append(media, label, title);
        grid.append(card);
      });
      continueSection.hidden = false;
    }
  }

  document.querySelectorAll('[data-guide-card]').forEach((card) => {
    const id = card.getAttribute('data-guide-card');
    const total = Number(readJSON(`hih:total:${id}`, 0));
    const doneSteps = readJSON(`hih:done:${id}`, []);
    if (!total || !Array.isArray(doneSteps) || !doneSteps.length) return;
    const count = Math.min(doneSteps.length, total);
    let next = 1;
    while (doneSteps.includes(next) && next <= total) next += 1;
    const finished = count >= total;
    const media = card.querySelector('.hih-media');
    if (!media) return;
    const badge = document.createElement('span');
    badge.className = `hih-progress-badge${finished ? ' is-finished' : ''}`;
    badge.textContent = finished ? 'Finished' : `Step ${next} of ${total}`;
    const bar = document.createElement('span');
    bar.className = 'hih-progress-bar';
    bar.setAttribute('aria-hidden', 'true');
    bar.style.setProperty('--hih-done', String(count / total));
    media.append(badge, bar);
    if (!finished) {
      card.classList.add('is-in-progress');
      const grid = card.closest('.hih-cards');
      if (grid) {
        const lastInProgress = Array.from(grid.querySelectorAll(':scope > .is-in-progress')).filter((c) => c !== card).pop();
        if (lastInProgress) lastInProgress.after(card); else grid.prepend(card);
      }
    }
  });

  /* Tools We Recommend: a filter box over the product cards. It only filters this page; it never leaves it. */
  const picks = [...document.querySelectorAll('.hih-rte .hih-picks')];
  if (picks.length) {
    const firstHeading = picks[0].parentElement.querySelector('h2');
    const form = document.createElement('form');
    form.className = 'hih-search hih-picks-search';
    form.setAttribute('role', 'search');
    form.innerHTML =
      '<input class="hih-input" type="search" name="q" autocomplete="off" aria-label="Search tools" placeholder="Search tools, e.g. drain, paint, stud">' +
      '<p class="hih-picks-status" aria-live="polite"></p>';
    firstHeading.before(form);
    const input = form.querySelector('[name="q"]');
    const status = form.querySelector('.hih-picks-status');
    const sections = picks.map((list) => ({
      list,
      heading: list.previousElementSibling?.previousElementSibling,
      intro: list.previousElementSibling,
      items: [...list.children].map((li) => ({ li, text: li.textContent.toLowerCase() })),
    }));
    let shown = 0;
    input.addEventListener('input', () => {
      const words = input.value.toLowerCase().trim().split(/\s+/).filter(Boolean);
      shown = 0;
      sections.forEach((sec) => {
        let count = 0;
        sec.items.forEach(({ li, text }) => {
          const hit = words.every((w) => text.includes(w));
          li.hidden = !hit;
          if (hit) count += 1;
        });
        [sec.list, sec.heading, sec.intro].forEach((el) => { if (el) el.hidden = count === 0; });
        shown += count;
      });
      if (!words.length) status.textContent = '';
      else if (shown) status.textContent = `${shown} ${shown === 1 ? 'tool matches' : 'tools match'}.`;
      else status.textContent = `No tools match “${input.value.trim()}”. Try another word, like drain, paint or saw.`;
    });
    form.addEventListener('submit', (e) => e.preventDefault());
  }

  /* Book slide-in: our own planner for this category, shown at most once every 14 days, after the reader
     is 60% through the guide or has spent 45 s on it. Never while the phone step bar or the end-of-guide box is on screen. */
  const slide = document.querySelector('[data-bookslide]');
  if (slide) {
    const key = 'hih:book-slide';
    let seenAt = 0;
    try { seenAt = Number(localStorage.getItem(key) || 0); } catch (e) { /* storage off: show once per page */ }
    const quiet = Date.now() - seenAt < 14 * 24 * 3600 * 1000;
    const box = document.querySelector('.hih-book');
    let boxVisible = false;
    if (box && 'IntersectionObserver' in window) {
      new IntersectionObserver((es) => { boxVisible = es[0].isIntersecting; if (boxVisible) slide.hidden = true; }).observe(box);
    }
    let shown = false;
    let timeUp = false;
    const article = document.querySelector('.hih-rte') || document.body;
    const show = () => {
      if (shown || quiet || boxVisible) return;
      if (document.querySelector('.hih-stepbar:not([hidden])') && window.matchMedia('(max-width: 61.99em)').matches) return;
      const r = article.getBoundingClientRect();
      const read = (window.innerHeight - r.top) / Math.max(r.height, 1);
      if (read < 0.6 && !timeUp) return;
      shown = true;
      slide.hidden = false;
      try { localStorage.setItem(key, String(Date.now())); } catch (e) { /* ignore */ }
    };
    const onScroll = () => { show(); if (shown) window.removeEventListener('scroll', onScroll); };
    if (!quiet) {
      window.addEventListener('scroll', onScroll, { passive: true });
      setTimeout(() => { timeUp = true; show(); }, 45000);
    }
    slide.querySelector('[data-bookslide-close]').addEventListener('click', () => { slide.hidden = true; });
    document.addEventListener('keydown', (e) => { if (e.key === 'Escape' && !slide.hidden) slide.hidden = true; });
  }

  /* Guide page */
  const guide = document.querySelector('[data-guide-id]');
  if (!guide) return;
  const guideId = guide.getAttribute('data-guide-id');
  const steps = Array.from(guide.querySelectorAll('.guide-steps > li'));
  const toc = guide.querySelector('[data-toc]');
  const storeKey = `hih:done:${guideId}`;

  const readDone = () => {
    try { return new Set(JSON.parse(localStorage.getItem(storeKey) || '[]')); } catch (e) { return new Set(); }
  };
  const writeDone = (set) => {
    try { localStorage.setItem(storeKey, JSON.stringify(Array.from(set))); } catch (e) { /* storage unavailable: progress lasts this visit only */ }
  };
  const done = readDone();
  try { localStorage.setItem(`hih:total:${guideId}`, String(steps.length)); } catch (e) { /* ignore */ }
  try {
    const entry = { id: guideId, u: guide.getAttribute('data-guide-url'), t: guide.getAttribute('data-guide-title'), b: guide.getAttribute('data-guide-blog'), img: guide.getAttribute('data-guide-image') || '' };
    const list = readJSON('hih:recent', []).filter((g) => g && g.id !== guideId);
    localStorage.setItem('hih:recent', JSON.stringify([entry, ...list].slice(0, 6)));
  } catch (e) { /* ignore */ }

  /* When every step is done: say so and point to the next guide. */
  const upnext = guide.querySelector('[data-upnext]');
  const syncComplete = () => {
    const complete = steps.length > 0 && steps.every((_, i) => done.has(i + 1));
    if (!upnext) return;
    upnext.classList.toggle('is-complete', complete);
    const msg = upnext.querySelector('[data-upnext-done]');
    if (msg) msg.hidden = !complete;
  };
  const tocLinks = [];

  steps.forEach((li, i) => {
    const n = i + 1;
    li.id = li.id || `step-${n}`;
    const h3 = li.querySelector('h3');
    const label = h3 ? h3.textContent.trim() : `Step ${n}`;

    if (toc) {
      const a = document.createElement('a');
      a.href = `#${li.id}`;
      a.textContent = label;
      const item = document.createElement('li');
      item.append(a);
      toc.append(item);
      tocLinks.push(a);
    }

    const btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'hih-step-done';
    btn.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg><span></span>';
    const text = btn.querySelector('span');
    const render = () => {
      const isDone = done.has(n);
      btn.setAttribute('aria-pressed', String(isDone));
      text.textContent = isDone ? 'Done' : 'Mark step done';
      li.classList.toggle('is-done', isDone);
      if (tocLinks[i]) tocLinks[i].classList.toggle('is-done', isDone);
    };
    btn.addEventListener('click', () => {
      if (done.has(n)) done.delete(n); else done.add(n);
      writeDone(done);
      render();
      syncComplete();
      if (done.has(n) && steps[i + 1]) {
        steps[i + 1].scrollIntoView({ behavior: reduceMotion ? 'auto' : 'smooth', block: 'start' });
      } else if (done.has(n) && upnext && upnext.classList.contains('is-complete')) {
        upnext.scrollIntoView({ behavior: reduceMotion ? 'auto' : 'smooth', block: 'center' });
      }
    });
    li.append(btn);
    render();
  });

  syncComplete();

  if (toc && !steps.length) {
    const panel = toc.closest('.hih-toc-panel');
    if (panel) panel.hidden = true;
  }

  /* Active step: highlights the TOC (desktop) and drives the step bar (phones). */
  let stepbar = null;
  let active = -1;
  if (steps.length) {
    stepbar = document.createElement('div');
    stepbar.className = 'hih-stepbar';
    stepbar.hidden = true;
    stepbar.innerHTML = '<span class="hih-stepbar__text" aria-live="polite"></span><button type="button" class="hih-stepbar__next"></button>';
    document.body.append(stepbar);
    const barText = stepbar.querySelector('.hih-stepbar__text');
    const barNext = stepbar.querySelector('.hih-stepbar__next');
    const titles = steps.map((li, i) => (li.querySelector('h3') ? li.querySelector('h3').textContent.trim() : `Step ${i + 1}`));
    const setActive = (idx) => {
      active = idx;
      tocLinks.forEach((a, j) => {
        a.classList.toggle('is-active', j === idx);
        if (j === idx) a.setAttribute('aria-current', 'step'); else a.removeAttribute('aria-current');
      });
      if (idx < 0) { stepbar.hidden = true; return; }
      stepbar.hidden = false;
      barText.textContent = `Step ${idx + 1} of ${steps.length}: ${titles[idx]}`;
      barNext.textContent = idx < steps.length - 1 ? 'Next step' : 'Finish';
    };
    barNext.addEventListener('click', () => {
      const target = steps[active + 1] || upnext;
      if (target) target.scrollIntoView({ behavior: reduceMotion ? 'auto' : 'smooth', block: 'start' });
    });
    const io = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) setActive(steps.indexOf(entry.target));
      });
    }, { rootMargin: '-30% 0px -60% 0px' });
    steps.forEach((li) => io.observe(li));
    /* Hide the bar before the first step and once the reader is past the steps. */
    const list = guide.querySelector('.guide-steps');
    if (list) {
      new IntersectionObserver(([entry]) => {
        if (!entry.isIntersecting) setActive(-1);
      }).observe(list);
    }
  }

  /* Tools and materials checklist remembers ticks */
  const checks = Array.from(guide.querySelectorAll('.hih-checklist input[type="checkbox"]'));
  const checkKey = `hih:checks:${guideId}`;
  let saved = [];
  try { saved = JSON.parse(localStorage.getItem(checkKey) || '[]'); } catch (e) { saved = []; }
  checks.forEach((c, i) => {
    c.checked = saved.includes(i);
    c.addEventListener('change', () => {
      const on = checks.map((x, j) => (x.checked ? j : -1)).filter((j) => j >= 0);
      try { localStorage.setItem(checkKey, JSON.stringify(on)); } catch (e) { /* ignore */ }
    });
  });

  /* Video: load YouTube only when asked (privacy-enhanced domain) */
  guide.querySelectorAll('[data-youtube-id]').forEach((frame) => {
    const play = frame.querySelector('.hih-video__play');
    if (!play) return;
    play.addEventListener('click', () => {
      const iframe = document.createElement('iframe');
      iframe.src = `https://www.youtube-nocookie.com/embed/${encodeURIComponent(frame.getAttribute('data-youtube-id'))}?autoplay=1&rel=0`;
      iframe.title = frame.getAttribute('data-title') || 'Video';
      iframe.allow = 'accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture';
      iframe.allowFullscreen = true;
      frame.replaceChildren(iframe);
    });
  });
})();
