from typing import List
from . import heap

def max_heapify(A: List[int], i: int) -> None:
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