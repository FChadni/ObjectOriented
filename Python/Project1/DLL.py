class DLLError(Exception):
    """
    Class representing an error related to the DLL class implemented below.
    """
    pass


class DLLNode:
    """
    Class representing a node in the doubly linked list implemented below.
    """

    def __init__(self, value, next=None, prev=None):
        """
        Constructor
        @attribute value: the value to give this node
        @attribute next: the next node for this node
        @attribute prev: the previous node for this node
        """
        self.next = next
        self.prev = prev
        self.value = value

    def __repr__(self):
        return str(self.value)

    def __str__(self):
        return str(self.value)


class DLL:
    """
    Class representing a doubly linked list.
    """

    def __init__(self):
        """
        Constructor
        @attribute head: the head of the linked list
        @attribute tail: the tail of the linked list
        @attribute size: the size of the linked list
        """
        self.head = None
        self.tail = None
        self.size = 0

    def __repr__(self):
        """
        iterates through the linked list to generate a string representation
        :return: string representation of the linked list
        """
        res = ""
        node = self.head
        while node:
            res += str(node)
            if node.next:
                res += " "
            node = node.next
        return res

    def __str__(self):
        """
        iterates through the linked list to generate a string representation
        :return: string representation of the linked list
        """
        res = ""
        node = self.head
        while node:
            res += str(node)
            if node.next:
                res += " "
            node = node.next
        return res

    ######### MODIFY BELOW ##########

    def is_empty(self):
        """
        Determines if the linked list is empty or not
        :return: [boolean] true if DLL is empty, false otherwise
        """
        if self.size == 0:
            return True
        else:
            return False

    def insert_front(self, value):
        """
        Inserts a value into the front of the list
        :param value: the value to insert
        """
        newnode = DLLNode(value, None, None)
        if self.size == 0:
            self.head = newnode
            self.tail = newnode
        else:
            newnode.next = self.head
            self.head.prev = newnode
            self.head = newnode
        self.size += 1

    def insert_back(self, value):
        """
        Inserts a value into the back of the list
        :param value: the value to insert
        """
        newnode = DLLNode(value, None, None)
        if self.is_empty():
            self.head = newnode
            self.tail = newnode
        else:
            self.tail.next = newnode
            newnode.prev = self.tail
            self.tail = newnode
        self.size += 1

    def delete_front(self):
        """
        Deletes the front node of the list
        """
        if self.size == 0:
            raise DLLError
        elif self.size == 1:
            self.tail = None
            self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.size -= 1

    def delete_back(self):
        if self.size == 0:
            raise DLLError
        elif self.size == 1:
            self.tail = None
            self.head = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.size -= 1

    def delete_value(self, value):
        """
        Deletes the first instance of the value in the list.
        :param value: The value to remove
        """
        if self.size == 0:
            raise DLLError
        elif value == self.head.value:
            self.delete_front()
        elif value == self.tail.value:
            self.delete_back()
        else:
            current = self.head
            while current:
                if current.value == value:
                    current.next.prev = current.prev
                    current.prev.next = current.next
                    break
                current = current.next
            raise DLLError

    def delete_all(self, value):
        """
        Deletes all instances of the value in the list
        :param value: the value to remove
        """
        tem = self.count(value)
        if tem == 0:
            raise DLLError
        if self.size == 0:
            raise DLLError

        while value == self.head.value:
            self.delete_front()
        while value == self.tail.value:
            self.delete_back()

        current = self.head
        while current:
            if current.value == value:
                current.prev.next = current.next
                current.next.prev = current.prev
                self.size -=1
            current = current.next
    
        
    def find_first(self, value):
        """
        Finds the first instance of the value in the list
        :param value: the value to find
        :return: [DLLNode] the first node containing the value
        """
        curnode = self.head
        while curnode:
            if curnode.value == value:
                return curnode
            curnode = curnode.next
        raise DLLError

    def find_last(self, value):
        """
        Finds the last instance of the value in the list
        :param value: the value to find
        :return: [DLLNode] the last node containing the value
        """
        curnode = self.tail
        while curnode:
            if curnode.value == value:
                return curnode
            curnode = curnode.prev
        raise DLLError

    def find_all(self, value):
        """
        Finds all of the instances of the value in the list
        :param value: the value to find
        :return: [List] a list of the nodes containing the value
        """
        list1 = []
        curnode = self.head
        while curnode:
            if curnode.value == value:
                list1.append(curnode)
            curnode = curnode.next
        if list1 == []:
            raise DLLError
        return list1

    def count(self, value):
        """
        Finds the count of times that the value occurs in the list
        :param value: the value to count
        :return: [int] the count of nodes that contain the given value
        """
        count = 0
        curnode = self.head
        while (curnode != None):
            if (curnode.value == value):
                count += 1
            curnode = curnode.next
        return count

    def sum(self):
        """
        Finds the sum of all nodes in the list
        :param start: the indicator of the contents of the list
        :return: the sum of all items in the list
        """
        if (self.size == 0):
            return None
        sum1 = type(self.head.value)()
        curnode = self.head
        while curnode:
            sum1 += curnode.value
            curnode = curnode.next
        return sum1


def reverse(LL):
    """
    Reverses a linked list in place
    :param LL: The linked list to reverse
    """
    temnode = None
    curnode = LL.head
    val = LL.head
    LL.head = LL.tail
    LL.tail = val
    while curnode:
        temnode = curnode.prev
        curnode.prev = curnode.next
        curnode.next = temnode
        curnode = curnode.prev
    if temnode:
        LL.head = temnode.prev




