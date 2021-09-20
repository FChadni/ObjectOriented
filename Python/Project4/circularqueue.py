"""
Project 4 - Circular Queues
Name: 
PID:
"""
from collections import defaultdict


class CircularQueue:
    """
    Circular Queue Class.
    """

    # DO NOT MODIFY THESE METHODS
    def __init__(self, capacity=4):
        """
        Initialize the queue with an initial capacity
        :param capacity: the initial capacity of the queue
        """
        self.capacity = capacity
        self.size = 0
        self.data = [None] * capacity
        self.head = 0
        self.tail = 0

    def __eq__(self, other):
        """
        Defines equality for two queues
        :return: true if two queues are equal, false otherwise
        """
        if self.capacity != other.capacity or self.size != other.size:
            return False

        if self.head != other.head or self.tail != other.tail:
            return False

        for i in range(self.capacity):
            if self.data[i] != other.data[i]:
                return False

        return True

    def __str__(self):
        """
        String representation of the queue
        :return: the queue as a string
        """
        if self.is_empty():
            return "Empty queue"

        str_list = [str(self.data[(self.head + i) % self.capacity]) for i in range(self.size)]
        return "Queue: " + ", ".join(str_list)

    # -----------MODIFY BELOW--------------

    def is_empty(self):
        """
        checking if is empty
        :return: Ture/False
        """
        if self.size == 0:
            return True
        return False

    def __len__(self):
        """
        getting the length of element
        :return: size of elements
        """
        return self.size

    def head_element(self):
        """
        getting the front element
        :return: head element
        """
        if self.size == 0:
            return None
        return self.data[self.head]

    def tail_element(self):
        """
        getting tail element
        :return: tail element
        """
        if self.size == 0:
            return None
        return self.data[self.tail-1]

    def grow(self):
        """
        Doubles the capacity of the queue immediately when capacity is reached to make room for new elements
        Moves the head to the front of the newly allocated list
        """
        if self.capacity == self.size:
            old = self.data
            self.capacity = self.capacity * 2
            self.data = [None] * self.capacity
            walk = self.head
            for k in range(self.size):
                self.data[k] = old[walk]
                walk = (1 + walk) % len(old)
            self.head = 0
            self.tail = self.size

    def shrink(self):
        """
        Halves the capacity of the queue immediately if the size is 1/4 or less of the capacity
        Capacity should never go below 4. This means that if halving the capacity would be less than 4, the queue should NOT be shrunk.
        Example: Queue capacity of 6, with 2 elements. If you dequeue an element, the capacity should stay 6. While 1/6 capacity is less than 1/4 capacity, the queue would be shrinking to 3 elements, which isn't allowed. In addition, the queue should stay at capacity 6, it shouldn't shrink to capacity of 4 since that is the threshold.
        Moves the head to the front of the newly allocated list
        """
        if self.size <= self.capacity // 4 and self.capacity // 2 >= 4:
            old = self.data
            self.capacity = self.capacity // 2
            self.data = [None] * self.capacity
            walk = self.head
            for k in range(self.size):
                self.data[k] = old[walk]
                walk = (1 + walk) % len(old)
            self.head = 0
            self.tail = self.size

    def enqueue(self, val):
        """
        Add an element val to the back of the queue
        :param val: value that to be enqeue
        :return: None
        """
        if self.is_empty():
            self.tail = 1
            self.data[self.head] = val
            self.size += 1
            return None
        ans1 = (self.head + self.size) % len(self.data)
        self.data[ans1] = val
        self.tail = ans1 + 1
        self.size += 1
        if self.size == len(self.data):
            self.grow()
        return None

    def dequeue(self):
        """
        Remove an element from the front of a queue. Calls shrink & shrinks queue immediately after a value is removed, if needed.
        :return: None
        """
        if self.is_empty():
            return None
        ans = self.data[self.head]
        self.data[self.head] = None
        self.head = (self.head + 1) % len(self.data)
        self.size -= 1
        if (self.size <= self.capacity // 4 and self.capacity // 2 >= 4):
            self.shrink()
        return ans

class QStack:
    """
    Stack class, implemented with underlying Circular Queue
    """
    # DO NOT MODIFY THESE METHODS
    def __init__(self):
        self.cq = CircularQueue()
        self.size = 0

    def __eq__(self, other):
        """
        Defines equality for two QStacks
        :return: true if two stacks are equal, false otherwise
        """
        if self.size != other.size:
            return False

        if self.cq != other.cq:
            return False

        return True

    def __str__(self):
        """
        String representation of the QStack
        :return: the stack as a string
        """
        if self.size == 0:
            return "Empty stack"

        str_list = [str(self.cq.data[(self.cq.head + i) % self.cq.capacity]) for i in range(self.size)]
        return "Stack: " + ", ".join(str_list)

    # -----------MODIFY BELOW--------------
    def push(self, val):
        """
        Adds an element, val, to the top of the stack.
        :param val: value to be pushed into stack
        :return: None
        """
        if self.cq.is_empty():
            self.cq.enqueue(val)
            self.size += 1
        else:
            self.cq.enqueue(val)
            self.size += 1
            for k in range(self.size - 1):
                dequ = self.cq.dequeue()
                self.cq.enqueue(dequ)
        return None

    def pop(self):
        """
        Removes an element from the top of the stack,
        :return: element popped
        """
        if self.cq.is_empty():
            return None
        self.size -= 1
        return self.cq.dequeue()

    def top(self):
        """
        Returns but DOES NOT remove the top element of the stack.
        :return: element peeked at
        """
        if self.cq.is_empty():
            return None
        return self.cq.head_element()

def digit_swap(nums, replacements):
    """
    String representation of the queue
    :param nums: the string of numbers to swap elements
    :param replacements: the number of swaps that you are permitted to make
    :return: max occurence after applying replacement
    """
    q = CircularQueue()
    numdict = defaultdict(int)
    len_occur = 0
    maximum_occur = 0
    for i in nums:
        q.enqueue(i)
        numdict[i] += 1
        len_occur = max(len_occur, numdict[i])
        if len(q) - len_occur > replacements:
            remo = q.dequeue()
            numdict[remo] -= 1
        maximum_occur = max(maximum_occur, len(q))
    return maximum_occur
