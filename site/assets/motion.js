'use strict';
// Single cursor per mark; static complete SVGs remain the no-script fallback.
(() => {
  const button = document.querySelector('.motion-control');
  const media = window.matchMedia('(prefers-reduced-motion: reduce)');
  const marks = [...document.querySelectorAll('svg.typing')].map(svg => {
    const glyphs = [...svg.querySelectorAll('.glyph')];
    const times = svg.dataset.keyTimes.split(',').map(Number);
    const offsets = svg.dataset.cursorOffsets.split(',').map(Number);
    const delay = Number(svg.dataset.startDelay);
    const cursor = svg.querySelector('.brand-cursor');
    if (!cursor || glyphs.length !== times.length + 1 ||
        offsets.length !== glyphs.length || ![...times,...offsets,delay].every(Number.isFinite)) {
      throw new Error('Invalid brand timing configuration');
    }
    return {glyphs, times, offsets, delay, cursor, credit:svg.querySelector('.brand-credit')};
  });
  if (!marks.length || !button) return;
  let paused = media.matches;
  let start = performance.now(), timer = 0;
  const hide = (node, hidden) => {if(node)node.toggleAttribute('data-hidden',hidden);};
  const staticMark = mark => {
    mark.glyphs.forEach(glyph => hide(glyph,false));
    hide(mark.credit,false); hide(mark.cursor,false);
    mark.cursor.removeAttribute('transform');
  };
  const render = (mark, elapsed) => {
    const t = Math.max(0,elapsed-mark.delay);
    const end = mark.times.at(-1);
    const typed = mark.times.filter(time => t >= time).length;
    const done = typed === mark.times.length;
    mark.glyphs.forEach((glyph,i) => hide(glyph,i>typed));
    hide(mark.credit,!done);
    const visible = done ? (t-end)%1000 < 500 : !(t>=500 && t<1000);
    hide(mark.cursor,!visible);
    mark.cursor.setAttribute('transform','translate('+mark.offsets[typed]+' 0)');
    if(elapsed<mark.delay)return mark.delay-elapsed;
    if(done)return 500-((t-end)%500);
    const next = [500,1000,...mark.times].find(time=>time>t);
    return next-t;
  };
  const tick = () => {
    clearTimeout(timer);
    if(paused){marks.forEach(staticMark);return;}
    const elapsed = performance.now()-start;
    const next = Math.min(...marks.map(mark=>render(mark,elapsed)));
    timer = setTimeout(tick,Math.max(1,Math.ceil(next)));
  };
  const update = () => {
    clearTimeout(timer);
    button.setAttribute('aria-pressed',String(paused));
    button.textContent = paused ? 'Animation starten' : 'Animation stoppen';
    if(paused)marks.forEach(staticMark);
    else {start=performance.now();tick();}
  };
  button.addEventListener('click',()=>{paused=!paused;update();});
  media.addEventListener('change',event=>{paused=event.matches;update();});
  document.addEventListener('visibilitychange',()=>{if(!document.hidden)tick();});
  window.addEventListener('pageshow',event=>{if(event.persisted)tick();});
  button.hidden=false;
  update();
})();
