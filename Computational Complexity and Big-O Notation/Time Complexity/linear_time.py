"""
Demonstration of O(n) - Linear Time Complexity.

An algorithm has linear time complexity when its execution time grows
linearly with the size of the input. If you double the input size,
the execution time also roughly doubles.
"""


def print_all_elements(arr):
    """
    Print all elements of an array.

    This operation has O(n) time complexity because it must visit each
    element exactly once, where n is the number of elements.

    Args:
        arr (list): The input array

    Time Complexity: O(n) - must visit each element
    Space Complexity: O(1) - uses constant extra space

    Note:
        If the array has 10 elements, this runs 10 times.
        If the array has 1000 elements, this runs 1000 times.
    """
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")

    # Loop through each element in the array
    # The loop will run once for each element, so it takes O(n) time,
    # where n is the number of elements in the array.
    for element in arr:
        print(element)  # Print the current element


def find_element(arr, target):
    """
    Find an element in an array (linear search).

    This is another example of O(n) time complexity because in the worst case,
    we may need to check every element.

    Args:
        arr (list): The array to search
        target: The element to find

    Returns:
        int: Index of element if found, -1 otherwise

    Time Complexity: O(n) - worst case checks all n elements
    """
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")

    for i, element in enumerate(arr):
        if element == target:
            return i
    return -1


def sum_array(arr):
    """
    Calculate sum of all elements.

    Args:
        arr (list): Array of numbers

    Returns:
        The sum of all elements

    Time Complexity: O(n)
    """
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")

    total = 0
    for num in arr:
        total += num
    return total


# Test case
if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]
    print("Array:", arr)
    print("\n=== Printing all elements (O(n)) ===")
    print_all_elements(arr)

    print("\n=== Finding element (O(n)) ===")
    target = 30
    index = find_element(arr, target)
    print(f"Element {target} found at index: {index}")

    print("\n=== Sum of array (O(n)) ===")
    print(f"Sum: {sum_array(arr)}")
