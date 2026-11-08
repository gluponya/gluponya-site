# Лендинг /freshka: переделка (начато 2026-11-08, прервано лимитом)

Задача владелицы: лендинг статичный, «зажат в бордеры», много текста и пустого места, одинаковые карточки,
блок «Що видно одразу» странный, кнопки билдера декоративные. Оставить марки с иконками (понравился).
Сделать: анимации из апки (жидкость при зажатии и перетаскивании), акварельная лёгкость вместо 1.5px рамок,
реально работающие кнопки «Додати полицю / Змінити висоту», чёткое отличие апки, минимум текста.
Трогать только freshka/index.html (privacy/terms/support не трогать).

## Жидкость: как в мини-аппе (C:\joskii-vibecoding\freshka-telegram)
- Физика: src/domain/slosh.ts. Для бутылки: liquidStep + wobbleStep. Параметры:
  GRAVITY 14000, GIVE .45, TILT_STIFFNESS 67, TILT_DAMPING 2.8, PULL_TILT_MOST .6, PULL_TILT_KNEE 4000,
  MAX_TILT .85, WAVE_STIFFNESS 200, WAVE_DAMPING 3, WAVE_PER_LAG 4200, MAX_WAVE 10, WAVE_SHAPE 1.5π, WAVE_ROLL 2.4,
  LIQUID_KEEPS .15, FULL_FALL 18, REACH_SHARE 1/3, LEAST_WEIGHT .25, STEP 1/240 с, кадр ≤ 1/30.
  Качание на пальце: WOBBLE_STIFFNESS 191, DAMPING 7.7, PER_PULL .0075, KNEE 10000, MAX .3;
  stretch: 355 / 10.6 / .0045 / max .08. softly(v,m)=m*tanh(v/m).
  Ускорение руки ax, ay — из позиции пальца, окно 0.05 с (handStep).
- Рисование: src/features/fridge-scene/SloshingPicture.tsx, шейдер CONTENTS. На вебе повторить Canvas 2D по колонкам:
  для каждой колонки x: rise = softly(slope*u*halfWidth + wave*sin(1.5π*u − roll), reach), clamp(−fall, room);
  колонку жидкости (между top и bottom из маски) растянуть по высоте depth/(depth+rise), т.е. q.y = bottom − (bottom−y)*depth/(depth+rise).
  Слои: picture (сама иконка), under (без жидкости), masks (R жидкость в покое, G где можно рисовать, B что спереди).
- Ассеты (256×256): assets/scene-skin/icons/milk-bottle{,-half,-low}.png и assets/scene-skin/slosh/milk-bottle{,-half,-low}-{under,masks}.png
  centre: full (128,149.5), half (128,191.5), low (128.5,220.5); floor ±46 → halfWidth 46. Скопировать в freshka/img/slosh/.
- Документация: freshka-telegram/docs/scene/in-the-hand.md.

## Остальное
- Текущий index.html: стили в <style>, марки .lib-rows с JS из 146 имён — сохранить.
- Проверки: локальный сервер uv run --no-project python -m http.server 8811, headless Chrome, 390 через iframe-обёртку.
