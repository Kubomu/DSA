"""
Demonstration of O(n²) - Quadratic Time Complexity.

An algorithm has quadratic time complexity when its execution time grows
proportionally to the square of the input size. This often occurs with
nested loops where each loop iterates over the input.

If you double the input size, the execution time roughly quadruples.
"""


def print_pairs(arr):
    """
    Print all pairs of elements from an array.

    This operation has O(n²) time complexity because it uses nested loops,
    each iterating n times, resulting in n × n = n² iterations.

    Args:
        arr (list): The input array

    Time Complexity: O(n²) - nested loops each running n times
    Space Complexity: O(1) - uses constant extra space

    Note:
        - For 3 elements: 3 × 3 = 9 pairs
        - For 10 elements: 10 × 10 = 100 pairs
        - For 100 elements: 100 × 100 = 10,000 pairs
    """
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")

    # Outer loop iterates through each element of the array (n times)
    for i in range(len(arr)):
        # Inner loop iterates through each element of the array again (n times)
        # Total iterations: n × n = n²
        for j in range(len(arr)):
            print(arr[i], arr[j])  # Print the pair of elements (arr[i], arr[j])


def has_duplicates(arr):
    """
    Check if array has duplicates using nested loops.

    This is a naive O(n²) approach. Better approaches exist using sets (O(n)).

    Args:
        arr (list): The array to check

    Returns:
        bool: True if duplicates exist, False otherwise

    Time Complexity: O(n²) - checks each pair of elements
    """
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")

    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):  # Start from i+1 to avoid comparing element with itself
            if arr[i] == arr[j]:
                return True
    return False


def count_pairs_with_sum(arr, target_sum):
    """
    Count pairs of elements that sum to target.

    Args:
        arr (list): Array of numbers
        target_sum: The target sum to find

    Returns:
        int: Number of pairs that sum to target

    Time Complexity: O(n²)
    """
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")

    count = 0
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target_sum:
                count += 1
                print(f"Pair found: {arr[i]} + {arr[j]} = {target_sum}")
    return count


# Test case
if __name__ == "__main__":
    arr = [1, 2, 3]
    print("Array:", arr)
    print("\n=== Printing all pairs (O(n²)) ===")
    print_pairs(arr)
    print(f"\nTotal pairs: {len(arr) * len(arr)}")

    print("\n=== Checking for duplicates (O(n²)) ===")
    arr_with_dups = [1, 2, 3, 2, 4]
    print(f"Array: {arr_with_dups}")
    print(f"Has duplicates: {has_duplicates(arr_with_dups)}")

    print("\n=== Finding pairs with sum (O(n²)) ===")
    arr_nums = [1, 2, 3, 4, 5]
    target = 7
    print(f"Array: {arr_nums}, Target sum: {target}")
    count = count_pairs_with_sum(arr_nums, target)
    print(f"Total pairs with sum {target}: {count}")
