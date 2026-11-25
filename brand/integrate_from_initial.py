from pathlib import Path
import json,re,hashlib,html
root=Path.cwd()
assert (root/'site/index.html').exists()
b=root/'brand'
g=json.loads((b/'glyphs.json').read_text(encoding='utf-8'))
assert hashlib.sha256((b/'glyphs.json').read_bytes()).hexdigest()=='ea11b09f0e8603b3667b18176850919bbbc74c1b596d1163528c9370d358acf0'
logo={"viewBox":"185 475 920 315","paths":[
"M204 493 L279 493 L383 618 L273 761 L200 760 L311 618 Z",
"M474 493 L647 493 L590 726 L543 770 L409 770 L377 707 L526 707 L565 546 L460 546 Z",
"M731 493 L930 493 L908 546 L747 546 L732 598 L872 598 L900 631 L873 728 L823 770 L625 770 L649 711 L809 711 L825 653 L688 653 L658 617 L680 537 Z",
"M916 714 L1085 714 L1072 769 L900 769 Z"],"source":"Approved transparent PNG, straight polygon fit from 50% alpha contour; raster mask IoU 0.9930172936186081"}
(b/'primary.json').write_text(json.dumps(logo,indent=2)+'\n',encoding='utf-8')
assets=root/'site'/'assets'
assets.mkdir(exist_ok=True)
def svg(name,motion=False,theme=None,cls=''):
    islogo=name=='JS'
    label={'JS':'JStudios','JStudios':'JStudios','Skolary':'Skolary by JStudios'}[name]
    box=logo['viewBox'] if islogo else ('-8 -8 724 102' if name=='JStudios' else '-8 -8 684 164')
    color=theme or 'currentColor'
    cname='brand-svg brand-'+name.lower()+(' typing' if motion else '')+(' '+cls if cls else '')
    s=f'<svg xmlns="http://www.w3.org/2000/svg" class="{cname}" viewBox="{box}" role="img" aria-label="{label}" fill="{color}" fill-rule="evenodd">'
    if islogo:
        for i,p in enumerate(logo['paths'][:-1]):
            s+=f'<path class="glyph glyph-{i}" d="{p}"/>'
        cursor=logo['paths'][-1]
        start=-510; afterj=-282
        if motion:
            s+=f'<path class="cursor-intro" d="{cursor}"/><path class="cursor-idle" d="{cursor}"/>'
        else:s+=f'<path d="{cursor}"/>'
    else:
        pos=g['positions'][name]
        for i,(ch,x) in enumerate(pos[:-1]):
            s+=f'<path class="glyph glyph-{i}" transform="translate({x} 0)" d="{g["glyphs"][ch]}"/>'
        x=pos[-1][1]
        if motion:
            s+=f'<g transform="translate({x} 0)"><path class="cursor-intro" d="{g["glyphs"]["_"]}"/><path class="cursor-idle" d="{g["glyphs"]["_"]}"/></g>'
        else:s+=f'<path transform="translate({x} 0)" d="{g["glyphs"]["_"]}"/>'
        if name=='Skolary':s+=f'<path class="brand-credit" d="{g["creditPath"]}"/>'
    return s+'</svg>'
for name in ['JS','JStudios','Skolary']:
    for color,val in [('white','#FFFFFF'),('black','#000000')]:
        (assets/f'{name.lower()}-{color}.svg').write_text(svg(name,theme=val)+'\n',encoding='utf-8')
