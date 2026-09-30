/* 动漫原画设计 · 交互 */
(function () {
  'use strict';

  /* 1. 顶部进度条 */
  var bar = document.getElementById('progress');
  function progress() {
    var h = document.documentElement.scrollHeight - window.innerHeight;
    bar.style.width = (h > 0 ? (window.scrollY / h) * 100 : 0) + '%';
  }

  /* 2. 滚动出现 */
  var io = new IntersectionObserver(function (es) {
    es.forEach(function (e) {
      if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
    });
  }, { threshold: 0.08 });
  document.querySelectorAll('[data-reveal]').forEach(function (el) { io.observe(el); });

  /* 3. 模块筛选 */
  var filters = document.getElementById('filters');
  if (filters) {
    filters.addEventListener('click', function (ev) {
      var btn = ev.target.closest('button');
      if (!btn) return;
      filters.querySelectorAll('button').forEach(function (b) { b.classList.remove('on'); });
      btn.classList.add('on');
      var f = btn.dataset.f;
      document.querySelectorAll('#mods .mod').forEach(function (m) {
        var show = (f === 'all' || m.dataset.cat === f);
        m.classList.toggle('hide', !show);
      });
    });
  }

  /* 4. 导航高亮 */
  var links = Array.prototype.slice.call(document.querySelectorAll('#navlinks a'));
  var secs = links.map(function (a) { return document.querySelector(a.getAttribute('href')); });
  function highlight() {
    var y = window.scrollY + 160, cur = -1;
    secs.forEach(function (s, i) { if (s && s.offsetTop <= y) cur = i; });
    links.forEach(function (a, i) { a.classList.toggle('active', i === cur); });
  }

  /* 5. 回到顶部 */
  var top = document.getElementById('top');
  top.addEventListener('click', function () { window.scrollTo({ top: 0, behavior: 'smooth' }); });

  /* 6. 滚动监听（合并一次 rAF） */
  var ticking = false;
  function onScroll() {
    if (ticking) return;
    ticking = true;
    requestAnimationFrame(function () {
      progress(); highlight();
      top.classList.toggle('on', window.scrollY > 600);
      ticking = false;
    });
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();
})();
