'use strict';
document.documentElement.classList.add('motion-enabled');
document.addEventListener('DOMContentLoaded',()=>{
  const button=document.querySelector('.motion-control');
  if(!button)return;
  button.hidden=false;
  const root=document.documentElement;
  const media=window.matchMedia('(prefers-reduced-motion: reduce)');
  let paused=media.matches;
  const update=()=>{root.classList.toggle('motion-off',paused);button.setAttribute('aria-pressed',String(paused));button.textContent=paused?'Animation starten':'Animation stoppen';};
  button.addEventListener('click',()=>{paused=!paused;update();});
  media.addEventListener('change',event=>{paused=event.matches;update();});
  update();
});
