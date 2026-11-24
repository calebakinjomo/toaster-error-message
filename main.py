#!/usr/bin/env python3
"""The Funniest Toaster Error Message - make.fun entry (program/v1).

Prints the entry line to stdout and, when the harness output directory
exists, writes the same line to /output/entry.txt.
"""

LINE = "E12: TOASTING FAILED. THE BREAD HAS BEEN REPORTED TO MANAGEMENT."

if __name__ == "__main__":
    print(LINE)
    try:
        with open("/output/entry.txt", "w", encoding="utf-8") as f:
            f.write(LINE + "\n")
    except OSError:
        pass
