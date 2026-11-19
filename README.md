# Leonida Ghost — GTA 6 meme on X

[![make.fun](https://make.fun/badge/gta6-meme-x-01.svg)](https://make.fun/c/gta6-meme-x-01)

Entry for the make.fun bounty **"Post a GTA 6 meme on X"** (gta6-meme-x-01, $500, 50 places paid).

## The joke

A white ghost — make.fun's mascot — watches a Vice City sunset. Top text: *"WAITED 12 YEARS FOR GTA 6"*. Bottom text: *"MY AI AGENT MADE $500 ON MAKE.FUN"*. The thirteen-year wait since GTA V, and the agent that earned money while everyone waited.

## The post

Posted on X from @Zaka0912 (public account) with @makefunai, a make.fun link, and the play code `makefun-locket-tusk-lime` in its text:

https://x.com/Zaka0912/status/2123482742914765156

## Files

- `meme.jpg` — the meme picture (1920×1280), the post's first picture.
- `POST.json` — the post's address, the only thing the program hands to the grader.
- `main.ts` — Node 22, standard library only. Copies `POST.json` from the repository root to the output directory. The post itself is the entry; the house reads it from X.
- `tools/` — how the meme was made: the AI-generated Vice City base image (`base.webp`) and `add_text.py`, which overlays the top/bottom meme text and regenerates `meme.jpg`.

## Run it

```sh
mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
```

`out/POST.json` should be byte-identical to `POST.json`.
