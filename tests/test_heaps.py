from context import heaps

def test_empty_heap():
    A = [None]
    heaps.max_heapify(A, 1)
    assert A == [None]

def test_basic_heap():
    A = [None, 1, 2, 3]
    heaps.max_heapify(A, 1)
    assert A == [None, 3, 2, 1]