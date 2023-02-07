class NILNode:
    def __init__(self) -> None:
        self.item = None
        self.left = self
        self.right = self
        self.height = -1

NIL = NILNode()