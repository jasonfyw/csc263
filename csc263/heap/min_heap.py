from typing import List, TypeVar
from . import heap

T = TypeVar('T')

def min_heapify(A: List[T], i: int) -> None:
    l = heap.left(i)
    r = heap.right(i)
    if l <= len(A) - 1 and A[l] < A[i]:
        smallest = l
    else:
        smallest = i

    if r <= len(A) - 1 and A[r] < A[smallest]:
        smallest = r

    if smallest != i:
        A[i], A[smallest] = A[smallest], A[i]
        min_heapify(A, smallest)


def build_min_heap(A: List[T]) -> None:
    for i in range((len(A) - 1) // 2, 0, -1):
        min_heapify(A, i)


def heap_min(A: List[T]) -> T:
    return A[1]


def heap_extract_min(A: List[T]) -> T:
    if len(A) <= 1:
        raise ValueError('Heap is empty')
    min_ = A[1]
    A[1] = A.pop()
    min_heapify(A, 1)
    return min_


def heap_decrease_key(A: List[T], i: int, key: T) -> None:
    if key < A[i]:
        raise ValueError('New key is smaller than current key')
    A[i] = key
    while i > 1 and A[heap.parent(i)] > A[i]:
        A[i], A[heap.parent(i)] = A[heap.parent(i)], A[i]
        i = heap.parent(i)


def min_heap_insert(A: List[T], key: T) -> None:
    A.append(float('inf'))
    heap_decrease_key(A, len(A) - 1, key)