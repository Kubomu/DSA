"""
Demonstration of O(n) - Linear Space Complexity.

An algorithm has linear space complexity when the amount of extra memory
it uses grows linearly with the size of the input. If you double the input
size, the memory usage also roughly doubles.
"""


def create_copy(arr):
    """
    Create a copy of the given array.

    This function has O(n) space complexity because it creates a new array
    of the same size as the input. The space needed grows proportionally
    with the input size.

    Args:
        arr (list): The array to copy

    Returns:
        list: A new array that is a copy of the input

    Raises:
        TypeError: If arr is not a list

    Time Complexity: O(n) - must copy each element
    Space Complexity: O(n) - creates new array of size n

    Examples:
        >>> create_copy([1, 2, 3, 4, 5])
        [1, 2, 3, 4, 5]
        >>> create_copy([])
        []

    Note:
        - For 10 elements: uses 10 units of extra space
        - For 1000 elements: uses 1000 units of extra space
    """
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")

    # Creates a shallow copy of the array using slicing
    # The space needed grows with the size of the input array - O(n) space
    copy = arr[:]
    return copy  # Returns the newly created copy of the array


def reverse_array(arr):
    """
    Create a reversed copy of an array.

    Args:
        arr (list): The array to reverse

    Returns:
        list: A new array with elements in reverse order

    Space Complexity: O(n) - creates new array of size n
    """
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")

    # Creates a new array - O(n) space
    reversed_arr = []
    for element in arr:
        reversed_arr.insert(0, element)
    return reversed_arr


def filter_even_numbers(arr):
    """
    Create a new array containing only even numbers.

    Args:
        arr (list): Array of integers

    Returns:
        list: New array with only even numbers

    Space Complexity: O(n) - in worst case, all elements could be even
    """
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")

    # Creates a new array - O(n) space in worst case
    evens = []
    for num in arr:
        if num % 2 == 0:
            evens.append(num)
    return evens


def create_frequency_map(arr):
    """
    Create a dictionary mapping elements to their frequencies.

    Args:
        arr (list): The input array

    Returns:
        dict: Dictionary with element frequencies

    Space Complexity: O(n) - dictionary can have up to n unique elements
    """
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")

    # Dictionary grows with number of unique elements - O(n) space
    freq_map = {}
    for element in arr:
        freq_map[element] = freq_map.get(element, 0) + 1
    return freq_map


# Test case
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print("Original array:", arr)
    print("Copy of the array:", create_copy(arr))

    print("\n=== Reversed Array (O(n) space) ===")
    print("Reversed:", reverse_array(arr))

    print("\n=== Filtered Array (O(n) space) ===")
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Original:", numbers)
    print("Even numbers:", filter_even_numbers(numbers))

    print("\n=== Frequency Map (O(n) space) ===")
    arr_with_dups = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    print("Array:", arr_with_dups)
    print("Frequencies:", create_frequency_map(arr_with_dups))

    print("\n=== Space Complexity Demo ===")
    print("For an array of 5 elements, we create a new array of 5 elements")
    large_arr = list(range(1000))
    copy_large = create_copy(large_arr)
    print(f"For an array of {len(large_arr)} elements, we create a new array of {len(copy_large)} elements")
