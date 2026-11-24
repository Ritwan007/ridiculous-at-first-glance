"""Ridiculous at First Glance, Real by the Second.

Writes one sentence (<=200 chars) pitching a bizarre startup that is a
real business: a professional worrier for hire. The pitch turns from
laughing (renting someone to worry for you) to nodding (insomniacs pay
less than therapy to finally sleep).
"""

import os

SENTENCE = (
    "We rent you a professional worrier who frets about your deadlines "
    "on a strict schedule, so you can finally sleep \u2014 insomniacs pay "
    "$30 a night because outsourcing your anxiety is cheaper than therapy."
)

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    text = SENTENCE.strip()
    # Gate: one sentence, 1-200 characters, valid UTF-8.
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert sum(text.count(c) for c in ".!?") == 1, "entry must be one sentence"
    assert text == text.encode("utf-8").decode("utf-8")
    os.makedirs(os.path.dirname(OUTPUT_PATH) or ".", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
