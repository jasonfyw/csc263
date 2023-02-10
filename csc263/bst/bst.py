from typing import TypeVar, Tuple
from ._bst_helpers import NIL
from ._node import Node

T = TypeVar('T')


"""
============================================================
Binary Search Tree Classes
============================================================
"""

class BSTNode(Node):
    def __init__(self, item=None):
        self.left = NIL
        self.right = NIL
        self.item = item

class BST:
    def __init__(self, root=NIL):
        self.root = root

    def insert(self, x: T) -> None:
        """Method to insert <x> to BST

        Args:
            x (T): comparable item to insert
        """
        self.root = bst_insert(self.root, x)

    def delete(self, x: T) -> None:
        """Method to delete <x> from BST

        Args:
            x (T): comparable item to delete
        """
        self.root = bst_delete(self.root, x)
    
    def __str__(self) -> str:
        """Return a horizontal string representation of the  tree 

        Returns:
            str: string representation of the tree
        """
        return self._pretty_print(self.root, 0)
    
    def __repr__(self) -> str:
        """Return a horizontal string representation of the  tree 

        Returns:
            str: string representation of the tree
        """
        return self._pretty_print(self.root, 0)
    
    def _pretty_print(self, node: BSTNode, level: int):
        """Private helper function to recursively generate each level in the 
        string representation

        Args:
            node (BSTNode): current node
            level (int): the level of the node
        """
        result = ""
        if node != NIL:
            result += self._pretty_print(node.right, level + 1)
            result += "\t" * level + str(node.item) + "\n"
            result += self._pretty_print(node.left, level + 1)
        return result


"""
============================================================
BST Insertion
============================================================
"""

def bst_insert(root: BSTNode, x: T):
    if root == NIL:
        root = BSTNode(x)
    elif x < root.item:
        root.left = bst_insert(root.left, x)
    elif x > root.item:
        root.right = bst_insert(root.right, x)
    else:
        root.item = x
    return root

def bst_delete(root: BSTNode, x: T) -> BSTNode:
    """Deletes node with item <x> from tree with root <root>

    Args:
        root (BSTNode): root node to delete from
        x (T): the comparable item to delete

    Returns:
        BSTNode: <root> with <x> deleted 
    """
    if root == NIL:
        pass
    elif x < root.item:
        root.left = bst_delete(root.left, x)
    elif x > root.item:
        root.right = bst_delete(root.right, x)
    else: # x == root.item
        if root.left == NIL:
            root = root.right
        elif root.right == NIL:
            root = root.left
        else:
            root.item, root.left = bst_extract_max(root.left)
    return root


def bst_extract_max(root: BSTNode) -> Tuple[T, BSTNode]:
    """Returns and removes maximum item in <root>

    Args:
        root (AVLNode): root of subtree to extract max from

    Returns:
        Tuple[T, AVLNode]: maximum item, new root with extracted max
    """
    # PRECOND: root != NIL
    if root.right == NIL:
        return root.item, root.left
    else:
        item, root.right = bst_extract_max(root.right)
        return item, root