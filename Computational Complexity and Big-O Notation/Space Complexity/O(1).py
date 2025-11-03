"""
Demonstration of O(1) - Constant Space Complexity.

An algorithm has constant space complexity when the amount of extra memory
it uses does not depend on the size of the input. It uses the same amount
of memory regardless of input size.
"""


def sum_array(arr):
    """
    Calculate the sum of all elements in an array.

    This function has O(1) space complexity because it only uses a single
    variable (total) to store the sum, regardless of how large the input array is.

    Args:
        arr (list): Array of numbers

    Returns:
        The sum of all elements

    Raises:
        TypeError: If arr is not a list

    Time Complexity: O(n) - must visit each element
    Space Complexity: O(1) - uses only one variable (constant space)

    Examples:
        >>> sum_array([1, 2, 3, 4, 5])
        15
        >>> sum_array([10, 20, 30])
        60
    """
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")

    # Initialize a variable to keep track of the sum
    # This uses constant space (O(1)) - only one variable regardless of array size
    total = 0

    # Loop through each number in the array
    for num in arr:
        total += num  # Add each element to the total sum

    return total  # Return the total sum of the array


def find_max(arr):
    """
    Find the maximum element in an array.

    Another example of O(1) space complexity - uses only one variable
    to track the maximum value.

    Args:
        arr (list): Array of comparable elements

    Returns:
        The maximum element

    Space Complexity: O(1)
    """
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")

    if not arr:
        raise ValueError("Cannot find max of empty array")

    max_val = arr[0]  # Only one extra variable - O(1) space
    for element in arr[1:]:
        if element > max_val:
            max_val = element
    return max_val


def swap_first_last(arr):
    """
    Swap first and last elements in-place.

    Args:
        arr (list): The array to modify

    Space Complexity: O(1) - only uses a temp variable
    """
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")

    if len(arr) < 2:
        return arr

    # Swap using Python's tuple unpacking - still O(1) space
    arr[0], arr[-1] = arr[-1], arr[0]
    return arr


# Test case
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print("Array:", arr)
    print("Sum of the array:", sum_array(arr))  # Output: 15
    print("Maximum element:", find_max(arr))  # Output: 5

    print("\n=== Space Complexity Demo ===")
    print("For an array of 5 elements, we use 1 variable")
    large_arr = list(range(1, 1000001))  # 1 million elements
    print("For an array of 1 million elements, we still use 1 variable!")
    print("Sum of large array:", sum_array(large_arr))

    print("\n=== In-place Modification (O(1) space) ===")
    test_arr = [1, 2, 3, 4, 5]
    print("Before swap:", test_arr)
    swap_first_last(test_arr)
    print("After swap:", test_arr)
