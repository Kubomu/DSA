def merge_sort(arr):
    """
    Sort an array using the Merge Sort algorithm.

    Merge Sort is a divide-and-conquer algorithm that divides the input array
    into two halves, recursively sorts them, and then merges the sorted halves.

    Args:
        arr (list): The array to sort (modified in-place)

    Returns:
        list: The sorted array

    Raises:
        TypeError: If arr is not a list
        ValueError: If array contains non-comparable elements

    Time Complexity: O(n log n) - divides array log(n) times and merges in O(n)
    Space Complexity: O(n) - requires additional space for temporary arrays

    Examples:
        >>> merge_sort([38, 27, 43, 3, 9, 82, 10])
        [3, 9, 10, 27, 38, 43, 82]
        >>> merge_sort([5, 2, 8, 1, 9])
        [1, 2, 5, 8, 9]
    """
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")

    if len(arr) > 1:  # Only proceed if the array has more than 1 element
        mid = len(arr) // 2  # Find the middle index of the array
        left_half = arr[:mid]  # Split the array into the left half
        right_half = arr[mid:]  # Split the array into the right half

        merge_sort(left_half)  # Recursively sort the left half
        merge_sort(right_half)  # Recursively sort the right half

        i = j = k = 0  # Initialize indices for left_half, right_half, and arr

        # Merge the sorted left and right halves
        try:
            while i < len(left_half) and j < len(right_half):  # Compare elements in both halves
                if left_half[i] < right_half[j]:  # If element in left_half is smaller
                    arr[k] = left_half[i]  # Place it in the correct position of the original array
                    i += 1  # Move to the next element in left_half
                else:  # If element in right_half is smaller
                    arr[k] = right_half[j]  # Place it in the correct position of the original array
                    j += 1  # Move to the next element in right_half
                k += 1  # Move to the next position in the original array
        except TypeError as e:
            raise ValueError(f"Array contains non-comparable elements: {e}")

        # If there are remaining elements in left_half, add them to arr
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # If there are remaining elements in right_half, add them to arr
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr  # Return the sorted array


# Test
if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10]
    print("Original array:", arr.copy())
    print("Sorted array:", merge_sort(arr))

    # Test with different arrays
    arr2 = [5, 2, 8, 1, 9]
    print("\nTest 2:", merge_sort(arr2))

    # Test with already sorted array
    arr3 = [1, 2, 3, 4, 5]
    print("Already sorted:", merge_sort(arr3))

    # Test with empty and single element
    print("Empty array:", merge_sort([]))
    print("Single element:", merge_sort([42]))
