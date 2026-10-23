# Rolex Submariner: motion-этюд

Ролик на 57,6 с: карандаш → бумага → неоновый контур → 2D → 2,5D → 3D → разбор на детали → сборка → логотип. Раскадровка и выбор вариантов описаны в [STORYBOARD.md](STORYBOARD.md).

| Файл | Что это |
|---|---|
| `index.html` | Исходник анимации: SVG + CSS 3D, свой таймлайн (`window.__render(ms)` даёт детерминированный кадр, `#film` растягивает сцену на весь экран) |
| `audio/score.py` | Офлайн-синтез музыки и звуковых эффектов (numpy), 100 BPM, по тем же таймкодам |
| `audio/score.m4a` | Готовый микс, AAC |
| `build.py` | Собирает `dist/rolex-submariner.html` со встроенным звуком |
| `render_frames.py` | Покадровый рендер через Playwright для экспорта в MP4 |

Экспорт:

```bash
python3 audio/score.py score.wav
python3 render_frames.py page.html frames 120 0 1    # page.html = index.html в обёртке <html><body>
ffmpeg -framerate 120 -i frames/f%05d.jpg -i score.wav \
  -vf "tmix=frames=2,fps=60" -c:v libx264 -crf 17 -pix_fmt yuv420p -c:a aac -b:a 192k rolex-submariner.mp4
```

Неофициальный этюд. Rolex, Submariner, Oyster и корона являются товарными знаками Rolex SA.
