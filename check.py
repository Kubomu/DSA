"""
Friendly progress checker for the practice exercises.

Run it from the repo folder:

    python check.py

It runs the autograder and prints one line per topic so you can see, at a
glance, what you have solved and what is left. For the full detail behind any
result, run `pytest` instead.
"""

import re
import subprocess
import sys

# (label shown to the learner, substring that identifies that topic's tests)
TOPICS = [
    ("1. Recursion (factorial)", "test_factorial"),
    ("2. Binary search", "test_binary_search"),
    ("3. Bubble sort", "test_bubble_sort"),
    ("4. Merge sort", "test_merge_sort"),
    ("5. Stack (LIFO)", "test_stack"),
    ("6. Queue (FIFO)", "test_queue"),
]


def main():
    result = subprocess.run(
        [sys.executable, "-m", "pytest", "exercises", "-q", "-rA", "--no-header"],
        capture_output=True,
        text=True,
    )
    output = result.stdout + result.stderr

    passed = set(re.findall(r"PASSED\s+\S*::(\w+)", output))
    failed = set(re.findall(r"(?:FAILED|ERROR)\s+\S*::(\w+)", output))

    solved = 0
    print()
    print("=====================================")
    print("  DSA Practice - your progress")
    print("=====================================")
    for label, key in TOPICS:
        has_pass = any(key in name for name in passed)
        has_fail = any(key in name for name in failed)
        done = has_pass and not has_fail
        if done:
            solved += 1
        box = "[x]" if done else "[ ]"
        state = "done" if done else "todo"
        print(f"  {box} {label:<26} {state}")
    print("-------------------------------------")
    print(f"  Solved {solved} of {len(TOPICS)}")
    if solved == len(TOPICS):
        print("  Every topic passes. Well done.")
    else:
        print("  Edit exercises/practice.py, then run  python check.py  again.")
    print()

    # exit non-zero until everything passes, so CI and editors can react to it
    sys.exit(0 if solved == len(TOPICS) else 1)


if __name__ == "__main__":
    main()