(assets/'favicon.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 1000"><rect width="1000" height="1000" rx="160" fill="#000"/><g fill="#fff" transform="translate(-100 170) scale(.94)">' + ''.join(f'<path d="{p}"/>' for p in logo['paths'])+'</g></svg>',encoding='utf-8')
# Animated elements use the same path strings, never a second set of outlines.
css=['.brand-svg{display:block;max-width:100%;height:auto;color:inherit}.top .brand-js{width:108px}.hero .brand-jstudios,.product-hero .brand-skolary{width:min(100%,660px);margin:0 0 28px;color:#fff}.product .brand-skolary{width:min(100%,420px);margin:0 0 12px}.hero .brand-heading{margin:0 0 20px;font-size:clamp(1.9rem,4vw,3.2rem);letter-spacing:-.055em;line-height:1.1}.brand-credit{fill:currentColor}.typing .cursor-intro{display:none}.typing .cursor-idle{opacity:1}.motion-control{font:inherit;color:var(--muted);border:1px solid var(--line);background:transparent;padding:6px 10px;border-radius:7px;cursor:pointer}.motion-control:focus-visible{outline:2px solid var(--accent)}.motion-control[hidden]{display:none}.footer .brand-js{width:94px}.brand-hero{--start:1400ms}.motion-enabled .typing .glyph:not(.glyph-0){animation:brand-reveal 1ms step-end both;animation-delay:calc(var(--start,0ms) + var(--keytime))}.motion-enabled .typing .cursor-intro{display:block}.motion-enabled .typing .cursor-idle{animation:brand-idle 1s step-end infinite;animation-delay:calc(var(--start,0ms) + var(--end));animation-fill-mode:backwards}.motion-enabled .typing .brand-credit{animation:brand-reveal 1ms step-end both;animation-delay:calc(var(--start,0ms) + var(--end))}@keyframes brand-reveal{from{opacity:0}to{opacity:1}}@keyframes brand-idle{0%{opacity:1}50%{opacity:0}100%{opacity:1}}.motion-enabled .typing .cursor-idle{visibility:hidden;animation-name:brand-idle-visible}@keyframes brand-idle-visible{0%{visibility:visible;opacity:1}50%{visibility:visible;opacity:0}100%{visibility:visible;opacity:1}}.motion-enabled .typing .cursor-idle{animation-fill-mode:forwards}']
# Build exact discrete startup timing; final cursor appears at the final keystroke.
timings={'JS':[1200,1400],'JStudios':[1200,1400,1510,1620,1750,1850,1960,2070],'Skolary':[1200,1400,1510,1620,1740,1850,1960]}
for name,t in timings.items():
    key=name.lower(); end=t[-1]; cls=f'.typing.brand-{key}'
    offsets=[-510,-282,0] if name=='JS' else [x-g['positions'][name][-1][1] for ch,x in g['positions'][name][1:]]
    assert len(offsets)==len(t)+1
    css.append(f'{cls}'+'{--end:'+str(end)+'ms}')
    for i,when in enumerate(t,1):
        css.append(f'{cls} .glyph-{i}'+'{--keytime:'+str(when)+'ms}')
    # step-end maintains the current state until the following keyframe.
    frames=[(0,offsets[0],1),(500,offsets[0],0),(1000,offsets[0],1)]
    frames.extend((when,offsets[i+1],1) for i,when in enumerate(t[:-1]))
    frames.append((end,0,0))
    css.append(f'.motion-enabled {cls} .cursor-intro'+'{animation:brand-start-'+key+f' {end}ms steps(1,end) both;animation-delay:var(--start,0ms)'+'}')
    css.append('@keyframes brand-start-'+key+'{'+''.join(f'{ms/end*100:.9f}%{{transform:translateX({dx}px);opacity:{op}}}' for ms,dx,op in frames)+'}')
css.append('@media(prefers-reduced-motion:reduce){.motion-enabled .typing .glyph,.motion-enabled .typing .brand-credit,.motion-enabled .typing .cursor-idle{animation:none!important;visibility:visible;opacity:1}.motion-enabled .typing .cursor-intro{display:none}}.motion-off .typing .glyph,.motion-off .typing .brand-credit,.motion-off .typing .cursor-idle{animation:none!important;visibility:visible;opacity:1}.motion-off .typing .cursor-intro{display:none}.motion-enabled .typing .cursor-idle{animation-fill-mode:forwards}@media(max-width:480px){.top .brand-js{width:80px}.motion-control{font-size:.73rem}.hero .brand-jstudios,.product-hero .brand-skolary{margin-bottom:20px}}')
(assets/'brand.css').write_text('\n'.join(css)+'\n',encoding='utf-8')
(assets/'motion.js').write_text("""'use strict';
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
""",encoding='utf-8')
def replace_once(s,old,new):
    assert s.count(old)==1,old[:100]
    return s.replace(old,new,1)
