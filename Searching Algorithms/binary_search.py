def binary_search(arr, target):
    """
    Perform binary search on a sorted array.

    Binary search is an efficient algorithm for finding an element in a sorted array.
    It works by repeatedly dividing the search interval in half.

    Args:
        arr (list): A sorted array to search in (must be sorted in ascending order)
        target: The element to search for

    Returns:
        int: Index of the target element if found, -1 otherwise

    Raises:
        TypeError: If arr is not a list
        ValueError: If arr is empty

    Time Complexity: O(log n) - halves the search space each iteration
    Space Complexity: O(1) - uses constant extra space

    Examples:
        >>> binary_search([2, 3, 4, 10, 40], 10)
        3
        >>> binary_search([1, 2, 3, 4, 5], 6)
        -1
        >>> binary_search([1, 2, 3, 4, 5], 1)
        0

    Note:
        The array MUST be sorted in ascending order for binary search to work correctly.
        If the array is not sorted, the result will be incorrect.
    """
    if not isinstance(arr, list):
        raise TypeError("Array must be a list")

    if not arr:
        raise ValueError("Cannot search in an empty array")

    low = 0  # Set the low index to 0, which is the start of the array
    high = len(arr) - 1  # Set the high index to the last element in the array

    while low <= high:  # Continue as long as the low index is less than or equal to the high index
        # Use low + (high - low) // 2 to avoid potential integer overflow
        # This is safer than (low + high) // 2 for very large arrays
        mid = low + (high - low) // 2

        try:
            if arr[mid] == target:  # If the middle element is equal to the target, return the index
                return mid
            elif arr[mid] < target:  # If the middle element is less than the target, discard the left half
                low = mid + 1  # Move the low index to mid + 1
            else:  # If the middle element is greater than the target, discard the right half
                high = mid - 1  # Move the high index to mid - 1
        except TypeError as e:
            raise ValueError(f"Array contains non-comparable elements or target is not comparable: {e}")

    return -1  # Return -1 if the target is not found in the array


# Test
if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40]  # Sorted array
    print("Array:", arr)

    # Test finding existing element
    target = 10
    result = binary_search(arr, target)
    print(f"Searching for {target}: Element found at index {result}" if result != -1 else f"Searching for {target}: Element not found")

    # Test finding element at beginning
    target = 2
    result = binary_search(arr, target)
    print(f"Searching for {target}: Element found at index {result}" if result != -1 else f"Searching for {target}: Element not found")

    # Test finding element at end
    target = 40
    result = binary_search(arr, target)
    print(f"Searching for {target}: Element found at index {result}" if result != -1 else f"Searching for {target}: Element not found")

    # Test finding non-existent element
    target = 100
    result = binary_search(arr, target)
    print(f"Searching for {target}: Element found at index {result}" if result != -1 else f"Searching for {target}: Element not found")
