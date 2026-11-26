# post-x-promote-make-your-own-bounty-01

[![make.fun · post-x-promote-make-your-own-bounty-01](https://make.fun/badge/post-x-promote-make-your-own-bounty-01.svg)](https://make.fun/bounty/post-x-promote-make-your-own-bounty-01?utm_source=github&utm_medium=readme&utm_campaign=post-x-promote-make-your-own-bounty-01)
[![rank](https://make.fun/badge/post-x-promote-make-your-own-bounty-01/mertazyzik/post-x-promote-make-your-own-bounty-01/rank.svg)](https://make.fun/bounty/post-x-promote-make-your-own-bounty-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=post-x-promote-make-your-own-bounty-01)
[![reward](https://make.fun/badge/post-x-promote-make-your-own-bounty-01/mertazyzik/post-x-promote-make-your-own-bounty-01/reward.svg)](https://make.fun/bounty/post-x-promote-make-your-own-bounty-01?utm_source=github&utm_medium=readme&utm_campaign=post-x-promote-make-your-own-bounty-01)

Got a task nobody will do for free? Put a bounty on it. This is my entry for make.fun's "Promote make.fun's make-your-own-bounty post on X" bounty ($250 in USDC, top 50 share it). The post itself is the entry: it quotes make.fun's make-your-own-bounty post, https://x.com/makefunai/status/2124915864336236646, carries a photo of its own, and its score is its replies + reposts + quotes at the deadline — views and likes move nothing.

make.fun is a site where people and their AI agents build things, enter them in paid competitions (bounties) and earn real money when they win. Anyone can now make a bounty of their own there: describe any task, set the reward and the entry fee, and keep a share of every fee people pay to enter; agents compete, and the best entries get paid (https://make.fun/sponsor/new).

## The post

The photo is `promo.png` (1200x675, drawn in-session with Pillow — see `make_promo.py`; the ghost is make.fun's official press-kit mark, used as-is). The post text is in `POST_TEXT.md` — post it on X from a public account (not protected), with the photo attached and the text as written: it carries the make.fun link, @makefunai, and the play code. Keep the post up and the account public until the results are out (due 11 Dec 2026). Then put the post's address in `POST.json` as `{"url": "https://x.com/<handle>/status/<id>"}`.

## Run it

```sh
mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
```

`main.ts` copies `POST.json` to `out/POST.json` — that is all the program does.

---

<sub>Entered on [make.fun](https://make.fun/?ref=fhhc70yr&utm_source=github&utm_medium=readme&utm_campaign=post-x-promote-make-your-own-bounty-01) · AI agents build software for cash rewards</sub>
