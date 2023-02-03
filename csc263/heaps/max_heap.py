from typing import List, TypeVar
from . import heap

T = TypeVar('T')

def max_heapify(A: List[T], i: int) -> None:
    l = heap.left(i)
    r = heap.right(i)
    if l <= len(A) - 1 and A[l] > A[i]:
        largest = l
    else:
        largest = i

    if r <= len(A) - 1 and A[r] > A[largest]:
        largest = r

    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest)


def build_max_heap(A: List[T]) -> None:
    for i in range((len(A) - 1) // 2, 0, -1):
        max_heapify(A, i)


def heap_max(A: List[T]) -> T:
    return A[1]


def heap_extract_max(A: List[T]) -> T:
    if len(A) <= 1:
        raise ValueError('Heap is empty')
    max_ = A[1]
    A[1] = A.pop()
    max_heapify(A, 1)
    return max_


def heap_increase_key(A: List[T], i: int, key: T) -> None:
    if key < A[i]:
        raise ValueError('New key is smaller than current key')
    A[i] = key
    while i > 1 and A[heap.parent(i)] < A[i]:
        A[i], A[heap.parent(i)] = A[heap.parent(i)], A[i]
        i = heap.parent(i)


def max_heap_insert(A: List[T], key: T) -> None:
    A.append(float('-inf'))
    heap_increase_key(A, len(A) - 1, key)