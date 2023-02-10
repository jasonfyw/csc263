from ._node import Node


class NILNode(Node):
    """Class implementing Node that contains a self-referencing NIL node
    """
    def __init__(self) -> None:
        self.item = None
        self.left = self
        self.right = self
        self.height = -1

NIL = NILNode()