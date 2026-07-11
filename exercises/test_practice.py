"""
Autograder for practice.py.

You do not need to edit this file. It is what `python check.py`, `pytest`, and
the green check on GitHub all run to confirm your solutions are correct.
"""

import pytest

import practice as p


# 1. Recursion ---------------------------------------------------------------
def test_factorial():
    assert p.factorial(0) == 1
    assert p.factorial(1) == 1
    assert p.factorial(5) == 120
    assert p.factorial(6) == 720


# 2. Searching ---------------------------------------------------------------
def test_binary_search_finds_values():
    nums = [1, 3, 5, 7, 9]
    assert p.binary_search(nums, 1) == 0
    assert p.binary_search(nums, 7) == 3
    assert p.binary_search(nums, 9) == 4


def test_binary_search_missing_values():
    assert p.binary_search([1, 3, 5], 4) == -1
    assert p.binary_search([], 1) == -1


# 3. Sorting: bubble sort ----------------------------------------------------
def test_bubble_sort():
    assert p.bubble_sort([5, 1, 4, 2, 8]) == [1, 2, 4, 5, 8]
    assert p.bubble_sort([]) == []
    assert p.bubble_sort([3, 3, 1]) == [1, 3, 3]


def test_bubble_sort_does_not_mutate_input():
    original = [3, 2, 1]
    p.bubble_sort(original)
    assert original == [3, 2, 1]


# 4. Sorting: merge sort -----------------------------------------------------
def test_merge_sort():
    assert p.merge_sort([5, 1, 4, 2, 8]) == [1, 2, 4, 5, 8]
    assert p.merge_sort([]) == []
    assert p.merge_sort([9, -1, 0, 2, 2]) == [-1, 0, 2, 2, 9]


# 5. Stack -------------------------------------------------------------------
def test_stack():
    s = p.Stack()
    assert s.is_empty() is True
    s.push(10)
    s.push(20)
    assert len(s) == 2
    assert s.peek() == 20
    assert s.pop() == 20
    assert s.pop() == 10
    assert s.is_empty() is True


# 6. Queue -------------------------------------------------------------------
def test_queue():
    q = p.Queue()
    assert q.is_empty() is True
    q.enqueue(1)
    q.enqueue(2)
    assert len(q) == 2
    assert q.dequeue() == 1
    assert q.dequeue() == 2
    assert q.is_empty() is True
