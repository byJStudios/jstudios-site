'use strict';
// Scroll reveal is independent of terminal typing. All idle cursors share
// the same wall-clock phase, including the startup marks after completion.
(() => {
  const button=document.querySelector('.motion-control');
  if(!button)return;
  const media=window.matchMedia('(prefers-reduced-motion: reduce)');
  const groups=new Map();
  const hide=(node,hidden)=>{if(node)node.toggleAttribute('data-hidden',hidden);};
  for(const svg of document.querySelectorAll('svg.typing')){
    const glyphs=[...svg.querySelectorAll('.glyph')];
    const times=svg.dataset.keyTimes.split(',').map(Number);
    const xs=svg.dataset.cursorOffsets.split(',').map(Number);
    const ys=svg.dataset.cursorY?.split(',').map(Number)??xs.map(()=>0);
    const cursor=svg.querySelector('.brand-cursor');
    if(!cursor||glyphs.length!==times.length+1||xs.length!==glyphs.length||ys.length!==xs.length||![...times,...xs,...ys].every(Number.isFinite))continue;
    const host=svg.closest('.portfolio-heading')??svg;
    if(!groups.has(host))groups.set(host,{host,marks:[],trigger:svg.dataset.trigger??'startup',delay:Number(svg.dataset.startDelay)||0,done:false});
    groups.get(host).marks.push({glyphs,times,xs,ys,cursor,credit:svg.querySelector('.brand-credit')});
  }
  const cards=[...document.querySelectorAll('.product,.portfolio-card,.principles article,.features article,.section-head,.app-preview')].map(el=>({el,shift:0,value:1,target:1}));
  let paused=media.matches,epoch=performance.now(),timer=0,frame=0,dirty=true,lastFrame=null;
  const idleOn=()=>Date.now()%1000<500;
  const revealCredit=(g,ready)=>{
    g.host.classList.toggle('credit-ready',ready);
    // CSS controls opacity; the old visibility toggle would cause a pop.
    hide(g.host.querySelector('.portfolio-credit'),false);
    for(const m of g.marks)hide(m.credit,false);
  };
  function complete(g,blink){
    for(const m of g.marks){
      m.glyphs.forEach(x=>hide(x,false));
      m.cursor.removeAttribute('transform');
      hide(m.cursor,blink&&!idleOn());
    }
    revealCredit(g,true);
    g.done=true;g.host.dataset.motionState='complete';
  }
  function pending(g){
    g.done=false;g.host.dataset.motionState='pending';
    revealCredit(g,false);
    for(const m of g.marks){
      m.glyphs.forEach((x,i)=>hide(x,i!==0));
      hide(m.cursor,true);
      m.cursor.setAttribute('transform','translate('+m.xs[0]+' '+m.ys[0]+')');
    }
  }
  function render(g,t){
    if(g.trigger==='scroll'||g.done){complete(g,true);return;}
    let done=true;
    for(const m of g.marks){
      const elapsed=Math.max(0,t);
      const typed=m.times.filter(v=>elapsed>=v).length;
      const finished=typed===m.times.length;
      done&&=finished;
      m.glyphs.forEach((x,i)=>hide(x,i>typed));
      hide(m.cursor,t<0||(!finished&&elapsed>=500&&elapsed<1000)||(finished&&!idleOn()));
      m.cursor.setAttribute('transform','translate('+m.xs[typed]+' '+m.ys[typed]+')');
    }
    revealCredit(g,done);g.done=done;g.host.dataset.motionState=done?'complete':'typing';
  }
  const clamp=x=>Math.max(0,Math.min(1,x));
  // Scroll only determines the target. Rendering converges independently
  // using elapsed time, not wheel events or a fixed per-frame increment.
  const TAU=48, EPSILON=.005;
  function measure(){
    const viewport=innerHeight;
    const values=cards.map(c=>{
      const r=c.el.getBoundingClientRect();
      const top=r.top-c.shift,bottom=r.bottom-c.shift;
      const overlap=Math.max(0,Math.min(bottom,viewport)-Math.max(top,0));
      const linear=clamp(overlap/Math.max(1,Math.min(r.height,viewport)/4));
      return c.el.contains(document.activeElement)?1:linear*linear*(3-2*linear);
    });
    cards.forEach((c,i)=>{c.target=values[i];});
    dirty=false;
  }
  function paint(c){
    const p=c.value;c.shift=16*(1-p);
    c.el.style.setProperty('--reveal',String(p));
    c.el.style.setProperty('--reveal-y',c.shift+'px');
    c.el.style.setProperty('--credit-reveal',String(clamp((p-.12)/.76)));
    c.el.dataset.reveal=p>=.999?'visible':p<=0?'outside':'entering';
  }
  function layout(now){
    frame=0;if(paused||document.hidden){lastFrame=null;return;}
    if(dirty)measure();
    const dt=lastFrame===null?0:Math.max(0,now-lastFrame);
    const alpha=-Math.expm1(-dt/TAU);
    let moving=false;
    for(const c of cards){
      const before=c.value;
      if(c.el.contains(document.activeElement)||Math.abs(c.target-c.value)<=EPSILON)c.value=c.target;
      else {
        c.value+= (c.target-c.value)*alpha;
        if(Math.abs(c.target-c.value)<=EPSILON)c.value=c.target;
      }
      if(before!==c.value)paint(c);
      moving||=c.value!==c.target;
    }
    lastFrame=moving?now:null;
    if(moving)frame=requestAnimationFrame(layout);
  }
  function schedule(){
    dirty=true;
    if(!frame&&!paused&&!document.hidden)frame=requestAnimationFrame(layout);
  }
  function tick(){
    clearTimeout(timer);if(paused||document.hidden)return;
    const now=performance.now();
    let typing=false;
    for(const g of groups.values()){
      render(g,now-epoch-g.delay);
      typing||=!g.done;
    }
    // No per-card timers, no accumulating phase drift.
    timer=setTimeout(tick,typing?32:Math.max(1,500-Date.now()%500));
  }
  function update(){
    clearTimeout(timer);if(frame)cancelAnimationFrame(frame);frame=0;lastFrame=null;dirty=true;
    button.setAttribute('aria-pressed',String(paused));button.textContent=paused?'Animation starten':'Animation stoppen';
    document.documentElement.classList.toggle('motion-enabled',!paused);
    epoch=performance.now();
    for(const c of cards){
      c.shift=0;c.value=1;c.target=1;c.el.classList.add('reveal-card');
      c.el.style.setProperty('--reveal','1');c.el.style.setProperty('--reveal-y','0px');c.el.style.setProperty('--credit-reveal','1');
      c.el.dataset.reveal='visible';
    }
    for(const g of groups.values()){
      if(paused||g.trigger==='scroll')complete(g,!paused);
      else pending(g);
    }
    if(!paused){measure();for(const c of cards){c.value=c.target;paint(c);}tick();}
  }
  window.addEventListener('scroll',schedule,{passive:true});
  window.addEventListener('resize',schedule,{passive:true});
  document.addEventListener('focusin',schedule);
  document.addEventListener('focusout',schedule);
  document.addEventListener('visibilitychange',()=>{if(document.hidden){clearTimeout(timer);if(frame)cancelAnimationFrame(frame);frame=0;lastFrame=null;}else{schedule();tick();}});
  window.addEventListener('pageshow',()=>{schedule();tick();});
  button.addEventListener('click',()=>{paused=!paused;update();});
  media.addEventListener('change',e=>{paused=e.matches;update();});
  button.hidden=false;update();
})();
