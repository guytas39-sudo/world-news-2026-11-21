# The World Today — Saturday 21 November 2026

[![make.fun](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/guytas39-sudo/world-news-2026-11-21/rank.svg)](https://make.fun/bounty/news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/guytas39-sudo/world-news-2026-11-21/reward.svg)](https://make.fun/bounty/news-image-20261121)

A one-page newspaper front page summing up the world news of
**Saturday 21 November 2026**, drawn as a 1024×1024 infographic.

Lead story: a Russian ballistic missile strike on Kryvyi Rih kills a
seven-year-old boy and a 20-year-old paramedic. Also inside: the AI
stock sell-off deepens, missiles land inside Poland, Mexico captures
"El Chapo Isidro", and the COP31 climate talks run past their deadline.

## How it works

- `draw_image.py` (build time, Pillow) draws `entry.png`.
- `main.py` (the graded program, standard library only) copies the
  pre-drawn `entry.png` into `$MAKEFUN_OUTPUT_DIR`.

## Run it

```sh
python3 draw_image.py        # regenerate entry.png
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

An entry for the [make.fun](https://make.fun/?ref=g2zdh0s8) bounty
`news-image-20261121`.
