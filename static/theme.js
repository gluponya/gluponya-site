/* Перекраска оверлеев за баллы («Сменить цвет оверлея»): палитра приходит со Глупостанции, через 5 минут возвращается своя.
   Перекрашивается всё: плашки и рамки (--pink), тени (--pink-hot), второй акцент (--mint), искорки и цифры (--yellow),
   фон и тёмный текст (--plum), карточки (--card), линии (--line), подписи (--muted). Цвета перетекают плавно.
   Один опрос /hub/theme на страницу (раз в 5 с, в «радуге» чаще): страницы со своей отрисовкой (фон, рамка камеры)
   не спрашивают Глупостанцию сами, а подписываются: window.gluTheme.on(j => …) — j как отдаёт /hub/theme. */
(() => {
  if (window.gluTheme) return;                 // скрипт подключили дважды — второй опрос не заводим
  const R = document.documentElement.style;
  const MAP = { pink: '--pink', hot: '--pink-hot', mint: '--mint', yellow: '--yellow',
                plum: '--plum', card: '--card', line: '--line', muted: '--muted' };
  const BASE = { pink: '#FF7ABE', hot: '#FF4FA3', mint: '#78EEC4', yellow: '#FFD84D',
                 plum: '#2E0C24', card: '#45173A', line: '#6B2E58', muted: '#D9B8CC' };
  const subs = [];
  let last = null;
  window.gluTheme = {
    on(fn) { subs.push(fn); if (last) try { fn(last); } catch (e) {} },
    get last() { return last; },
  };
  // регистрируем как цвета, чтобы смена шла плавным переходом, а не скачком
  try {
    if (window.CSS && CSS.registerProperty)
      for (const k in MAP) CSS.registerProperty({ name: MAP[k], syntax: '<color>', inherits: true, initialValue: BASE[k] });
    const st = document.createElement('style');
    st.textContent = ':root{transition:' + Object.values(MAP).map(v => v + ' 1.6s ease').join(',') + '}';
    (document.head || document.documentElement).appendChild(st);
  } catch (e) {}
  // запрос не висит дольше 4 с (AbortSignal.timeout есть не во всех версиях OBS)
  const T = ms => { if (window.AbortSignal && AbortSignal.timeout) return AbortSignal.timeout(ms);
                    const c = new AbortController(); setTimeout(() => c.abort(), ms); return c.signal; };
  let cur = '';
  const NO_SKIN = /^\/(panel|bot|tg)(\/|$)/.test(location.pathname);   // интерфейс пульта скином не трогаем
  const FORCE_SKIN = NO_SKIN ? '' : new URLSearchParams(location.search).get('skin');
  if (FORCE_SKIN && /^[a-z]{1,20}$/.test(FORCE_SKIN)) document.documentElement.dataset.skin = FORCE_SKIN;
  async function tick() {
    let fast = false;
    try {
      const r = await fetch('/hub/theme', { cache: 'no-store', signal: T(4000) });
      if (!r.ok) throw new Error(r.status);
      const j = await r.json();
      const pal = j.pal || (j.color ? { pink: j.color, hot: j.dark, mint: j.light } : null);
      fast = !!j.rainbow;
      const key = JSON.stringify(pal);
      if (key !== cur) {
        cur = key;
        for (const k in MAP) {
          if (pal && pal[k]) R.setProperty(MAP[k], pal[k]); else R.removeProperty(MAP[k]);
        }
      }
      // скин (07.11): <html data-skin="terminal"> — всё остальное делает CSS страницы. ?skin=… в адресе — для проверки
      const sk = NO_SKIN ? '' : FORCE_SKIN != null ? FORCE_SKIN : (j.skin && j.skin !== 'none' ? String(j.skin) : '');
      if (/^[a-z]{0,20}$/.test(sk) && (document.documentElement.dataset.skin || '') !== sk) {
        if (sk) document.documentElement.dataset.skin = sk; else delete document.documentElement.dataset.skin;
      }
      last = j;
      subs.forEach(fn => { try { fn(j); } catch (e) {} });
    } catch (e) {}
    setTimeout(tick, fast ? 2500 : 5000);    // следующий опрос — только когда этот закончился
  }
  if (/^https?:$/.test(location.protocol)) tick();
})();
