"""
Array basics and operations in Python.

Arrays (lists in Python) are ordered, mutable collections that can store
multiple elements of different types.

Time Complexity:
    - Access by index: O(1)
    - Append: O(1) amortized
    - Insert at beginning: O(n)
    - Delete: O(n)

Space Complexity: O(n) where n is the number of elements
"""


def demonstrate_array_operations():
    """
    Demonstrate basic array operations in Python.

    Shows initialization, access, modification, and common operations.
    """
    # Initializing a list with values 1 through 5
    arr = [1, 2, 3, 4, 5]
    print("Array:", arr)

    # Accessing the first element of the list (O(1) operation)
    try:
        first_element = arr[0]
        print("First element:", first_element)
    except IndexError:
        print("Error: Cannot access element from empty array")

    # Accessing the last element
    if arr:
        print("Last element:", arr[-1])

    # Adding an element (O(1) amortized)
    arr.append(6)
    print("After append(6):", arr)

    # Inserting at a specific position (O(n))
    arr.insert(0, 0)
    print("After insert(0, 0):", arr)

    # Removing an element (O(n))
    arr.remove(3)
    print("After remove(3):", arr)

    # Array length
    print("Array length:", len(arr))


def safe_array_access(arr, index):
    """
    Safely access an array element with error handling.

    Args:
        arr (list): The array to access
        index (int): The index to access

    Returns:
        The element at the given index, or None if index is invalid

    Raises:
        TypeError: If arr is not a list or index is not an integer
    """
    if not isinstance(arr, list):
        raise TypeError("First argument must be a list")

    if not isinstance(index, int):
        raise TypeError("Index must be an integer")

    if not arr:
        raise ValueError("Cannot access element from empty array")

    if index < 0 or index >= len(arr):
        raise IndexError(f"Index {index} out of range for array of length {len(arr)}")

    return arr[index]


# Demonstrate array operations
if __name__ == "__main__":
    demonstrate_array_operations()

    print("\n=== Safe Array Access ===")
    test_arr = [10, 20, 30, 40, 50]
    print("Array:", test_arr)
    print("Element at index 2:", safe_array_access(test_arr, 2))
