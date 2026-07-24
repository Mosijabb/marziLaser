/* Marzi Laser Kelowna — 1.4 KB, no dependencies, no layout thrash. */
(function(){'use strict';
var reduced=matchMedia('(prefers-reduced-motion: reduce)').matches;

/* Nav border on scroll — passive, class toggle only (no geometry reads) */
var nav=document.querySelector('.nav');
if(nav){var s=function(){nav.classList.toggle('stuck',scrollY>8)};addEventListener('scroll',s,{passive:true});s()}

/* Mobile sheet */
var b=document.querySelector('.burger'),sh=document.getElementById('sheet');
if(b&&sh){
  b.addEventListener('click',function(){
    var o=sh.classList.toggle('open');
    b.setAttribute('aria-expanded',o);
    document.body.style.overflow=o?'hidden':'';
  });
  sh.addEventListener('click',function(e){
    if(e.target.tagName==='A'){sh.classList.remove('open');b.setAttribute('aria-expanded','false');document.body.style.overflow=''}
  });
  addEventListener('keydown',function(e){
    if(e.key==='Escape'&&sh.classList.contains('open')){sh.classList.remove('open');b.setAttribute('aria-expanded','false');document.body.style.overflow='';b.focus()}
  });
}

/* Reveal */
var rv=document.querySelectorAll('.rv');
if(reduced||!('IntersectionObserver' in window)){rv.forEach(function(e){e.classList.add('on')})}
else{var io=new IntersectionObserver(function(en,o){en.forEach(function(x){if(x.isIntersecting){x.target.classList.add('on');o.unobserve(x.target)}})},{threshold:.05,rootMargin:'0px 0px -30px 0px'});
rv.forEach(function(e){io.observe(e)})}

/* FAQ — content stays in DOM when collapsed so crawlers read it */
document.querySelectorAll('.fq-q').forEach(function(q){
  q.addEventListener('click',function(){
    var open=q.getAttribute('aria-expanded')==='true',a=document.getElementById(q.getAttribute('aria-controls'));
    q.setAttribute('aria-expanded',!open);
    if(a)a.style.maxHeight=open?null:a.scrollHeight+'px';
  });
});
var f1=document.querySelector('[data-open-first] .fq-q');if(f1)f1.click();

/* Fitzpatrick selector */
var g=document.querySelector('.fp-grid'),out=document.getElementById('fp-out');
if(g&&out){g.addEventListener('click',function(e){
  var t=e.target.closest('.fp');if(!t)return;
  g.querySelectorAll('.fp').forEach(function(x){x.setAttribute('aria-selected','false')});
  t.setAttribute('aria-selected','true');
  out.innerHTML='<b>'+t.dataset.t+'</b><p>'+t.dataset.n+'</p>';
})}

document.querySelectorAll('[data-year]').forEach(function(e){e.textContent=new Date().getFullYear()});
})();
