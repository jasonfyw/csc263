from typing import TypeVar, Tuple
import sys
from ._bst_helpers import NIL
from ._node import Node

T = TypeVar('T')


"""
============================================================
AVL Tree Classes
============================================================
"""

class AVLNode(Node):
    """Class representing a node in an AVL tree
    """
    def __init__(self, x: T = None) -> None:
        self.item = x
        self.left = NIL
        self.right = NIL
        self.height = 0


class AVLTree:
    """Class representing an AVL Tree
    """
    def __init__(self) -> None:
        """Create an empty AVL tree
        """
        self.root = NIL

    def insert(self, x: T) -> None:
        """Method to insert <x> to AVLTree

        Args:
            x (T): comparable item to insert
        """
        self.root = avl_insert(self.root, x)

    def delete(self, x: T) -> None:
        """Method to delete <x> from AVLTree

        Args:
            x (T): comparable item to delete
        """
        self.root = avl_delete(self.root, x)

    def __str__(self) -> str:
        self.print_helper(self.root)
        return ''

    def print_helper(self, node: AVLNode, indent: str = '', last: bool = True) -> None:
        if node != NIL:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "
            print(node.item)
            self.print_helper(node.left, indent, False)
            self.print_helper(node.right, indent, True)


"""
============================================================
AVL Insertion
============================================================
"""

def avl_insert(root: AVLNode, x: T) -> AVLNode:
    """Inserts item <x> into AVLNode <root>

    Args:
        root (AVLNode): the root of the AVL tree

    Returns:
        AVLNode: the new root node with the inserted item
    """
    if root == NIL:
        root = AVLNode(x)
    elif x < root.item:
        root.left = avl_insert(root.left, x)
        root = avl_rebalance_right(root)
    elif x > root.item:
        root.right = avl_insert(root.right, x)
        root = avl_rebalance_left(root)
    else: # x == root.item
        root.item = x
    return root


"""
============================================================
AVL Rebalancing
============================================================
"""

def avl_rebalance_left(root: AVLNode) -> AVLNode:
    """Rebalances the left subtree

    Args:
        root (AVLNode): root node of the subtree to rebalance

    Returns:
        AVLNode: the new rebalanced node
    """
    # PRECOND: root != NIL
    # first recalculate height
    root.height = 1 + max(root.left.height, root.right.height)
    # rebalance left if necessary
    if root.right.height > 1 + root.left.height:
        # check for double rotation
        if root.right.left.height > root.right.right.height:
            root.right = avl_rotate_right(root.right)
        root = avl_rotate_left(root)
    return root


def avl_rebalance_right(root: AVLNode) -> AVLNode:
    """Rebalances the right subtree

    Args:
        root (AVLNode): root node of the subtree to rebalance

    Returns:
        AVLNode: the new rebalanced node
    """
    # PRECOND: root != NIL
    # first recalculate height
    root.height = 1 + max(root.left.height, root.right.height)
    # rebalance if necessary
    if root.left.height > 1 + root.right.height:
        # check for double rotation
        if root.left.right.height > root.left.left.height:
            root.left = avl_rotate_left(root.left)
        root = avl_rotate_right(root)
    return root


def avl_rotate_left(parent: AVLNode) -> AVLNode:
    """Performs one left rotation on <parent>

    Args:
        parent (AVLNode): the node on which to rotate

    Returns:
        AVLNode: the parent node after rotation
    """
    # PRECOND: parent != NIL and parent.right != NIL
    child = parent.right
    parent.right = child.left
    child.left = parent
    parent.height = 1 + max(parent.left.height, parent.right.height)
    child.height = 1 + max(child.left.height, child.right.height)
    return child


def avl_rotate_right(parent: AVLNode) -> AVLNode:
    """Performs one right rotation on <parent>

    Args:
        parent (AVLNode): the node on which to rotate

    Returns:
        AVLNode: the parent node after rotation
    """
    # PRECOND: parent != NIL and parent.left != NIL
    child = parent.left
    parent.left = child.right
    child.right = parent
    parent.height = 1 + max(parent.left.height, parent.right.height)
    child.height = 1 + max(child.left.height, child.right.height)
    return child


"""
============================================================
AVL Deletion
============================================================
"""

def avl_delete(root: AVLNode, x: T) -> AVLNode:
    """Deletes node with item <x> from tree with root <root>

    Args:
        root (AVLNode): root node to delete from
        x (T): the comparable item to delete

    Returns:
        AVLNode: <root> with <x> deleted 
    """
    if root == NIL:
        pass
    elif x < root.item:
        root.left = avl_delete(root.left, x)
        root = avl_rebalance_left(root)
    elif x > root.item:
        root.right = avl_delete(root.right, x)
        root = avl_rebalance_right(root)
    else: # x == root.item
        if root.left == NIL:
            root = root.right
        elif root.right == NIL:
            root = root.left
        else:
            if root.left.height > root.height:
                root.item, root.left = avl_extract_max(root.left)
            else:
                root.item, root.right = avl_extract_min(root.right)
            root.height = 1 + max(root.left.height, root.right.height)
    return root


def avl_extract_max(root: AVLNode) -> Tuple[T, AVLNode]:
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
        item, root.right = avl_extract_max(root.right)
        root = avl_rebalance_right(root)
        return item, root
    

def avl_extract_min(root: AVLNode) -> Tuple[T, AVLNode]:
    """Returns and removes minimum item in <root>

    Args:
        root (AVLNode): root of subtree to extract min from

    Returns:
        Tuple[T, AVLNode]: minimum item, new root with extracted min
    """
    # PRECOND: root != NIL
    if root.left == NIL:
        return root.item, root.right
    else:
        item, root.left = avl_extract_min(root.left)
        root = avl_rebalance_left(root)
        return item, root

