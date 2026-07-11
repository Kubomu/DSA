# Data Structures and Algorithms (DSA) in Python

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/Kubomu/DSA?quickstart=1)
[![Python 3.7+](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://www.python.org/downloads/)

Welcome to the DSA Learning Repository! This is a beginner-friendly collection of fundamental data structures and algorithms implemented in Python, designed to help you understand and master core computer science concepts, and then practise them with exercises that grade themselves as you go.

New to this? You do not need to install anything. Jump to [Try it now](#try-it-now-no-install-needed) and you will be running real code in your browser in under a minute.

## Table of Contents

- [Try it now (no install needed)](#try-it-now-no-install-needed)
- [Overview](#overview)
- [Repository Structure](#repository-structure)
- [Topics Covered](#topics-covered)
- [Getting Started](#getting-started)
- [Interactive practice with instant feedback](#interactive-practice-with-instant-feedback)
- [How to Use](#how-to-use)
- [Learning Path](#learning-path)
- [Resources](#resources)
- [Contributing](#contributing)
- [License](#license)

## Try it now (no install needed)

Click the green button below. GitHub builds a full Python workspace for you in the cloud (this is called a Codespace) with everything already set up. Nothing to download, nothing to configure.

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/Kubomu/DSA?quickstart=1)

Once it opens:

1. Wait a few seconds for the setup to finish. A small progress scoreboard prints in the terminal.
2. Run any example, for example: `python "Sorting Algorithms/merge_sort.py"`
3. Open `exercises/practice.py` and start solving. Check your progress any time with `python check.py`.

Prefer to work on your own machine instead? See [Getting Started](#getting-started) below.

## Overview

This repository contains clean, well-documented Python implementations of essential data structures and algorithms. Each implementation includes:

- Comprehensive docstrings explaining purpose, parameters, and complexity
- Error handling for robust code
- Time and space complexity analysis
- Test cases and examples demonstrating usage
- Detailed inline comments explaining the logic

## Repository Structure

```
DSA/
├── Computational Complexity and Big-O Notation/
│   ├── Intro.md                          Introduction to Big-O notation
│   ├── Notes.md                          Complexity analysis of algorithms
│   ├── Time Complexity/
│   │   ├── constant_time.py              O(1) examples
│   │   ├── linear_time.py                O(n) examples
│   │   └── quadratic_time.py             O(n^2) examples
│   └── Space Complexity/
│       ├── O(1).py                       Constant space examples
│       └── O(n).py                       Linear space examples
│
├── Data Structures/
│   ├── arrays.py                         Array operations
│   ├── linked_lists.py                   Singly linked list
│   ├── stacks.py                         Stack (LIFO)
│   ├── queue.py                          Queue (FIFO) with deque
│   ├── hash.py                           Hash functions
│   └── dictionary.py                     Dictionary/HashMap operations
│
├── Sorting Algorithms/
│   ├── bubble_sort.py                    O(n^2) sorting
│   └── merge_sort.py                     O(n log n) sorting
│
├── Searching Algorithms/
│   └── binary_search.py                  O(log n) search
│
├── Recursion/
│   └── factorial.py                      Recursive and iterative factorial
│
├── exercises/
│   ├── practice.py                       Self-grading exercises (start here after the lessons)
│   └── test_practice.py                  The autograder that checks your solutions
│
└── check.py                              Prints your exercise progress as a scoreboard
```

## Topics Covered

### Data Structures

| Data Structure | File | Time Complexity | Space |
|----------------|------|-----------------|-------|
| Arrays | `arrays.py` | Access: O(1), Search: O(n) | O(n) |
| Linked Lists | `linked_lists.py` | Append: O(n), Search: O(n) | O(n) |
| Stacks | `stacks.py` | Push/Pop: O(1) | O(n) |
| Queues | `queue.py` | Enqueue/Dequeue: O(1) | O(n) |
| Hash Functions | `hash.py` | Hash: O(k) where k = key length | O(1) |
| Dictionaries | `dictionary.py` | Insert/Lookup/Delete: O(1) avg | O(n) |

### Sorting Algorithms

| Algorithm | Best Case | Average Case | Worst Case | Space |
|-----------|-----------|--------------|------------|-------|
| Bubble Sort | O(n) | O(n^2) | O(n^2) | O(1) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) |

### Searching Algorithms

| Algorithm | Best Case | Average Case | Worst Case | Space |
|-----------|-----------|--------------|------------|-------|
| Binary Search | O(1) | O(log n) | O(log n) | O(1) |

### Computational Complexity

- Big-O Notation for understanding algorithm efficiency
- Time Complexity: O(1), O(n), O(n^2) examples
- Space Complexity: O(1), O(n) examples

## Getting Started

If you use the [Try it now](#try-it-now-no-install-needed) button above, you can skip this section entirely.

### Prerequisites

- Python 3.7 or higher
- Basic understanding of programming concepts

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Kubomu/DSA.git
   cd DSA
   ```

2. Install the one tool used by the exercises (pytest):
   ```bash
   pip install -r requirements.txt
   ```
   The lesson files use only the Python standard library, so they run without this step. You only need pytest to grade the practice exercises.

### Running the code

Each file can be run independently:

```bash
python "Data Structures/linked_lists.py"
python "Sorting Algorithms/merge_sort.py"
python "Searching Algorithms/binary_search.py"
```

## Interactive practice with instant feedback

Reading an algorithm is one thing. Writing it yourself, and getting told immediately whether you got it right, is how it sticks. That is what the `exercises/` folder is for.

**How it works:**

1. Open `exercises/practice.py`. There is one small exercise for each core topic: factorial, binary search, bubble sort, merge sort, a Stack, and a Queue. Each one has a `# TODO` where your code goes.
2. Fill in a `# TODO` with your own solution.
3. Ask for a friendly progress report:
   ```bash
   python check.py
   ```
   You will see a scoreboard, one line per topic:
   ```
     [x] 1. Recursion (factorial)   done
     [ ] 2. Binary search           todo
     [ ] 3. Bubble sort             todo
     ...
     Solved 1 of 6
   ```
4. Want the full detail on a result? Run the grader directly:
   ```bash
   pytest
   ```
5. Keep going until all six read `done`.

If you get stuck on a topic, open its matching lesson file (named in the exercise) for a worked example, then come back and try again. You cannot break anything, so experiment freely.

**Working in a fork?** When you push your solved `exercises/practice.py` to your own fork, GitHub automatically runs the same grader and shows a green check next to your commit once every exercise passes.

## How to Use

### 1. Study the theory first

Start with the complexity documentation in `Computational Complexity and Big-O Notation/` (`Intro.md` and `Notes.md`).

### 2. Explore the implementations

Each file contains class or function definitions with docstrings, inline comments, and test cases at the bottom in an `if __name__ == "__main__"` block.

### 3. Run the examples

```bash
python "Data Structures/stacks.py"
```

### 4. Practise and experiment

Solve the exercises in `exercises/practice.py`, change input values, add your own test cases, and compare performance with different input sizes.

## Learning Path

### Beginner (start here)

1. Computational Complexity: read `Intro.md` and `Notes.md`, study `constant_time.py` and `linear_time.py`
2. Basic Data Structures: `arrays.py`, `stacks.py`, `queue.py`
3. Simple Algorithms: `bubble_sort.py`, `factorial.py`
4. Practise: solve exercises 1, 3, 5, and 6 in `exercises/practice.py`

### Intermediate

5. Advanced Data Structures: `linked_lists.py`, `hash.py`, `dictionary.py`
6. Efficient Algorithms: `merge_sort.py`, `binary_search.py`
7. Space Complexity: study `O(1).py` and `O(n).py`
8. Practise: solve exercises 2 and 4 in `exercises/practice.py`

## Resources

- Big-O Cheat Sheet: [bigocheatsheet.com](https://www.bigocheatsheet.com/)
- Visualizations: [visualgo.net](https://visualgo.net/)
- Practice Problems: [leetcode.com](https://leetcode.com/), [hackerrank.com](https://www.hackerrank.com/)
- Books: "Introduction to Algorithms" by CLRS, "Grokking Algorithms" by Aditya Bhargava, "Data Structures and Algorithms in Python" by Goodrich et al.
- Python docs: [Python Official Docs](https://docs.python.org/3/), [collections module](https://docs.python.org/3/library/collections.html), [time complexity](https://wiki.python.org/moin/TimeComplexity)

## Contributing

Contributions are welcome:

1. Report bugs by opening a GitHub issue
2. Suggest improvements to implementations
3. Add new algorithms and data structures
4. Improve documentation

Areas for expansion: Trees, Graphs, Heaps, Tries, Union-Find; Quick Sort, Heap Sort, DFS, BFS, Dijkstra; Dynamic Programming; and more exercises in `exercises/practice.py`.

## License

This project is open source and available for educational purposes.

---

Happy learning! Understanding these fundamentals is key to becoming a better programmer. Take your time, experiment with the code, and enjoy the process.
