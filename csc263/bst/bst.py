from typing import TypeVar
from ._bst_helpers import NIL

T = TypeVar('T')


class BSTNode:
    def __init__(self, item=None):
        self.left = NIL
        self.right = NIL
        self.item = item

class BST:
    def __init__(self, root=NIL):
        self.root = root
    
    def __str__(self):
        self.print_tree()
        return ''

    def print_tree(self, level=0):
        if self.root == NIL:
            return
        self.print_tree(self.root.right, level + 1)
        print("    " * level + str(self.root.item))
        self.print_tree(self.root.left, level + 1)


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