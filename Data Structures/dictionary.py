"""
Hash Map (Dictionary) implementation and operations in Python.

A dictionary is a data structure that stores key-value pairs and allows
fast lookups, insertions, and deletions based on the key.

Time Complexity (Average Case):
    - Insert: O(1)
    - Lookup: O(1)
    - Delete: O(1)

Time Complexity (Worst Case):
    - Insert: O(n) - when hash collisions occur
    - Lookup: O(n) - when hash collisions occur
    - Delete: O(n) - when hash collisions occur

Space Complexity: O(n) where n is the number of key-value pairs
"""


def demonstrate_dictionary_operations():
    """
    Demonstrate common dictionary operations with error handling.

    Shows insertion, retrieval, deletion, and safe access patterns.
    """
    # Creating a hash map (dictionary)
    hash_map = {}

    # Insert key-value pairs into the hash map
    # The key is the unique identifier, and the value is the associated data.
    hash_map["name"] = "Alice"  # Add a key-value pair: 'name' -> 'Alice'
    hash_map["age"] = 30        # Add a key-value pair: 'age' -> 30
    hash_map["city"] = "Gulu"   # Add a key-value pair: 'city' -> 'Gulu'

    print("Initial hash map:", hash_map)

    # Safe retrieval using get() method (returns None if key doesn't exist)
    name = hash_map.get("name")
    print("Name:", name)

    # Direct access (raises KeyError if key doesn't exist)
    try:
        city = hash_map["city"]
        print("City:", city)
    except KeyError as e:
        print(f"Key not found: {e}")

    # Check if key exists
    if "age" in hash_map:
        print("Age exists:", hash_map["age"])

    # Delete a key-value pair from the hash map
    del hash_map["age"]
    print("After deleting 'age':", hash_map)

    # Safe deletion
    hash_map.pop("nonexistent", None)  # Won't raise error

    # Iterating over dictionary
    print("\nIterating over keys and values:")
    for key, value in hash_map.items():
        print(f"  {key}: {value}")


def safe_dict_get(dictionary, key, default=None):
    """
    Safely retrieve a value from a dictionary.

    Args:
        dictionary (dict): The dictionary to access
        key: The key to look up
        default: Default value to return if key not found (default: None)

    Returns:
        The value associated with the key, or default if not found

    Raises:
        TypeError: If dictionary is not a dict
    """
    if not isinstance(dictionary, dict):
        raise TypeError("First argument must be a dictionary")

    return dictionary.get(key, default)


def safe_dict_set(dictionary, key, value):
    """
    Safely set a value in a dictionary with validation.

    Args:
        dictionary (dict): The dictionary to modify
        key: The key to set (must be hashable)
        value: The value to associate with the key

    Raises:
        TypeError: If dictionary is not a dict or key is not hashable
    """
    if not isinstance(dictionary, dict):
        raise TypeError("First argument must be a dictionary")

    try:
        dictionary[key] = value
    except TypeError:
        raise TypeError(f"Key must be hashable, got {type(key).__name__}")


# Demonstrate dictionary operations
if __name__ == "__main__":
    demonstrate_dictionary_operations()

    print("\n=== Safe Dictionary Operations ===")
    test_dict = {"x": 10, "y": 20}
    print("Value for 'x':", safe_dict_get(test_dict, "x"))
    print("Value for 'z' (not exists):", safe_dict_get(test_dict, "z", default="Not Found"))
