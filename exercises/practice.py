"""
Practice exercises for the DSA repository.

HOW THIS WORKS
  1. Every function and class below has a `# TODO` and raises NotImplementedError.
  2. Replace each TODO with your own code so the behaviour matches the docstring.
  3. Check your work instantly. From the repo folder run either:
         python check.py     (friendly scoreboard, one line per topic)
         pytest              (full detail on what passed and failed)
  4. A topic turns green once its tests pass. Keep going until all six pass.

Each exercise mirrors a worked example already in this repository. If you get
stuck, open the matching file for a reference, then come back and try again.
You cannot break anything here, so experiment freely.
"""


# ---------------------------------------------------------------------------
# 1. Recursion                      (worked example: Recursion/factorial.py)
# ---------------------------------------------------------------------------
def factorial(n):
    """Return n! (n factorial) using recursion.

    factorial(0) is 1, and factorial(n) is n * factorial(n - 1).

    >>> factorial(0)
    1
    >>> factorial(5)
    120
    """
    # TODO: return 1 when n is 0, otherwise n * factorial(n - 1)
    raise NotImplementedError("Exercise 1: fill in factorial")


# ---------------------------------------------------------------------------
# 2. Searching       (worked example: Searching Algorithms/binary_search.py)
# ---------------------------------------------------------------------------
def binary_search(nums, target):
    """Return the index of target in the SORTED list nums, or -1 if missing.

    Binary search repeatedly halves the search range, so it is O(log n).

    >>> binary_search([1, 3, 5, 7, 9], 7)
    3
    >>> binary_search([1, 3, 5], 4)
    -1
    """
    # TODO: keep low/high pointers, compare nums[mid] to target, and narrow the
    #       range until you find target (return mid) or the range is empty (-1)
    raise NotImplementedError("Exercise 2: fill in binary_search")


# ---------------------------------------------------------------------------
# 3. Sorting             (worked example: Sorting Algorithms/bubble_sort.py)
# ---------------------------------------------------------------------------
def bubble_sort(nums):
    """Return a NEW list with the numbers sorted ascending, using bubble sort.

    Do not use Python's built-in sorted() or list.sort(); the goal is to write
    the algorithm yourself by repeatedly swapping neighbours that are in the
    wrong order.

    >>> bubble_sort([5, 1, 4, 2, 8])
    [1, 2, 4, 5, 8]
    """
    # TODO: copy nums, then repeatedly pass through it swapping any pair where
    #       the left value is greater than the right, until no swaps are needed
    raise NotImplementedError("Exercise 3: fill in bubble_sort")


# ---------------------------------------------------------------------------
# 4. Sorting              (worked example: Sorting Algorithms/merge_sort.py)
# ---------------------------------------------------------------------------
def merge_sort(nums):
    """Return a NEW sorted list using merge sort (divide and conquer).

    Split the list in half, sort each half, then merge the two sorted halves
    back together. This runs in O(n log n).

    >>> merge_sort([5, 1, 4, 2, 8])
    [1, 2, 4, 5, 8]
    """
    # TODO: base case is a list of length 0 or 1 (already sorted). Otherwise
    #       split in two, merge_sort each half, and merge them in order.
    raise NotImplementedError("Exercise 4: fill in merge_sort")


# ---------------------------------------------------------------------------
# 5. Data structure                 (worked example: Data Structures/stacks.py)
# ---------------------------------------------------------------------------
class Stack:
    """A last-in, first-out (LIFO) stack. The most recently pushed item is the
    first one popped.

    >>> s = Stack()
    >>> s.push(10)
    >>> s.push(20)
    >>> s.peek()
    20
    >>> s.pop()
    20
    >>> len(s)
    1
    """

    def __init__(self):
        self._items = []

    def push(self, item):
        # TODO: add item to the top of the stack
        raise NotImplementedError("Exercise 5: fill in Stack.push")

    def pop(self):
        # TODO: remove and return the top item
        raise NotImplementedError("Exercise 5: fill in Stack.pop")

    def peek(self):
        # TODO: return the top item without removing it
        raise NotImplementedError("Exercise 5: fill in Stack.peek")

    def is_empty(self):
        # TODO: return True when the stack has no items
        raise NotImplementedError("Exercise 5: fill in Stack.is_empty")

    def __len__(self):
        # TODO: return how many items are in the stack
        raise NotImplementedError("Exercise 5: fill in Stack.__len__")


# ---------------------------------------------------------------------------
# 6. Data structure                  (worked example: Data Structures/queue.py)
# ---------------------------------------------------------------------------
class Queue:
    """A first-in, first-out (FIFO) queue. The first item enqueued is the first
    one dequeued.

    >>> q = Queue()
    >>> q.enqueue(1)
    >>> q.enqueue(2)
    >>> q.dequeue()
    1
    >>> len(q)
    1
    """

    def __init__(self):
        self._items = []

    def enqueue(self, item):
        # TODO: add item to the back of the queue
        raise NotImplementedError("Exercise 6: fill in Queue.enqueue")

    def dequeue(self):
        # TODO: remove and return the item at the front
        raise NotImplementedError("Exercise 6: fill in Queue.dequeue")

    def is_empty(self):
        # TODO: return True when the queue has no items
        raise NotImplementedError("Exercise 6: fill in Queue.is_empty")

    def __len__(self):
        # TODO: return how many items are in the queue
        raise NotImplementedError("Exercise 6: fill in Queue.__len__")
