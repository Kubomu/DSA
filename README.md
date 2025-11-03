# Data Structures and Algorithms (DSA) Learning Repository

Welcome to the **DSA Learning Repository**! This is a comprehensive, beginner-friendly collection of fundamental data structures and algorithms implemented in Python, designed to help you understand and master core computer science concepts.

## 📚 Table of Contents

- [Overview](#overview)
- [Repository Structure](#repository-structure)
- [Topics Covered](#topics-covered)
- [Getting Started](#getting-started)
- [How to Use](#how-to-use)
- [Learning Path](#learning-path)
- [Code Quality](#code-quality)
- [Contributing](#contributing)
- [Resources](#resources)

## 🎯 Overview

This repository contains clean, well-documented Python implementations of essential data structures and algorithms. Each implementation includes:

- **Comprehensive docstrings** explaining purpose, parameters, and complexity
- **Error handling** for robust, production-quality code
- **Time and space complexity analysis** for performance understanding
- **Test cases and examples** demonstrating usage
- **Detailed inline comments** explaining the logic

## 📁 Repository Structure

```
DSA/
├── Computational Complexity and Big-O Notation/
│   ├── Intro.md                          # Introduction to Big-O notation
│   ├── Notes.md                          # Complexity analysis of algorithms
│   ├── Time Complexity/
│   │   ├── constant_time.py              # O(1) examples
│   │   ├── linear_time.py                # O(n) examples
│   │   └── quadratic_time.py             # O(n²) examples
│   └── Space Complexity/
│       ├── O(1).py                       # Constant space examples
│       └── O(n).py                       # Linear space examples
│
├── Data Structures/
│   ├── arrays.py                         # Array operations
│   ├── linked_lists.py                   # Singly linked list
│   ├── stacks.py                         # Stack (LIFO)
│   ├── queue.py                          # Queue (FIFO) with deque
│   ├── hash.py                           # Hash functions
│   └── dictionary.py                     # Dictionary/HashMap operations
│
├── Sorting Algorithms/
│   ├── bubble_sort.py                    # O(n²) sorting
│   └── merge_sort.py                     # O(n log n) sorting
│
├── Searching Algorithms/
│   └── binary_search.py                  # O(log n) search
│
└── Recursion/
    └── factorial.py                      # Recursive and iterative factorial
```

## 🔍 Topics Covered

### Data Structures (6 implementations)

| Data Structure | File | Time Complexity | Space |
|----------------|------|-----------------|-------|
| **Arrays** | `arrays.py` | Access: O(1), Search: O(n) | O(n) |
| **Linked Lists** | `linked_lists.py` | Append: O(n), Search: O(n) | O(n) |
| **Stacks** | `stacks.py` | Push/Pop: O(1) | O(n) |
| **Queues** | `queue.py` | Enqueue/Dequeue: O(1) | O(n) |
| **Hash Functions** | `hash.py` | Hash: O(k) where k=key length | O(1) |
| **Dictionaries** | `dictionary.py` | Insert/Lookup/Delete: O(1) avg | O(n) |

### Algorithms

#### Sorting Algorithms (2 implementations)

| Algorithm | Best Case | Average Case | Worst Case | Space |
|-----------|-----------|--------------|------------|-------|
| **Bubble Sort** | O(n) | O(n²) | O(n²) | O(1) |
| **Merge Sort** | O(n log n) | O(n log n) | O(n log n) | O(n) |

#### Searching Algorithms (1 implementation)

| Algorithm | Best Case | Average Case | Worst Case | Space |
|-----------|-----------|--------------|------------|-------|
| **Binary Search** | O(1) | O(log n) | O(log n) | O(1) |

### Computational Complexity

- **Big-O Notation** - Understanding algorithm efficiency
- **Time Complexity** - O(1), O(n), O(n²) examples
- **Space Complexity** - O(1), O(n) examples

## 🚀 Getting Started

### Prerequisites

- **Python 3.x** (3.7 or higher recommended)
- Basic understanding of programming concepts
- Familiarity with Python syntax (helpful but not required)

### Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd DSA
   ```

2. **No external dependencies required!** All implementations use Python's standard library.

### Running the Code

Each file can be run independently:

```bash
# Run a specific implementation
python "Data Structures/linked_lists.py"
python "Sorting Algorithms/merge_sort.py"
python "Searching Algorithms/binary_search.py"
```

## 📖 How to Use

### 1. **Study the Theory First**

Start with the complexity documentation:
```bash
# Read the Big-O introduction
cat "Computational Complexity and Big-O Notation/Intro.md"

# Study complexity analysis
cat "Computational Complexity and Big-O Notation/Notes.md"
```

### 2. **Explore Implementations**

Each file contains:
- **Class/function definitions** with comprehensive docstrings
- **Implementation details** with inline comments
- **Test cases** at the bottom (in `if __name__ == "__main__"` blocks)

Example:
```python
# Read and understand the code
from "Data Structures.stacks" import Stack

# Create and use the data structure
stack = Stack()
stack.push(10)
stack.push(20)
print(stack.pop())  # Output: 20
```

### 3. **Run Examples**

Execute files to see the output:
```bash
python "Data Structures/stacks.py"
```

### 4. **Modify and Experiment**

- Change input values
- Add your own test cases
- Implement additional methods
- Compare performance with different input sizes

## 🎓 Learning Path

### Beginner Level (Start Here!)

1. **Computational Complexity**
   - Read `Intro.md` and `Notes.md`
   - Study `constant_time.py`, `linear_time.py`
   - Understand Big-O notation

2. **Basic Data Structures**
   - Arrays: `arrays.py`
   - Stacks: `stacks.py`
   - Queues: `queue.py`

3. **Simple Algorithms**
   - Bubble Sort: `bubble_sort.py`
   - Recursion: `factorial.py`

### Intermediate Level

4. **Advanced Data Structures**
   - Linked Lists: `linked_lists.py`
   - Hash Functions: `hash.py`
   - Dictionaries: `dictionary.py`

5. **Efficient Algorithms**
   - Merge Sort: `merge_sort.py`
   - Binary Search: `binary_search.py`

6. **Space Complexity**
   - Study `O(1).py` and `O(n).py`
   - Understand trade-offs between time and space

## ✅ Code Quality

All code in this repository follows best practices:

### Documentation
- ✅ Comprehensive docstrings for all functions and classes
- ✅ Type hints in docstrings (Args, Returns, Raises)
- ✅ Time and space complexity annotations
- ✅ Usage examples in docstrings

### Error Handling
- ✅ Input validation (type checking)
- ✅ Proper exception raising with meaningful messages
- ✅ Edge case handling (empty arrays, invalid inputs)

### Performance
- ✅ Optimized implementations (e.g., Queue uses `collections.deque` for O(1) operations)
- ✅ Early termination optimizations where applicable
- ✅ Overflow prevention (e.g., binary search uses safe mid calculation)

### Testing
- ✅ Test cases included in each file
- ✅ Multiple scenarios covered (normal, edge cases, error cases)
- ✅ Expected outputs documented

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Report bugs** - Found an issue? Open a GitHub issue
2. **Suggest improvements** - Ideas for better implementations
3. **Add new algorithms** - Implement additional DSA topics
4. **Improve documentation** - Clarify explanations or add examples

### Areas for Expansion

We'd love contributions in these areas:

**Data Structures:**
- Trees (Binary Search Trees, AVL Trees, Red-Black Trees)
- Graphs (Adjacency List, Adjacency Matrix)
- Heaps (Min Heap, Max Heap, Priority Queue)
- Tries
- Disjoint Set (Union-Find)

**Algorithms:**
- Quick Sort, Heap Sort, Radix Sort
- Graph algorithms (DFS, BFS, Dijkstra, Bellman-Ford)
- Dynamic Programming (Knapsack, LCS, Fibonacci)
- Greedy algorithms
- String algorithms (KMP, Rabin-Karp)

**Testing:**
- Unit tests using pytest
- Performance benchmarks
- Comparison scripts

## 📚 Resources

### Learn More About DSA

- **Big-O Cheat Sheet:** [bigocheatsheet.com](https://www.bigocheatsheet.com/)
- **Visualizations:** [visualgo.net](https://visualgo.net/)
- **Practice Problems:** [leetcode.com](https://leetcode.com/), [hackerrank.com](https://www.hackerrank.com/)
- **Books:**
  - "Introduction to Algorithms" by CLRS
  - "Grokking Algorithms" by Aditya Bhargava
  - "Data Structures and Algorithms in Python" by Goodrich et al.

### Python Documentation

- [Python Official Docs](https://docs.python.org/3/)
- [Python collections module](https://docs.python.org/3/library/collections.html)
- [Python time complexity](https://wiki.python.org/moin/TimeComplexity)

## 📊 Repository Statistics

| Metric | Value |
|--------|-------|
| Total Python Files | 15 |
| Data Structures | 6 |
| Algorithms | 3 |
| Complexity Examples | 5 |
| Documentation Files | 2 |
| Total Lines of Code | ~1000+ |

## 📝 License

This project is open source and available for educational purposes.

## 💬 Feedback

Have questions or suggestions? Feel free to:
- Open an issue on GitHub
- Submit a pull request
- Reach out for discussions

---

**Happy Learning!** 🎉

Remember: Understanding these fundamentals is key to becoming a better programmer. Take your time, experiment with the code, and most importantly, have fun while learning!

---

*This repository is maintained with ❤️ for the programming community. Learn DSA with Kubomu!*
