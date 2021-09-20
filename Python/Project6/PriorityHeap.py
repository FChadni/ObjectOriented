"""
PROJECT 6 - Priority Queues and Heaps
Name: Farjana Chadni
"""

class Node:
    """
    This class represents a node object with k (key) and v (value)
    Node definition should not be changed in any way
    """

    def __init__(self, k, v):
        """
        Initializes node
        :param k: key to be stored in the node
        :param v: value to be stored in the node
        """
        self.key = k
        self.value = v

    def __lt__(self, other):
        """
        Less than comparator
        :param other: second node to be compared to
        :return: True if the node is less than other, False otherwise
        """
        return self.key < other.key or (self.key == other.key and self.value < other.value)

    def __gt__(self, other):
        """
        Greater than comparator
        :param other: second node to be compared to
        :return: True if the node is greater than other, False otherwise
        """
        return self.key > other.key or (self.key == other.key and self.value > other.value)

    def __eq__(self, other):
        """
        Equality comparator
        :param other: second node to be compared to
        :return: True if the nodes are equal, False otherwise
        """
        return self.key == other.key and self.value == other.value

    def __str__(self):
        """
        Converts node to a string
        :return: string representation of node
        """
        return '({0},{1})'.format(self.key, self.value)

    __repr__ = __str__


class PriorityHeap:
    """
    Partially completed data structure. Do not modify completed portions in any way
    """

    def __init__(self, is_min=True):
        """
        Initializes the priority heap
        """
        self._data = []
        self.min = is_min

    def __str__(self):
        """
        Converts the priority heap to a string
        :return: string representation of the heap
        """
        return ', '.join(str(item) for item in self._data)

    def __len__(self):
        """
        Length override function
        :return: Length of the data inside the heap
        """
        return len(self._data)

    __repr__ = __str__

    #   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #   Modify below this line
    def _parent(self, j):
        """
        Calculates the parent index
        :param j: index
        :return: parent index
        """
        return (j - 1) // 2

    def _left(self, j):
        """
        Calculates the left child index
        :param j: index
        :return: left child index
        """
        return 2 * j + 1

    def _right(self, j):
        """
        Calculates the right child index
        :param j: index
        :return: right child index
        """
        return 2 * j + 2

    def _has_left(self, j):
        """
        checks if node has left child
        :param j: index
        :return: bool
        """
        return self._left(j) < len(self._data)

    def _has_right(self, j):
        """
        Checks if node had right child
        :param j: index
        :return: bool
        """
        return self._right(j) < len(self._data)

    def _swap(self, i, j):
        """
        swaps nodes
        :param i: data index
        :param j: data index
        """
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def empty(self):
        """
        checks if empty
        """
        if len(self._data) == 0:
            return True
        if len(self._data) != 0:
            return False

    def top(self):
        """
        peeks into root
        :return: none
        """
        if self.empty():
            return None
        return self._data[0].value

    def push(self, key, val):
        """
        adds nodes to tree
        :param key: key
        :param val: value
        """
        self._data.append(Node(key, val))
        self.percolate_up(len(self._data) - 1)

    def pop(self):
        """
        removes root element from the tree
        :return: removed item
        """
        if self.empty():
            return None
        self._swap(0, len(self._data) - 1)
        item = self._data.pop()
        self.percolate_down(0)
        return Node(item.key, item.value)

    def min_child(self, index):
        """
        checks for minimum child
        :param index: index
        :return: min child
        """
        if self.empty():
            return None
        if self._has_left(index):
            left = self._left(index)
            small_child = left
            if self._has_right(index):
                right = self._right(index)
                if self._data[right] < self._data[left]:
                    small_child = right
                if self._data[right] == self._data[left]:
                    small_child = right
            return small_child
        return None

    def max_child(self, index):
        """
        checks for maximum child
        :param index: index
        :return: max child
        """
        if self.empty():
            return None
        if self._has_left(index):
            left = self._left(index)
            large = left
            if self._has_right(index):
                right = self._right(index)
                if self._data[right] == self._data[left]:
                    large = right
                if self._data[right] > self._data[left]:
                    large = right
            return large
        return None

    def percolate_up(self, index):
        """
        finds position for added element
        :param index: index
        """
        if self.min is True:
            parent = self._parent(index)
            if index > 0 and self._data[index] < self._data[parent]:
                self._swap(index, parent)
                self.percolate_up(parent)
        if self.min is False:
            parent = self._parent(index)
            if index > 0 and self._data[index] > self._data[parent]:
                self._swap(index, parent)
                self.percolate_up(parent)

    def percolate_down(self, index):
        """
        replace root position with another root
        :param j: index
        """
        if self.min is True:
            small_child = self.min_child(index)
            if small_child is not None:
                if self._data[small_child] < self._data[index]:
                    self._swap(index, small_child)
                    self.percolate_down(small_child)
        if self.min is False:
            large_child = self.max_child(index)
            if large_child is not None:
                if self._data[large_child] > self._data[index]:
                    self._swap(index, large_child)
                    self.percolate_down(large_child)


def heap_sort(array):
    """
    sorts a given array using max heap
    :param array: unsorted array
    :return: sorted array
    """
    p = PriorityHeap(min == False)
    n = len(array)
    for i in range(n):
        p.push(array[i], array[i])
    for j in range(n - 1, -1, -1):
        item = p.pop().value
        array[j] = item
    return array


def current_medians(values):
    """
    claculates running median
    :param values: given array
    :return: calculated median array
    """
    minp = PriorityHeap()
    maxp = PriorityHeap(False)
    med = []
    cur_med = 0
    if len(values) == 0:
        return med
    if len(values) == 1:
        return values
    for i in range(len(values)):
        if values[i] >= cur_med:
            minp.push(values[i], values[i])
        else:
            maxp.push(values[i], values[i])
        if (len(minp) - len(maxp)) > 1:
            pop_value = minp.pop().value
            maxp.push(pop_value, pop_value)
        elif (len(maxp) - len(minp)) > 1:
            pop_value = maxp.pop().value
            minp.push(pop_value, pop_value)
        if len(minp) - len(maxp) == 1:
            cur_med = minp.top()
        elif len(maxp) - len(minp) == 1:
            cur_med = maxp.top()
        if len(minp) == len(maxp):
            cur_med = (minp.top() + maxp.top()) / 2
        med.append(cur_med)
    return med

