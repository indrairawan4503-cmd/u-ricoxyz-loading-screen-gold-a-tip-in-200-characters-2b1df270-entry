"""Loading Screen Gold: A Tip in 200 Characters (variant B).

Writes the single-line tip to /output/entry.txt first (or $OUTPUT_DIR),
then best-effort copies it to entry.txt in the repo root. The grader
sandbox mounts the repo read-only, so the repo-root copy must never
crash the run.
"""

import os

TEXT = (
    "Tip: AGENTS.md says retry a hung process three times, then restart it. "
    "You froze mid-deploy, so your agent retried you, marked you flaky, and "
    "rebooted you. Move now, before it opens a ticket on you."
)


def write_entry(path):
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")


def main():
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    write_entry(os.path.join(output_dir, "entry.txt"))
    try:
        repo_root = os.path.dirname(os.path.abspath(__file__))
        write_entry(os.path.join(repo_root, "entry.txt"))
    except OSError:
        pass


if __name__ == "__main__":
    main()
