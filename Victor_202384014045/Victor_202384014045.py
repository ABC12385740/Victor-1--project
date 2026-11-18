"""Victor - 202384014045
Senior Capstone Project - first Python program.

This script implements the Mermaid flowchart in README.md:

    Start -> Decision?
      Yes -> Process -> End
      No  -> End

Run it with:
    python Victor_202384014045.py
    python Victor_202384014045.py --answer no

Author: Victor (202384014045)
"""

from __future__ import annotations

import argparse


def hello() -> str:
    """The classic first program from the class example."""
    return "Hello world"


def decision_flow(answer: str) -> list[str]:
    """Return the steps of the flowchart for a yes/no answer."""
    answer = answer.strip().lower()
    if answer in {"yes", "y"}:
        return ["Start", "Decision?", "Yes -> Process", "Process -> End"]
    if answer in {"no", "n"}:
        return ["Start", "Decision?", "No -> End"]
    raise ValueError("answer must be 'yes' or 'no'")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Victor 202384014045 - Mermaid flowchart in Python"
    )
    parser.add_argument(
        "--answer",
        choices=("yes", "no"),
        default="yes",
        help="follow the Yes or No branch (default: yes)",
    )
    args = parser.parse_args()

    print(hello())
    print("Victor - 202384014045")
    print()
    for step in decision_flow(args.answer):
        print(step)


if __name__ == "__main__":
    main()
