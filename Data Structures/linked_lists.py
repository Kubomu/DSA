class Node:
    """
    A node in a singly linked list.

    Attributes:
        data: The value stored in the node
        next: Reference to the next node in the list (None if it's the last node)
    """

    def __init__(self, data):
        """
        Initialize a new node.

        Args:
            data: The value to store in the node
        """
        self.data = data  # Stores the data of the node
        self.next = None  # Points to the next node in the list, initially set to None


class LinkedList:
    """
    A singly linked list implementation.

    A linked list is a linear data structure where elements are stored in nodes,
    and each node points to the next node in the sequence.

    Time Complexity:
        - append: O(n) - must traverse to the end
        - print_list: O(n) - must visit each node

    Space Complexity: O(n) where n is the number of nodes
    """

    def __init__(self):
        """Initialize an empty linked list."""
        self.head = None  # The head of the list is initially None, indicating an empty list

    def append(self, data):
        """
        Add a new node with the given data to the end of the list.

        Args:
            data: The value to append to the list

        Time Complexity: O(n) where n is the number of nodes
        """
        # Create a new node with the provided data
        new_node = Node(data)

        # If the list is empty (i.e., head is None), set the new node as the head
        if not self.head:
            self.head = new_node
            return

        # Otherwise, traverse the list to find the last node
        last = self.head
        while last.next:  # Loop until the last node (which has no 'next')
            last = last.next  # Move to the next node

        # Set the next pointer of the last node to the new node
        last.next = new_node

    def print_list(self):
        """
        Print all elements in the linked list in order.

        Prints elements in the format: data1 -> data2 -> data3 -> None

        Time Complexity: O(n) where n is the number of nodes
        """
        # Start from the head of the list
        temp = self.head

        # Handle empty list
        if not temp:
            print("Empty list")
            return

        # Traverse the list and print the data of each node
        while temp:
            print(temp.data, end=" -> ")  # Print the current node's data followed by an arrow
            temp = temp.next  # Move to the next node

        # After the list traversal, print "None" to indicate the end of the list
        print("None")

# Test the LinkedList implementation
ll = LinkedList()  # Create a new linked list
ll.append(1)  # Append a node with data 1 to the list
ll.append(2)  # Append a node with data 2 to the list
ll.append(3)  # Append a node with data 3 to the list

# Print the entire linked list
ll.print_list()  # Expected Output: 1 -> 2 -> 3 -> None