for file in [root/'site/index.html',root/'site/skolary/index.html',root/'site/hinweise/index.html']:
    s=file.read_text(encoding='utf-8')
    s=replace_once(s,'</head>','<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="/assets/brand.css"><script src="/assets/motion.js"></script></head>')
    s,n=re.subn(r'<a class="wordmark" href="/"[^>]*>J<span>Studios</span><i></i></a>',lambda m:'<a class="wordmark" href="/" aria-label="JStudios Startseite">'+svg('JS',motion=file.name=='index.html' and file.parent.name!='hinweise')+'</a>',s)
    assert n==1
    if file.parent==root/'site':
        s=replace_once(s,'<h1>Technologie.<br><span class="gradient">Mit einem Zweck.</span></h1>','<h1 aria-label="JStudios">'+svg('JStudios',True,cls='brand-hero')+'</h1><h2 class="brand-heading">Technologie. Mit einem Zweck.</h2>')
        s=replace_once(s,'<div class="product-brand"><span class="lettermark" aria-hidden="true">Sk</span><div><h3>Skolary</h3><span class="muted">by JStudios</span></div></div>', '<h3 aria-label="Skolary by JStudios">'+svg('Skolary')+'</h3>')
    elif file.parent.name=='skolary':
        s=replace_once(s,'<div class="product-brand"><span class="lettermark large" aria-hidden="true">Sk</span><div><h1>Skolary</h1><span class="muted">by JStudios</span></div></div>','<h1 aria-label="Skolary by JStudios">'+svg('Skolary',True,cls='brand-hero')+'</h1>')
    s=s.replace('<small>© 2026 JStudios</small>','<button type="button" class="motion-control" aria-pressed="false" hidden>Animation stoppen</button><small>© 2026 JStudios</small>')
    file.write_text(s,encoding='utf-8',newline='\n')
headers=root/'site/_headers'
s=headers.read_text(encoding='utf-8')
assert "style-src 'self'" in s
headers.write_text(s.replace("style-src 'self'","style-src 'self'; script-src 'self'"),encoding='utf-8',newline='\n')
# Update privacy draft to describe actual proposed host, without adding private contacts.
p=root/'site/hinweise/index.html';s=p.read_text(encoding='utf-8')
s=s.replace('Beim Abruf verarbeitet der jeweilige Hostinganbieter technisch notwendige Verbindungsdaten.','Für die geplante Veröffentlichung über Cloudflare Pages verarbeitet Cloudflare beim Abruf technisch erforderliche Verbindungsdaten (z. B. IP-Adresse, Anfragezeit und Browserinformationen). Weitere Informationen: <a href="https://www.cloudflare.com/privacypolicy/">Cloudflare-Datenschutzrichtlinie</a>.')
p.write_text(s,encoding='utf-8',newline='\n')
(b/'README.md').write_text("""# JStudios Brand Kit v1.0

The approved wordmark glyphs are unchanged from v0.2 (SHA-256 ea11b09f0e8603b3667b18176850919bbbc74c1b596d1163528c9370d358acf0). The primary JS mark is a straight-polygon fit from the approved transparent PNG, not a new design (threshold mask IoU 99.30%). Both color variants share identical paths. The original PNG remains the definitive raster master. No ASUS font is included.

Startup: prompt and cursor at 0 ms, cursor off at 500, on at 1000, first key at 1200, second at 1400. The complete wordmark then blinks 500/500 ms. Header starts first; hero begins after 1400 ms. Reduced motion and a user-controlled stop switch show the static mark. No external scripts, fonts or tracking. The full glyph set is not a general-purpose typeface.

Public deployment requires completed operator and privacy information and repository-only authorization in Cloudflare.
""",encoding='utf-8')
# Save this deterministic build source, with original HTML templates retained in Git history.
print('BRAND_ASSETS_CREATED',len(list(assets.iterdir())))
print('GLYPH_MASTER_SHA256',hashlib.sha256((b/'glyphs.json').read_bytes()).hexdigest())
