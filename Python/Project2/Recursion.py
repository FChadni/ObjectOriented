"""
PROJECT 2 - Linked List Recursion
Name: Farjana Chadni
PID: A58365164
"""


class LinkedNode:
    # DO NOT MODIFY THIS CLASS #
    __slots__ = '_value', '_next'

    def __init__(self, value, next=None):
        """
        DO NOT EDIT
        Initialize a node
        :param value: value of the node
        :param next: pointer to the next node in the LinkedList, default is None
        """
        self._value = value  # element at the node
        self._next = next  # reference to next node in the LinkedList

    def __repr__(self):
        """
        DO NOT EDIT
        String representation of a node
        :return: string of value
        """
        return str(self._value)

    __str__ = __repr__
    def get_value(self):
        """
        :param _value: getter
        """
        return self._value

    def get_next(self):
        """
        :param _next: getter
        """
        return self._next

    def set_value(self, value):
        """
        :param value: get value
        """
        self._value = value

    def set_next(self, next):
        """
        :param next: get next
        """
        self._next = next


# IMPLEMENT THESE FUNCTIONS - DO NOT MODIFY FUNCTION SIGNATURES #


def insert(value, node=None):
    """
    :param value: value to insert
    :param node: keeping track of where should the value be placed based on node
    :return: inserted node
    """
    if node is None:
        newnode = LinkedNode(value)
        return newnode
    else:
        newnode = insert(value, node._next)
        node._next = newnode
        return node

def to_string(node):
    """
    :param node: check for node of values in the list that needed to put into string
    :return: string of values with comma and space
    """
    if node is None:
        return ""
    new = to_string(node._next)
    temp = str(node) + ", " + new
    if node._next is None:
        temp = temp.replace(", ","")
    return str(temp)

def remove(value, node):
    """
    :param value: value that needed to be removed
    :param node: node that keeps track of which value to remove (pointer)
    :return: after list after removed values
    """
    if node is None:
        return None
    if node._value is value:
        node = node._next
        return node
    else:
        node._next = remove(value, node._next)
    return node

def remove_all(value, node):
    """
    :param value: value that needed to be removed
    :param node: node that keeps track of which value to remove
    :return: after removed values
    """
    if node is None:
        return None
    if node._value is value:
        return remove_all(value, node._next)
    else:
        node._next = remove_all(value, node._next)
    return node

def search(value, node):
    """
    :param value: values searching for
    :param node: pointer that finds the value
    :return: searched values (ture or false)
    """
    if node is None:
        return None
    if node._value is value:
        return node
    return search(value, node._next)

def length(node):
    """
    :param node: pointer moves each times over the list
    :return: length of list
    """
    if node is None:
        return 0
    else:
        return length(node._next) + 1

def sum_list(node):
    """
    :param node: pointer moves each times over the list
    :return: sum of all the nodes in side list
    """
    if node is None:
        return 0
    else:
        return sum_list(node._next) + node._value

def count(value, node):
    """
    :param value: needed to be counter
    :param node: pointer moves to next value
    :return: count of values inside node
    """
    if node is None:
        return 0
    if node._value == value:
        return (1 + count(value, node._next))
    else:
        return count(value, node._next)

def reverse(node):
    """
    :param node: pointer moves along list
    :return: reversed list
    """
    if node is None:
        return node
    if node._next is None:
        return node
    call_fuc = reverse(node._next)
    node._next._next = node
    node._next = None
    return call_fuc
def list_percentage(node, percentage, counter=0):
    """
    :param node: pointer moves along list
    :param percentage: given percent 
    :param counter: node that percentage matches
    :return: node that matches calculated value
    """
    if percentage is 0:
        return None
    if percentage is 1:
        return node
    if node is None:
        return None
    
    if node._next is None:
        counter += 1
        calc = int((counter - counter * percentage) +1)
        return calc
        #return node
    else:
        counter += 1
        re = list_percentage(node._next, percentage, counter)
        if isinstance(re, int):
            if re == counter:
                return node
            if re == (counter+1):
                return node._next
        return re
