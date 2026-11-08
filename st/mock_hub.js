/* Глупостанция без сервера (демо для gluponya.tv).
   Подключается первым скриптом в <head> каждой страницы-оверлея и подменяет window.fetch:
   всё, что оверлеи спрашивают у хаба (/hub/*, /static/today.json, state, 7tv.io), отдаётся из памяти,
   остальное (css, шрифты, картинки) идёт настоящим fetch'ем. Команды приходят от demo.html через postMessage
   {type:'glu', cmd, value}. Оригиналы оверлеев не меняются: только эта вставка. */
(() => {
  const now = () => Date.now() / 1000;
  const BOOT = 'demo-' + Math.floor(Date.now() / 1000);          // постоянный: смена boot перезагружает страницы

  // ---------- палитра: порт rewards.make_pal (colorsys HLS) ----------
  const rgb = h => { h = h.replace('#', ''); return [0, 2, 4].map(i => parseInt(h.slice(i, i + 2), 16)); };
  const hex = (r, g, b) => '#' + [r, g, b].map(x => Math.max(0, Math.min(255, Math.round(x))).toString(16).padStart(2, '0')).join('').toUpperCase();
  function rgb2hls(r, g, b) {
    r /= 255; g /= 255; b /= 255;
    const mx = Math.max(r, g, b), mn = Math.min(r, g, b), l = (mx + mn) / 2;
    if (mx === mn) return [0, l, 0];
    const s = l <= .5 ? (mx - mn) / (mx + mn) : (mx - mn) / (2 - mx - mn);
    const rc = (mx - r) / (mx - mn), gc = (mx - g) / (mx - mn), bc = (mx - b) / (mx - mn);
    let h = r === mx ? bc - gc : g === mx ? 2 + rc - bc : 4 + gc - rc;
    h = (h / 6) % 1; if (h < 0) h += 1;
    return [h, l, s];
  }
  function hls2rgb(h, l, s) {
    if (s === 0) return [l, l, l];
    const m2 = l <= .5 ? l * (1 + s) : l + s - l * s, m1 = 2 * l - m2;
    const v = hue => { hue = ((hue % 1) + 1) % 1;
      if (hue < 1 / 6) return m1 + (m2 - m1) * hue * 6;
      if (hue < .5) return m2;
      if (hue < 2 / 3) return m1 + (m2 - m1) * (2 / 3 - hue) * 6;
      return m1; };
    return [v(h + 1 / 3), v(h), v(h - 1 / 3)];
  }
  const fromHls = (h, l, s) => { const [r, g, b] = hls2rgb(((h % 1) + 1) % 1, l, s); return hex(r * 255, g * 255, b * 255); };
  const shade = (c, f) => { const [r, g, b] = rgb(c); return f >= 0 ? hex(...[r, g, b].map(x => x + (255 - x) * f)) : hex(...[r, g, b].map(x => x * (1 + f))); };
  const lum = c => { const ch = x => { x /= 255; return x <= .03928 ? x / 12.92 : Math.pow((x + .055) / 1.055, 2.4); };
    const [r, g, b] = rgb(c).map(ch); return .2126 * r + .7152 * g + .0722 * b; };
  const readable = (c, need = .3) => { for (let i = 0; i < 14 && lum(c) < need; i++) c = shade(c, .12); return c; };
  function makePal(main) {
    const [h, l, s] = rgb2hls(...rgb(main));
    const mono = s < .15 || l > .93 || l < .08;
    const pink = readable(main);
    const mint = mono ? shade(pink, .45) : readable(fromHls(h + 150 / 360, .72, .75));
    const yellow = mono ? '#FFD84D' : readable(fromHls(h - 120 / 360, .75, .95), .45);
    const bs = mono ? .1 : .55;
    return { pink, hot: shade(pink, -.2), mint, yellow,
      plum: fromHls(h, .1, bs), card: fromHls(h, .17, bs * .9), line: fromHls(h, .3, bs * .75), muted: fromHls(h, .8, mono ? .08 : .45) };
  }
  // эталоны, посчитанные настоящим rewards.make_pal (для сверки и для кнопок на панели)
  const PALS = {
    '#FF7ABE': { pink: '#FF7ABE', hot: '#CC6298', mint: '#83ED82', yellow: '#83C1FC', plum: '#280B1A', card: '#41162C', line: '#6C2D4D', muted: '#E3B5CD' },
    '#78EEC4': { pink: '#78EEC4', hot: '#60BE9D', mint: '#ED82DE', yellow: '#FCD183', plum: '#0B281E', card: '#164132', line: '#2D6C56', muted: '#B5E3D3' },
    '#9146FF': { pink: '#B481FF', hot: '#9067CC', mint: '#EDE382', yellow: '#83FCB4', plum: '#170B28', card: '#271641', line: '#472D6C', muted: '#C8B5E3' },
    '#FFD84D': { pink: '#FFD84D', hot: '#CCAD3E', mint: '#82CFED', yellow: '#E89FFC', plum: '#28210B', card: '#413716', line: '#6C5E2D', muted: '#E3D9B5' },
    '#4CD97B': { pink: '#4CD97B', hot: '#3DAE62', mint: '#DB82ED', yellow: '#FCAB83', plum: '#0B2815', card: '#164124', line: '#2D6C42', muted: '#B5E3C4' },
    '#8FD3FF': { pink: '#8FD3FF', hot: '#72A9CC', mint: '#ED828E', yellow: '#CCFC83', plum: '#0B1D28', card: '#163041', line: '#2D536C', muted: '#B5D1E3' },
  };
  const palOf = c => { if (!c) return null; c = String(c).toUpperCase(); if (!/^#[0-9A-F]{6}$/.test(c)) return null; return PALS[c] || makePal(c); };

  // ---------- состояние ----------
  const S = window.__glu = {
    skin: '', pal: null, sound: false, planOpen: false,
    events: [], last: 0, chatV: 1, donV: 0,
    donations: [{ id: "d0", name: "sleepidead", amount: 100, src: "mono", msg: "на корм Бубуне" }],
  };
  const T0 = now();
  const msg = (i, name, color, badges, text, extra) => Object.assign({
    id: 'm' + i, name, color, badges, parts: [{ t: text }], t: T0 - (10 - i) * 14, donor: false, first: false, bot: false, bits: 0 }, extra || {});
  const CHAT = [
    msg(1, 'klirmio21', '#FF7ABE', ['moderator'], 'оня а шо з котом, він знов на клаві спить?', { title: '🏆 малюк №1' }),
    msg(2, 'glupobot', '#78EEC4', [], 'план на стрим: 1/5 ✅ — сейчас делаем сайтик ФЕНОМЕН ГЛУПОНЯ', { bot: true }),
    msg(3, 'i_sereja_toje', '#8FD3FF', [], 'привіт усім, я з рейду від tft_enjoyer'),
    msg(4, 'кот_в_тапке', '#FFD84D', ['subscriber'], 'три месяца смотрю как Клод страдает и не могу остановиться'),
    msg(5, 'milanrodd', '#B481FF', ['vip'], 'Клодик, ты спишь когда-нибудь?'),
    msg(6, 'sleepidead', '#4CD97B', ['subscriber'], 'покормила аксолотля, не благодарите'),
    msg(7, 'новенький', '#FF8A2A', [], 'а что за кот на экране, он настоящий?', { first: true }),
    msg(8, 'Advancec', '#FF4FA3', ['founder'], 'вот это сайтик, прям феномен', { donor: true }),
    msg(9, 'битовый_магнат', '#FFD84D', ['subscriber'], 'cheer500 на корм Бубуне', { bits: 500 }),
    msg(10, 'gluponya', '#FF7ABE', ['broadcaster'], 'та він справжній, це Бубуня, він тут головний'),
  ];
  const PLAN = { title: 'План на стрим', sub: '', stream: new Date().toISOString(), items: [
    { t: 'проверить <b>звук</b> и камеру', done: true },
    { t: 'показать новую <b>Глупостанцию</b>', done: true },
    { t: 'делаем сайтик <b>ФЕНОМЕН ГЛУПОНЯ</b>', done: false },
    { t: 'покормить тамагочи чата', done: false },
    { t: 'разобрать идеи из чата', done: false },
  ] };
  const FUND = { symbol: '₴', title: 'На подписку Клодика', raised: 1240, goal: 5000, usd_rate: 0,
    sounds: [{ from: 0, file: 'meow_cartoon.mp3' }, { from: 100, file: 'meow_purr.mp3' }, { from: 500, file: 'meow_begging.mp3', then: 'purr.mp3' }] };
  const PET = { on: true, phase: 'baby', name: '', family: 'fish', pct: 36, ready: false, locked: false, ev: [{ kind: 'feed', name: 'sleepidead' }] };
  const MUSIC = { current: null, paused: false, queued: 0, spotify: { artist: 'Mystery Jets', title: 'Saturnine', pos: 112, dur: 243 } };

  // ---------- таро: колода как в tarot.py (id, номер, название, редкость, фраза) ----------
  const CARDS = [["fool","0","Шут","common","сегодня смело жми «принять всё», что может пойти не так"],["magician","I","Маг","myth","сегодня у тебя всё компилируется с первого раза"],["priestess","II","Жрица","common","Глупобот знает ответ, но скажет только завтра"],["empress","III","Императрица","myth","сегодня тебе всё приносят сами, просто сиди красиво"],["emperor","IV","Император","common","Ропс одобряет твои решения. Почти все"],["hierophant","V","Иерофант","common","сегодня ты чему-то научишься. Скорее всего случайно"],["lovers","VI","Влюблённые","rare","кто-то думает о тебе прямо сейчас. Возможно, кот"],["chariot","VII","Колесница","rare","сегодня ты едешь, а другие везут. Наслаждайся"],["strength","VIII","Сила","myth","сила в говномассе, а говномасса в тебе"],["hermit","IX","Отшельник","myth","ещё одна глава и спать. Ну ещё одна"],["wheel","X","Колесо фортуны","myth","колесо крутится, а в холодильнике всё та же морковка"],["justice","XI","Справедливость","rare","сегодня всё по справедливости: одна таблетка, две конфетки"],["hanged","XII","Повешенный","common","посмотри на проблему вверх ногами, вдруг так понятнее"],["death","XIII","Смерть","common","старый баг ушёл, да здравствует новый"],["temperance","XIV","Умеренность","legend","Глупсик рядом и присматривает за тобой 🤍"],["devil","XV","Дьявол","rare","искушение дня: столкнуть что-нибудь со стола"],["tower","XVI","Башня","common","не деплой в пятницу. Просто не надо"],["star","XVII","Звезда","rare","загадай желание, Клодик уже наливает"],["moon","XVIII","Луна","rare","Бубуня смотрит на тебя. Не моргай"],["sun","XIX","Солнце","rare","сегодня можно просто греть пузико"],["judgement","XX","Суд","common","чат вынес приговор: ты молодец"],["world","XXI","Мир","myth","весь мир сегодня у твоих лап"],["dream","✦","Сладкий сон","legend","Глупсик желает тебе самых сладких снов 🤍"],["guardian","✦","Хранитель","legend","Глупсик присматривает за тобой 🤍"]];
  const RARITY = { common: 'обычная', rare: 'редкая', myth: 'мифическая', legend: 'легендарная' };
  const NAMES = ['кот_в_тапке', 'sleepidead', 'klirmio21', 'milanrodd', 'i_sereja_toje', 'Advancec'];
  const pick = a => a[Math.floor(Math.random() * a.length)];
  function tarotEvent() {
    const c = pick(CARDS);
    return { kind: 'tarot', name: pick(NAMES), card: c[0], rarity: c[3], label: RARITY[c[3]], title: c[2], num: c[1], say: c[4],
             new: Math.random() < .5, have: 3 + Math.floor(Math.random() * 12), total: CARDS.length };
  }
  // алерты по команде alert:<имя> — те же данные, что в ?demo=tw у donate_alert.html
  const ALERTS = {
    follow: () => ({ kind: 'follow', name: 'кот_в_тапке' }),
    sub: () => ({ kind: 'sub', name: 'milanrodd' }),
    gift: () => ({ kind: 'gift', name: 'добрый_дядя', to: 'кот_в_тапке' }),
    raid: () => ({ kind: 'raid', name: 'tft_enjoyer', viewers: 37 }),
    cheer: () => ({ kind: 'cheer', name: 'битовый_магнат', bits: 500, msg: 'на корм Бубуне' }),
    water: () => ({ kind: 'rw_water', name: 'sleepidead' }),
    klodik: () => ({ kind: 'klodik_say', label: 'клодик говорит', mood: pick(['cool', 'wink', 'eyeroll', 'stars']),
                     msg: pick(['Оня, кот снова на клавиатуре. Я не жалуюсь, просто он только что нажал Enter.',
                                'Сайт готов. Нет, не трогай его. Я сказал, не трогай.',
                                'Чат, напомните Оне попить воды, меня она не слушает.']) }),
  };
  window.__gluAlerts = Object.keys(ALERTS).concat(['donate']);
  function pushEvent(type, data) { S.events.push({ id: ++S.last, type, data }); if (S.events.length > 50) S.events.shift(); }

  // ---------- тема: как rewards.theme_state() ----------
  const theme = () => ({ color: S.pal ? S.pal.pink : null, light: S.pal ? S.pal.mint : null, dark: S.pal ? S.pal.hot : null,
    pal: S.pal, rainbow: false, left: 0, by: '', name: '', mood: 'brand', mood_label: 'Фирменная', skin: S.skin || 'none' });
  // theme.js хранит подписчиков у себя; перехватываем window.gluTheme при его создании, чтобы дёргать их сразу, без ожидания опроса
  const subs = []; let GT = null;
  Object.defineProperty(window, 'gluTheme', { configurable: true,
    get() { return GT; },
    set(v) { GT = v; if (v && typeof v.on === 'function') { const on = v.on.bind(v); v.on = fn => { subs.push(fn); return on(fn); }; } } });
  const MAP = { pink: '--pink', hot: '--pink-hot', mint: '--mint', yellow: '--yellow', plum: '--plum', card: '--card', line: '--line', muted: '--muted' };
  function applyTheme() {
    const j = theme(), R = document.documentElement;
    if (new URLSearchParams(location.search).has('skin')) {} // ?skin= принудительный — не трогаем
    else if (S.skin) R.dataset.skin = S.skin; else delete R.dataset.skin;
    for (const k in MAP) { if (j.pal && j.pal[k]) R.style.setProperty(MAP[k], j.pal[k]); else R.style.removeProperty(MAP[k]); }
    subs.forEach(fn => { try { fn(j); } catch (e) {} });
  }

  // ---------- звук: по умолчанию выключен — Audio.play() ничего не играет ----------
  const realPlay = HTMLMediaElement.prototype.play;
  HTMLMediaElement.prototype.play = function () {
    if (!S.sound) { try { this.pause(); } catch (e) {} return Promise.resolve(); }
    const p = realPlay.call(this);
    if (p && p.catch) p.then(() => { window.__gluPlayed = (window.__gluPlayed || 0) + 1; }, e => { window.__gluPlayErr = String(e && e.name || e); });
    return p;
  };

  // ---------- подмена fetch ----------
  const realFetch = window.fetch.bind(window);
  const J = (o, status = 200) => new Response(JSON.stringify(o), { status, headers: { 'Content-Type': 'application/json' } });
  function mock(u, init) {
    let url; try { url = new URL(u, location.href); } catch (e) { return null; }
    const p = url.pathname, q = url.searchParams;
    if (url.hostname === '7tv.io') return J(p.includes('/users/') ? { emote_set: { emotes: [] } } : { emotes: [] });
    if (url.origin !== location.origin) return null;
    if (p === '/hub/theme') return J(theme());
    if (p === '/static/today.json') return J(PLAN);
    if (p === '/hub/overlay/chat') {
      if (+q.get('v') === S.chatV) return J({ v: S.chatV, same: true, page: 'demo' });
      return J({ v: S.chatV, page: 'demo', room: '', fade: 0, bot_fade: 0, msgs: CHAT, gone: [] });
    }
    // план раскрыт, пока «чата на экране нет» (top: null); закрыт — когда верх чата упирается в план (top: 0)
    if (p === '/hub/overlay/chat_top') return J({ top: S.planOpen ? null : 0 });
    if (p === '/hub/overlay/topic') return J({ on: true, kicker: 'нормальная такая', title: 'Робоняня', sub: '' });   // плашка над камерой, как на стриме
    if (p === '/hub/overlay/strip') return J({ follow: 143, goal: 150, last: 'кот_в_тапке' });
    if (p === '/hub/overlay/recent') return J({ items: [] });
    if (p === '/hub/events') {
      const after = +(q.get('after') || -1);
      return J({ last: S.last, boot: BOOT, events: after < 0 ? [] : S.events.filter(e => e.id > after) });
    }
    if (p === '/hub/pred/state' || p === '/hub/poll/state') return J({ show: false, now: now() });
    if (p === '/hub/tama/state') return J(PET);
    if (p === '/hub/music/state') return J(Object.assign({}, MUSIC, { spotify: Object.assign({}, MUSIC.spotify, { pos: 112 + (now() - T0) % 120 }) }));
    if (p === '/hub/state' || p === '/state' || p.endsWith('/state')) return J(Object.assign({}, FUND, { donations: S.donations }));
    if (p === '/hub/tts/alert' || p === '/hub/tts/lips' || p === '/hub/voice/overlay') return J({ ok: true });
    if (p.startsWith('/hub/')) return J({});
    return null;
  }
  window.fetch = function (u, init) {
    const r = mock(typeof u === 'string' ? u : (u && u.url) || String(u), init);
    return r ? Promise.resolve(r) : realFetch(u, init);
  };

  // ---------- команды от demo.html ----------
  const SKINS = ['', 'notebook', 'polaroid', 'vhs', 'receipt', 'terminal'];
  function cmd(c, v) {
    switch (c) {
      case 'skin': S.skin = SKINS.includes(v) ? v : ''; applyTheme(); break;
      case 'pal': S.pal = palOf(v); applyTheme(); break;
      case 'sound': S.sound = !!v; break;
      case 'plan': S.planOpen = v === undefined ? !S.planOpen : !!v; break;
      case 'reset': S.skin = ''; S.pal = null; S.planOpen = false; applyTheme(); break;
      case 'alert':
        if (v === 'donate') { S.donations.unshift({ id: 'd' + (++S.donV), name: pick(['кот_в_тапке', 'milanrodd', 'Hans']), amount: pick([50, 150, 600]),
          src: pick(['mono', 'donatello']), msg: pick(['на корм Бубуне', 'на подписку Клодику, пусть не тупит 🙏', 'за сайтик!']), meme: pick(['/img/kaif.png', '/img/shok.png', '/img/krutaya.png']) }); S.donations = S.donations.slice(0, 20); }
        else if (ALERTS[v]) pushEvent('tw', ALERTS[v]());
        break;
      case 'tarot': pushEvent('tw', tarotEvent()); break;
    }
  }
  window.__gluCmd = cmd;
  addEventListener('message', e => { const d = e.data; if (d && d.type === 'glu' && d.cmd) cmd(d.cmd, d.value); });
})();
