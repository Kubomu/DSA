def bubble_sort(arr):
    """
    Sort an array using the Bubble Sort algorithm.

    Bubble Sort repeatedly steps through the list, compares adjacent elements,
    and swaps them if they're in the wrong order. This process is repeated
    until the list is sorted.

    Args:
        arr (list): The array to sort (modified in-place)

    Returns:
        list: The sorted array

    Raises:
        TypeError: If arr is not a list
        ValueError: If array contains non-comparable elements

    Time Complexity: O(n^2) - due to nested loops
    Space Complexity: O(1) - sorts in-place

    Examples:
        >>> bubble_sort([64, 34, 25, 12, 22, 11, 90])
        [11, 12, 22, 25, 34, 64, 90]
        >>> bubble_sort([5, 2, 8, 1, 9])
        [1, 2, 5, 8, 9]
    """
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")

    if not arr:  # Empty array is already sorted
        return arr

    n = len(arr)  # Get the length of the array

    # Outer loop for n iterations (n elements in the array)
    for i in range(n):
        swapped = False  # Optimization: track if any swaps occurred

        # Inner loop to perform the comparisons and swap elements
        # After each pass, the largest element will be at the end of the array
        for j in range(0, n-i-1):
            try:
                if arr[j] > arr[j+1]:  # If the current element is greater than the next
                    arr[j], arr[j+1] = arr[j+1], arr[j]  # Swap the elements
                    swapped = True
            except TypeError as e:
                raise ValueError(f"Array contains non-comparable elements: {e}")

        # If no swaps occurred, array is already sorted
        if not swapped:
            break

    return arr  # Return the sorted array


# Test
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", arr)
    print("Sorted array:", bubble_sort(arr.copy()))

    # Test with already sorted array
    sorted_arr = [1, 2, 3, 4, 5]
    print("\nAlready sorted:", bubble_sort(sorted_arr.copy()))

    # Test with empty array
    print("Empty array:", bubble_sort([]))
