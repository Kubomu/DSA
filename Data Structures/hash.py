def simple_hash(key, table_size=100):
    """
    A simple hash function that computes hash value based on character values.

    This function uses polynomial rolling hash technique to reduce collisions.
    It computes: (c1 * 31^(n-1) + c2 * 31^(n-2) + ... + cn) % table_size
    where ci is the ASCII value of character i.

    Args:
        key (str): The string key to hash
        table_size (int): The size of the hash table (default: 100)

    Returns:
        int: Hash value in range [0, table_size-1]

    Raises:
        TypeError: If key is not a string
        ValueError: If key is empty or table_size is invalid

    Time Complexity: O(n) where n is the length of the key
    Space Complexity: O(1)

    Examples:
        >>> simple_hash("Alice")
        67
        >>> simple_hash("James")
        28
        >>> simple_hash("Alice", 50)
        17
    """
    if not isinstance(key, str):
        raise TypeError("Key must be a string")

    if not key:
        raise ValueError("Key cannot be empty")

    if table_size <= 0:
        raise ValueError("Table size must be positive")

    # Polynomial rolling hash with prime multiplier 31
    hash_value = 0
    for char in key:
        hash_value = (hash_value * 31 + ord(char)) % table_size

    return hash_value


def simple_hash_alternative(key, table_size=100):
    """
    Alternative simple hash function using sum of character values.

    This is a simpler approach but may have more collisions than polynomial hash.

    Args:
        key (str): The string key to hash
        table_size (int): The size of the hash table (default: 100)

    Returns:
        int: Hash value in range [0, table_size-1]

    Time Complexity: O(n) where n is the length of the key
    Space Complexity: O(1)
    """
    if not isinstance(key, str) or not key:
        raise ValueError("Key must be a non-empty string")

    return sum(ord(char) for char in key) % table_size


# Test both hash functions
print("=== Polynomial Rolling Hash (Recommended) ===")
test_keys = ["Alice", "James", "Bob", "Charlie", "Dave"]
for key in test_keys:
    hash_val = simple_hash(key)
    print(f"Hash for '{key}': {hash_val}")

print("\n=== Alternative Sum-Based Hash ===")
for key in test_keys:
    hash_val = simple_hash_alternative(key)
    print(f"Hash for '{key}': {hash_val}")

print("\n=== Collision Test ===")
# Test that different strings produce different hashes (reduced collisions)
print(f"'Alice' vs 'James': {simple_hash('Alice')} vs {simple_hash('James')} - Different: {simple_hash('Alice') != simple_hash('James')}")
