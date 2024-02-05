""" 
Implementations of Queue 
A queue is a fundamental data structure that follows the First-In/First-Out (FIFO) principle.
Queue operations (enqueue, dequeue) have a time complexity of O(1) when using a deque (double-ended queue), 
ensuring efficient performance for adding and removing elements from the front and rear of the queue. 

Using dequeue the queue has a  O(1) complexity because it uses a linkedin list structure 
rather than a dynamic list like list1 = [1,2,3] and doing list1.pop()
which makes the complexity of list1 O(n)
"""
# file name QQueue.py on purpose VScode prompts an error if queue.py 

class Queue:
    """
    A simple queue implementation using a Python list.
    """

    def __init__(self):
        """
        Initializes an empty queue.
        """
        self.queue = []

    def enqueue(self, item):
        """
        Adds an item to the end of the queue (enqueue operation).
        Args:
            item: The item to be enqueued.
        """
        self.queue.append(item)

    def dequeue(self):
        """
        Removes and returns the front item from the queue (dequeue operation).
        Returns:
            Any: The dequeued item, or None if the queue is empty.
        """
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

# Example usage:
my_queue = Queue()
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)

print("Dequeued item:", my_queue.dequeue())
print("Queue after dequeuing an element:", my_queue.queue)
my_queue.enqueue(4)
print("Queue after enqueuing an element:", my_queue.queue)

print("")

from collections import deque

class EfficientQueue:
    """
    A more efficient queue implementation using Python's deque.
    """

    def __init__(self):
        """
        Initializes an empty queue.
        """
        self.queue = deque()

    def enqueue(self, item):
        """
        Adds an item to the end of the queue (enqueue operation).
        Args:
            item: The item to be enqueued.
        """
        self.queue.append(item)

    def dequeue(self):
        """
        Removes and returns the front item from the queue (dequeue operation).
        Returns:
            Any: The dequeued item, or None if the queue is empty.
        """
        if len(self.queue) < 1:
            return None
        return self.queue.popleft()

# Example usage:
efficient_queue = EfficientQueue()
efficient_queue.enqueue(1)
efficient_queue.enqueue(2)
efficient_queue.enqueue(3)

print("Dequeued item:", efficient_queue.dequeue())
print("Queue after dequeuing an element:", my_queue.queue)
my_queue.enqueue(4)
print("Queue after dequeuing an element:", efficient_queue.queue)
