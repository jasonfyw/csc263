from typing import TypeVar
import sys
from ._bst_helpers import NIL

T = TypeVar('T')


"""
============================================================
AVL Tree Classes
============================================================
"""

class AVLNode:
    def __init__(self, x: T = None) -> None:
        self.item = x
        self.left = NIL
        self.right = NIL
        self.height = 0


class AVLTree:
    def __init__(self) -> None:
        self.root = NIL

    def insert(self, x: T) -> None:
        self.root = avl_insert(self.root, x)

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
    # PRECOND: parent != NIL and parent.right != NIL
    child = parent.right
    parent.right = child.left
    child.left = parent
    parent.height = 1 + max(parent.left.height, parent.right.height)
    child.height = 1 + max(child.left.height, child.right.height)
    return child


def avl_rotate_right(parent: AVLNode) -> AVLNode:
    # PRECOND: parent != NIL and parent.left != NIL
    child = parent.left
    parent.left = child.right
    child.right = parent
    parent.height = 1 + max(parent.left.height, parent.right.height)
    child.height = 1 + max(child.left.height, child.right.height)
    return child


