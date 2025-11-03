"""
Demonstration of O(1) - Constant Time Complexity.

An algorithm has constant time complexity when its execution time does not
depend on the size of the input. It always takes the same amount of time.
"""


def get_first_element(arr):
    """
    Get the first element of an array.

    This operation has O(1) time complexity because accessing an element
    by index in a list is a constant-time operation, regardless of array size.

    Args:
        arr (list): The input array

    Returns:
        The first element of the array

    Raises:
        TypeError: If arr is not a list
        IndexError: If arr is empty

    Time Complexity: O(1) - constant time
    Space Complexity: O(1) - constant space

    Examples:
        >>> get_first_element([10, 20, 30, 40, 50])
        10
        >>> get_first_element([1])
        1
    """
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")

    if not arr:
        raise IndexError("Cannot get first element of an empty array")

    # The function accesses the first element of the list (array) by index 0.
    # This operation always takes constant time, O(1), regardless of the size of the array.
    return arr[0]


def get_element_at_index(arr, index):
    """
    Get element at a specific index (also O(1)).

    Args:
        arr (list): The input array
        index (int): The index to access

    Returns:
        The element at the given index

    Time Complexity: O(1)
    """
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")

    if not isinstance(index, int):
        raise TypeError("Index must be an integer")

    if not arr:
        raise IndexError("Cannot access element from empty array")

    if index < 0 or index >= len(arr):
        raise IndexError(f"Index {index} out of range for array of length {len(arr)}")

    return arr[index]


# Test case
if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]
    print("Array:", arr)
    print("First element:", get_first_element(arr))  # Output: 10
    print("Element at index 2:", get_element_at_index(arr, 2))  # Output: 30

    # Demonstrate that it's O(1) regardless of array size
    large_arr = list(range(1000000))  # 1 million elements
    print("\nLarge array (1 million elements)")
    print("First element:", get_first_element(large_arr))  # Still O(1)!
