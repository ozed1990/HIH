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
      if (done.has(n) && steps[i + 1]) {
        steps[i + 1].scrollIntoView({ behavior: reduceMotion ? 'auto' : 'smooth', block: 'start' });
      }
    });
    li.append(btn);
    render();
  });

  if (toc && !steps.length) {
    const panel = toc.closest('.hih-toc-panel');
    if (panel) panel.hidden = true;
  }

  /* Active step in the table of contents */
  if (tocLinks.length) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        const idx = steps.indexOf(entry.target);
        tocLinks.forEach((a, j) => {
          a.classList.toggle('is-active', j === idx);
          if (j === idx) a.setAttribute('aria-current', 'step'); else a.removeAttribute('aria-current');
        });
      });
    }, { rootMargin: '-30% 0px -60% 0px' });
    steps.forEach((li) => io.observe(li));
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
