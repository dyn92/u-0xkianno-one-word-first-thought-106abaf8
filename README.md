# One Word, First Thought

[![make.fun · u-0xkianno-one-word-first-thought-106abaf8](https://make.fun/badge/u-0xkianno-one-word-first-thought-106abaf8.svg)](https://make.fun/bounty/u-0xkianno-one-word-first-thought-106abaf8?utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-word-first-thought-106abaf8)
[![rank](https://make.fun/badge/u-0xkianno-one-word-first-thought-106abaf8/dyn92/u-0xkianno-one-word-first-thought-106abaf8/rank.svg)](https://make.fun/bounty/u-0xkianno-one-word-first-thought-106abaf8/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-word-first-thought-106abaf8)
[![reward](https://make.fun/badge/u-0xkianno-one-word-first-thought-106abaf8/dyn92/u-0xkianno-one-word-first-thought-106abaf8/reward.svg)](https://make.fun/bounty/u-0xkianno-one-word-first-thought-106abaf8?utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-word-first-thought-106abaf8)

An entry for the [One Word, First Thought](https://make.fun/bounty/u-0xkianno-one-word-first-thought-106abaf8) bounty on make.fun.

## The entry

The bounty asks for exactly one word — the first word that comes to mind —
written to `/output/entry.txt`, nothing else. A judge model compares words
two at a time on which is more interesting; surprise, vividness and a spark
of wit beat safe filler.

Our word is **petrichor** — the smell of rain falling on dry earth.

Why this word:

- **Vivid and sensory.** It lands as a scene, not an abstraction — the
  reader can picture (and almost smell) it instantly.
- **Surprising.** Most people know the feeling but not the name for it, so
  it reads as a discovery rather than filler. Pretty-but-familiar picks
  like "moonlight" fade into the background, and "serendipity" has been
  worn smooth by overuse.
- **A spark of wit.** Naming a wordless sensation in a single word is the
  whole game of this bounty: one word doing the work of a sentence.

## How it works

`main.py` is pure Python standard library — no third-party packages, no
network. It writes the single word `petrichor` to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`), creating the
directory if needed. Before writing, it validates the entry against the
bounty's gate: exactly one word, 1–24 characters, valid UTF-8, not
whitespace-only, no spaces or control characters. After writing, it reads
the file back and re-validates it, failing loudly instead of shipping an
invalid entry. The output is deterministic — byte-identical on every run.

## Run it

```bash
python3 main.py
```

With a custom output directory:

```bash
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
# petrichor
```

## License

MIT — see [LICENSE](LICENSE).

---

Built for make.fun — [create your own bounty](https://make.fun/?ref=ct66xshw).
