from context import heap

def test_heapify_empty_max_heap():
    A = [None]
    heap.max_heapify(A, 1)
    assert A == [None]

def test_build_basic_max_heap():
    A = [None, 1, 2, 3]
    heap.build_max_heap(A)
    assert A == [None, 3, 2, 1]

def test_build_max_heap():
    A = [None, 48, 23, 17, 26, 14, 87, 53, 89, 32, 49, 95, 12]
    heap.build_max_heap(A)
    assert A == [None, 95, 89, 87, 48, 49, 17, 53, 26, 32, 23, 14, 12]

def test_extract_max():
    A = [None, 48, 23, 17, 26, 14, 87, 53, 89, 32, 49, 95, 12]
    heap.build_max_heap(A)
    assert A == [None, 95, 89, 87, 48, 49, 17, 53, 26, 32, 23, 14, 12]

    max_ = heap.heap_extract_max(A)
    assert max_ == 95
    assert A == [None, 89, 49, 87, 48, 23, 17, 53, 26, 32, 12, 14]
    
    max_ = heap.heap_extract_max(A)
    assert max_ == 89
    assert A == [None, 87, 49, 53, 48, 23, 17, 14, 26, 32, 12]
