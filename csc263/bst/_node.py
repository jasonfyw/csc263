from abc import abstractmethod

class Node:
    """Abstract class for a tree node
    """
    @abstractmethod
    def __init__(self, item=None):
        raise NotImplementedError