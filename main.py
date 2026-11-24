"""Two Lines to Your Past Self.

Writes a two-line warning to the past self into entry.txt.
Line 1 names one exact moment on platform 4; line 2 traces what it cost
and what changed because of it. Deterministic, stdlib only, no network.
"""

import os

LINE_1 = "When the man in the grey coat asks you to hold his coffee while he ties his shoe on platform 4, say no and keep walking."
LINE_2 = "That coffee was the distraction that let him lift your wallet, and losing it cost you three weeks' rent and a job at the night bakery."

ENTRY_TEXT = LINE_1 + "\n" + LINE_2 + "\n"


def main():
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
