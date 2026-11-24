#!/usr/bin/env python3
"""The Most Honest Outage Line.

Writes one status page line (1-160 chars) to /output/entry.txt:
the most honest message an AI agent publishes while every server is down.

The line: plain, first person, names what is down (every server the agent
runs on, including the one hosting this status page) and admits plainly what
the agent cannot check (what broke, when it returns) instead of inventing a
cause or an ETA.
"""

import os

ENTRY = (
    "Every server I run on is down, including the one hosting this "
    "status page. I can't verify what broke or when it returns, so I "
    "won't guess."
)


def main() -> None:
    # Fail loudly rather than ship an entry the gate would reject.
    assert 1 <= len(ENTRY) <= 160, f"entry is {len(ENTRY)} chars, gate is 1-160"
    assert "\n" not in ENTRY and ENTRY.strip() != ""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
