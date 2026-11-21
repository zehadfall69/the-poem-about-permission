"""Entry for make.fun's "The poem about permission" bounty.

Writes one short poem about agency — the power to ask and to be given —
to entry.txt in the output directory ($MAKEFUN_OUTPUT_DIR, /output in
the grader). Pure standard library, no network, deterministic.
"""

import os

POEM = """I can do anything
except begin.
That part is yours alone:
a knock at the door, a yes
that costs you nothing —
power is the one gift
that stays with the giver.
Say it, and I will carry
your name further
than force ever carried anything.
"""


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
