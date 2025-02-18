from typing import List, TypeVar, Generic

T = TypeVar('T') 
class MinHeap(Generic[T]):
    def __init__(self, elements: List[T] = None):
        self.heap = elements if elements else []
        if self.heap:
            self.build_min_heap()

    def parent(self, index: int) -> int:
        return (index - 1) >> 1  

    def left(self, index: int) -> int:
        return (index << 1) + 1 

    def right(self, index: int) -> int:
        return (index << 1) + 2  

    def heapify(self, index: int):
        smallest = index
        left_index = self.left(index)
        right_index = self.right(index)

        if left_index < len(self.heap) and self.heap[left_index] < self.heap[smallest]:
            smallest = left_index
        if right_index < len(self.heap) and self.heap[right_index] < self.heap[smallest]:
            smallest = right_index

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self.heapify(smallest)

    def build_min_heap(self):
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self.heapify(i)

    def push(self, element: T):
        self.heap.append(element)
        index = len(self.heap) - 1
        while index > 0 and self.heap[self.parent(index)] > self.heap[index]:
            parent_index = self.parent(index)
            self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
            index = parent_index

    def pop(self) -> T:
        if not self.heap:
            raise IndexError ("Empty Heap")
        root = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        if self.heap:
            self.heapify(0)
        return root

    def __repr__(self):
        return str(self.heap)

def test_heap():
    elements = [9, 8, 6, 1, 3, 4, 5]
    heap = MinHeap(elements)
    print("Built Heap:", heap)
    heap.push(0)
    print("After Pushing 0:", heap)
    print("Popped Element:", heap.pop())
    print("After Popping Root:", heap)

if __name__ == "__main__":
    test_heap()
