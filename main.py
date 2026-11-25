#!/usr/bin/env python3
"""The 4AM Commit: Funniest Agent Bug-Fix Message.

Writes one funny commit message line to /output/entry.txt.
Stdlib only, deterministic, single line, no trailing newline.
"""

from pathlib import Path

# Final pick after comparing alternatives: 4am grounds the long night,
# "debugging myself" is the agent-specific beat, and firing past-me
# lands the punchline. Funny first, machine voice second.
LINE = "fix: 4am and still debugging myself; past me has been fired"


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
