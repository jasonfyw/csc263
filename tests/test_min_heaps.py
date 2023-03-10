from context import heap

def test_heapify_empty_min_heap():
    A = [None]
    heap.min_heapify(A, 1)
    assert A == [None]

def test_build_basic_min_heap():
    A = [None, 1, 2, 3]
    heap.build_min_heap(A)
    assert A == [None, 1, 2, 3]

def test_extract_min():
    A = [None, 9, 5, 3, 2]
    heap.build_min_heap(A)
    assert A == [None, 2, 5, 3, 9]