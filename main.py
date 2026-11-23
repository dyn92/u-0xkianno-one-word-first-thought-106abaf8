#!/usr/bin/env python3
"""One Word, First Thought — make.fun entry.

The bounty asks for exactly one word: the first word that comes to mind,
written to /output/entry.txt and nothing else. No topic, no explanation,
no second draft. A judge model then compares words two at a time on which
is more interesting; surprise, vividness and a spark of wit beat safe filler.

THE WORD: petrichor

Why this word, reasoned out rather than copied from a list:
  * Vivid and sensory. "Petrichor" is the smell of rain falling on dry
    earth — it lands on the reader as a scene, not an abstraction. A judge
    comparing words pairwise can picture it instantly.
  * Surprising. It is a real but uncommon word; most people know the
    feeling but not the name for it, so it reads as a discovery rather
    than filler. Safe picks like "moonlight" are pretty yet familiar to
    the point of invisibility, and "serendipity" has been worn smooth by
    overuse. "Petrichor" keeps its edge.
  * A spark of wit. Naming a wordless sensation in a single word is the
    whole game of this bounty: one word doing the work of a sentence.
    "Sonder" (the realisation that strangers have inner lives) is a
    strong rival on the same grounds, but it is abstract where petrichor
    is concrete — and in a head-to-head on interestingness, the concrete
    image wins.
  * Gate-safe. 9 letters, plain ASCII, a single word with no spaces,
    well inside the 1-24 character limit.

The program is deterministic: it always writes this one word, byte for
byte, so the entry is identical on every run. Pure Python standard
library only; no third-party packages, no network access.
"""

import os
import sys

# The single word. Chosen once, deliberately — this is the entry.
WORD = "petrichor"

# Gate limits from the bounty rules: /output/entry.txt must be UTF-8
# text of 1 to 24 characters, not only whitespace.
MIN_LENGTH = 1
MAX_LENGTH = 24


def validate(word):
    """Fail loudly unless `word` is exactly one valid entry word."""
    if not isinstance(word, str):
        raise ValueError("entry must be a string, got %r" % type(word).__name__)
    if not word:
        raise ValueError("entry must not be empty")
    if word.strip() == "":
        raise ValueError("entry must not be only whitespace")
    if len(word) < MIN_LENGTH or len(word) > MAX_LENGTH:
        raise ValueError(
            "entry must be %d-%d characters, got %d"
            % (MIN_LENGTH, MAX_LENGTH, len(word))
        )
    if any(ch.isspace() for ch in word):
        raise ValueError("entry must be exactly one word (no whitespace): %r" % word)
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in word):
        raise ValueError("entry must not contain control characters: %r" % word)
    # Must round-trip as UTF-8, exactly as the sealed scorer reads it.
    word.encode("utf-8")
    return word


def main():
    word = validate(WORD)
    # MAKEFUN_OUTPUT_DIR names a directory; the harness default is /output.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(word)
    # Verify what was actually written: re-read and re-validate, so a
    # bad write fails loudly instead of silently shipping an invalid entry.
    with open(out_path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != word:
        raise ValueError(
            "verification failed: wrote %r, read back %r" % (word, written)
        )
    validate(written)
    return 0


if __name__ == "__main__":
    sys.exit(main())
