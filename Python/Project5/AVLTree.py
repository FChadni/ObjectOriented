"""
PROJECT 5 - AVL Trees
Name:Farjana Chadni
"""

from queue import *
class TreeNode:
    # DO NOT MODIFY THIS CLASS #
    """
        Class representing a node in the TreeNode implemented below.
    """
    __slots__ = 'value', 'parent', 'left', 'right', 'height'

    def __init__(self, value, parent=None, left=None, right=None):
        """
        Initialization of a node
        :param value: value stored at the node
        :param parent: the parent node
        :param left: the left child node
        :param right: the right child node
        """
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right
        self.height = 0

    def __eq__(self, other):
        """
        Determine if the two nodes are equal
        :param other: the node being compared to
        :return: true if the nodes are equal, false otherwise
        """
        if type(self) is not type(other):
            return False
        return self.value == other.value

    def __str__(self):
        """String representation of a node by its value"""
        return str(self.value)

    def __repr__(self):
        """String representation of a node by its value"""
        return str(self.value)


class AVLTree:
    """
        Class representing root in the AVLTree implemented below.
    """

    def __init__(self):
        # DO NOT MODIFY THIS FUNCTION #
        """
        Initializes an empty Binary Search Tree
        """
        self.root = None
        self.size = 0

    def __eq__(self, other):
        # DO NOT MODIFY THIS FUNCTION #
        """
        Describe equality comparison for BSTs ('==')
        :param other: BST being compared to
        :return: True if equal, False if not equal
        """
        if self.root is None and other.root is None:
            return True

        if self.size != other.size or self.root != other.root:
            return False  # size & root comp

        return self._is_equal(self.root.left, other.root.left) and self._is_equal(self.root.right, other.root.right)

    def _is_equal(self, root1, root2):
        # DO NOT MODIFY THIS FUNCTION #
        """
        Checks if rootts are both not None then calls _compare, otherwise checks their equality.
        :param root1: root node of first tree
        :param root2: root node of second tree
        :return: True if equal, False if not
        """
        return self._compare(root1, root2) if root1 and root2 else root1 == root2

    def _compare(self, t1, t2):
        # DO NOT MODIFY THIS FUNCTION #
        """
        Recursively compares two trees, used in __eq__.
        :param t1: root node of first tree
        :param t2: root node of second tree
        :return: True if equal, False if not
        """
        if t1 is None or t2 is None:
            return t1 == t2
        if t1 != t2:
            return False
        return self._compare(t1.left, t2.left) and self._compare(t1.right, t2.right)

    def __str__(self):
        """
        Collects a visual representation of AVL tree
        :return: string of AVL tree
        """
        if not self.root:
            return "Empty AVL Tree..."

        root = self.root
        ans = ""
        bfs_queue = []
        track = {}
        bfs_queue.append((root, 0, root.parent))
        h = AVLTree.height(self.root)

        for i in range(h + 1):
            track[i] = []

        while bfs_queue:
            node = bfs_queue.pop(0)
            if node[1] > h:
                break
            track[node[1]].append(node)

            if node[0] is None:
                bfs_queue.append((None, node[1] + 1, None))
                bfs_queue.append((None, node[1] + 1, None))
                continue

            if node[0].left:
                bfs_queue.append((node[0].left, node[1] + 1, node[0]))
            else:
                bfs_queue.append((None, node[1] + 1, None))

            if node[0].right:
                bfs_queue.append((node[0].right, node[1] + 1, node[0]))
            else:
                bfs_queue.append((None, node[1] + 1, None))

        spaces = pow(2, h) * 12
        ans += "\n"
        ans += "\t\tVisual Level Order Traversal of AVL Tree - Node (Parent Height)".center(spaces)
        ans += "\n\n"
        for i in range(h + 1):
            ans += f"Level {i}: "
            for node in track[i]:
                level = pow(2, i)
                space = int(round(spaces / level))
                if node[0] is None:
                    ans += " " * space
                    continue
                ans += "{} ({} {})".format(node[0], node[2], node[0].height).center(space, " ")
            ans += "\n"
        return ans

    # ------- Implement/Modify the functions below ------- #

    def insert(self, node, value):
        """
        inserts given values in the tree.
        :param node: add node to the tree
        :param value: The value to insert
        :return value inserted as node to tree
        """
        if self.root is None:
            self.root = TreeNode(value)
            node = self.root
            self.size += 1
        if value == node.value:
            return
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value, parent=node)
                self.size += 1
            else:
                self.insert(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value, parent=node)
                self.size += 1
            else:
                self.insert(node.right, value)
        self.update_height(node)
        self.rebalance(node)
        return node

    def fin(self, node, value):
        """
        finds given values in the tree.
        :param node: value as node in tree
        :param value: The value to find
        :return value found
        """
        if self.root is None:
            return None
        if value is node.value:
            return node
        if value < node.value and node.left is not None:
            return self.fin(node.left, value)
        elif value > node.value and node.right is not None:
            return self.fin(node.right, value)

    def remove(self, node, value):
        """
        deletes given values in the tree.
        :param node: deletes node from the tree
        :param value: The value to be deleted
        :return reblanced tree/none as node
        """
        found = self.fin(node, value)
        if not node:
            return node
        if found is None or found.value != value:
            return node
        if value < node.value and node.left is not None:
            node.left = self.remove(node.left, value)
        elif value > node.value and node.right is not None:
            node.right = self.remove(node.right, value)
        else:
            if node.left is None:
                tempnode = node.right
                node = None
                return tempnode
            elif node.right is None:
                tempnode = node.left
                node = None
                return tempnode
            else:
                temp = self.max(node.left)
                node.value = temp.value
                node.left = self.remove(node.left, temp.value)
        if node is None:
            return node
        self.height(node)
        self.rebalance(node)
        return node

    @staticmethod
    def height(node):
        """
        find height of the tree.
        :param node: given nodes
        :return height
        """
        if node is None:
            return -1
        return node.height

    @staticmethod
    def update_height(node):
        """
        updates height of the tree.
        :param node: given nodes
        :return noting
        """
        if node is None:
            return
        node.height = 1 + max(AVLTree.height(node.left), AVLTree.height(node.right))

    def depth(self, value):
        """
        distance from node to root in the tree.
        :param value: The value given to find distance from
        :return height of value to root
        """
        search = self.search(self.root, value)
        if search is None:
            return -1
        if search.parent is None:
            return 0
        return 1+self.depth(search.parent.value)

    def search(self, node, value):
        """
        searches for value in the tree.
        :param node: node to the tree
        :param value: The value to be searched
        :return searched value parent
        """
        if node is None:
            return None
        if value == node.value:
            return node
        if value < node.value and node.left is not None:
            return self.search(node.left, value)
        if value > node.value and node.right is not None:
            return self.search(node.right, value)
        return node

    def inorder(self, node):
        """
        transversed from left to root to right the tree.
        :param node: transversed starts at given node
        :return generator object
        """
        if node is None:
            return node
        if node.left is not None:
            yield from self.inorder(node.left)
        yield node
        if node.right is not None:
            yield from self.inorder(node.right)

    def preorder(self, node):
        """
        transversed from root to left to right the tree.
        :param node: transversed starts at given node
        :return generator object
        """
        if node is None:
            return node
        # if node is not None:
        yield node
        yield from self.preorder(node.left)
        yield from self.preorder(node.right)

    def postorder(self, node):
        """
        transversed from left to right to root the tree.
        :param node: transversed starts at given node
        :return generator object
        """
        if node is None:
            return node
        # if node is not None:
        yield from self.postorder(node.left)
        yield from self.postorder(node.right)
        yield node


    def bfs(self):
        """
        transversed breadth first method.
        :param self: transversed starts at given node
        :return generator object queue
        """
        if self.root is None:
            return
        queue = Queue()
        queue.put(self.root)
        while not queue.empty():
            var = queue.get()
            yield var
            if var.left is not None:
                queue.put(var.left)
            if var.right is not None:
                queue.put(var.right)

    def min(self, node):
        """
        minimum value in the tree.
        :param node: left node to the tree
        :return min left node
        """
        if node is None:
            return None
        if node.left is None:
            return node
        curnode = node
        if curnode.left is not None:
            curnode = curnode.left
        return self.min(curnode.left)

    def max(self, node):
        """
        maximum value in the tree.
        :param node: right node to the tree
        :return max right node
        """
        if node is None:
            return None
        if node.right is None:
            return node
        curnode = node
        if curnode.right is not None:
            curnode = curnode.right
        return self.max(curnode.right)

    def get_size(self):
        """
        size of the tree.
        :return size of the tree
        """
        return self.size

    @staticmethod
    def get_balance(node):
        """
        balance the tree.
        :param node: node to the tree
        :return balance factor
        """
        if node is None:
            return 0
        return AVLTree.height(node.left) - AVLTree.height(node.right)

    @staticmethod
    def set_child(parent, child, is_left):
        """
        searches for value in the tree.
        :param parent: parent lost child (not good parent)
        :param child: the child needs parent
        :param is_left: bool true of false
        :return searched value parent
        """
        if child is not None:
            child.parent = parent
        if is_left is True:
            parent.left = child
            AVLTree.update_height(parent)
        else:
            parent.right = child
            AVLTree.update_height(parent)

    @staticmethod
    def replace_child(parent, current_child, new_child):
        """
        replace child with another child.
        :param parent: parent of current_child (not good parent)
        :param current_child: child
        :param new_child: assigning parent
        :return nothing does replacement
        """
        if parent.left == current_child:
            AVLTree.set_child(parent, new_child, True)
        if parent.right == current_child:
            AVLTree.set_child(parent, new_child, False)

    def left_rotate(self, node):
        """
        left rotation.
        :param node: node needs rotation to balance
        :return nothing does rotation
        """
        rightleft = node.right.left
        if node.parent is not None:
            AVLTree.replace_child(node.parent, node, node.right)
        else:
            self.root = node.right
            self.root.parent = None
        AVLTree.set_child(node.right, node, True)
        AVLTree.set_child(node, rightleft, False)

    def right_rotate(self, node):
        """
        right rotation.
        :param node: node needs rotation to balance
        :return nothing does rotation
        """
        leftright = node.left.right
        if node.parent is not None:
            AVLTree.replace_child(node.parent, node, node.left)
        else:
            self.root = node.left
            self.root.parent = None
        AVLTree.set_child(node.left, node, False)
        AVLTree.set_child(node, leftright, True)

    def rebalance(self, node):
        """
        rotations 4 cases.
        :param node: node needs rotation to balance
        :return rotated balanced tree
        """
        AVLTree.update_height(node)
        if AVLTree.get_balance(node) == -2:
            if AVLTree.get_balance(node.right) == 1:
                AVLTree.right_rotate(self, node.right)
            var = AVLTree.left_rotate(self, node)
            AVLTree.update_height(node.parent)
            return var
        if AVLTree.get_balance(node) == 2:
            if AVLTree.get_balance(node.left) == -1:
                AVLTree.left_rotate(self, node.left)
            var = AVLTree.right_rotate(self, node)
            AVLTree.update_height(node.parent)
            return var
        return node

# ------- Application Problem ------- #
def avlh(node):
    """
    find height
    :param node: node height max balance
    :return max side + 1
    """
    if node is None:
        return 0
    return 1 + max(avlh(node.left), avlh(node.right))

def is_avl_tree(node):
    """
    checks is AVL tree or not (balanced or not)
    :param node: bool true of false
    """
    if node is None:
        return True
    if abs(avlh(node.left) - avlh(node.right)) <= 1 and is_avl_tree(node.left) and is_avl_tree(node.right):
        return True
    return False

