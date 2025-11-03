class Stack:
    """
    A Stack implementation using Python list.

    Stack follows LIFO (Last In First Out) principle where the last element
    added is the first one to be removed.

    Time Complexity:
        - push: O(1)
        - pop: O(1)
        - peek: O(1)
        - is_empty: O(1)

    Space Complexity: O(n) where n is the number of elements in the stack
    """

    def __init__(self):
        """Initialize an empty stack."""
        self.stack = []

    def push(self, data):
        """
        Add an element to the top of the stack.

        Args:
            data: The element to add to the stack

        Time Complexity: O(1)
        """
        self.stack.append(data)

    def pop(self):
        """
        Remove and return the top element from the stack.

        Returns:
            The top element of the stack

        Raises:
            IndexError: If the stack is empty

        Time Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("Cannot pop from an empty stack!")
        return self.stack.pop()

    def peek(self):
        """
        Return the top element without removing it from the stack.

        Returns:
            The top element of the stack

        Raises:
            IndexError: If the stack is empty

        Time Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("Cannot peek at an empty stack!")
        return self.stack[-1]

    def is_empty(self):
        """
        Check if the stack is empty.

        Returns:
            bool: True if stack is empty, False otherwise

        Time Complexity: O(1)
        """
        return len(self.stack) == 0

# Test the Stack class
stack = Stack()  # Create a new stack instance
stack.push(10)  # Push 10 onto the stack
stack.push(20)  # Push 20 onto the stack
stack.push(30)  # Push 30 onto the stack

# Peek to see the top element of the stack
print("Top element:", stack.peek())  # Output: 30

# Pop the top element from the stack
print("Popped element:", stack.pop())  # Output: 30

# Print the stack after popping an element
print("Stack after pop:", stack.stack)  # Output: [10, 20]
