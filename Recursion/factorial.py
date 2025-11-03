def factorial(n):
    """
    Calculate the factorial of a non-negative integer using recursion.

    The factorial of n (denoted as n!) is the product of all positive integers
    less than or equal to n. By definition, 0! = 1.

    Formula: n! = n × (n-1) × (n-2) × ... × 2 × 1

    Args:
        n (int): A non-negative integer

    Returns:
        int: The factorial of n

    Raises:
        TypeError: If n is not an integer
        ValueError: If n is negative

    Time Complexity: O(n) - makes n recursive calls
    Space Complexity: O(n) - uses n stack frames

    Examples:
        >>> factorial(0)
        1
        >>> factorial(5)
        120
        >>> factorial(10)
        3628800

    Note:
        For large values of n, this may cause a stack overflow due to deep recursion.
        Consider using an iterative approach or increasing the recursion limit for very large values.
    """
    # Input validation
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")

    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")

    # Base case: If n is 0 or 1, return 1
    # factorial of 0 is defined as 1, and factorial of 1 is also 1
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive case: n * factorial of (n-1)
        # This calls the function itself with a smaller value, reducing the problem size
        return n * factorial(n - 1)


def factorial_iterative(n):
    """
    Calculate the factorial using an iterative approach (more efficient).

    This version avoids recursion depth issues and is generally faster.

    Args:
        n (int): A non-negative integer

    Returns:
        int: The factorial of n

    Time Complexity: O(n)
    Space Complexity: O(1) - constant space
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")

    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


# Test the factorial function
if __name__ == "__main__":
    print("=== Recursive Factorial ===")
    test_values = [0, 1, 5, 10]

    for val in test_values:
        result = factorial(val)
        print(f"factorial({val}) = {result}")

    print("\n=== Iterative Factorial (More Efficient) ===")
    for val in test_values:
        result = factorial_iterative(val)
        print(f"factorial_iterative({val}) = {result}")

    # Demonstrate error handling
    print("\n=== Error Handling ===")
    try:
        factorial(-5)
    except ValueError as e:
        print(f"Error with negative input: {e}")

    try:
        factorial(3.14)
    except TypeError as e:
        print(f"Error with float input: {e}")
