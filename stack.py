""" 
Implementations of Stack 
A stack is a fundamental data structure that follows the Last-In/First-Out (LIFO) principle.
The time complexity of stack operations (push, pop, peek) is generally O(1), 
which means they execute in constant time regardless of the stack’s size.

Using dequeue the stack has a O(1) complexity because it uses a linkedin list structure 
rather than a dynamic list like list1 = [1,2,3] and doing list1.pop(0)
which makes the complexity of list1 O(n)
"""

class Stack:
    """
    A simple implementation of a stack data structure.

    """

    def __init__(self):
        """
        Initializes an empty stack.
        """
        self.items = []

    def push(self, item):
        """
        Pushes an item onto the top of the stack.
        Args:
            item: The item to be pushed.
        """
        self.items.append(item)

    def is_empty(self):
        """
        Checks if the stack is empty.
        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return len(self.items) == 0

    def pop(self):
        """
        Removes and returns the top item from the stack.
        Returns:
            Any: The popped item, or a message indicating that the stack is empty.
        """
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Stack is empty"

    def peek(self):
        """
        Returns the top item from the stack without removing it.
        Returns:
            Any: The top item, or a message indicating that the stack is empty.
        """
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Stack is empty"

# Example Usage:
my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
print("Popped item:", my_stack.pop())
print("Top element of the stack:", my_stack.peek())
my_stack.push(4)
print("Stack after popping an element:", my_stack.items)

print("")

from collections import deque

class EfficientStack:
    """
    A simple stack implementation using Python's deque.
    """

    def __init__(self):
        """
        Initializes an empty stack.
        """
        self.items = deque()

    def push(self, item):
        """
        Pushes an item onto the top of the stack.
        Args:
            item: The item to be pushed.
        """
        self.items.append(item)

    def pop(self):
        """
        Removes and returns the top item from the stack.
        Returns:
            Any: The popped item, or a message indicating that the stack is empty.
        """
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Stack is empty"

    def is_empty(self):
        """
        Checks if the stack is empty.
        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return len(self.items) == 0

    def peek(self):
        """
        Returns the top item from the stack without removing it.
        Returns:
            Any: The top item, or a message indicating that the stack is empty.
        """
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Stack is empty"

# Example usage:
my_stack = EfficientStack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
print("Popped item:", my_stack.pop())
print("Top element of the stack:", my_stack.peek())
my_stack.push(4)
print("Stack after popping an element:", my_stack.items)
