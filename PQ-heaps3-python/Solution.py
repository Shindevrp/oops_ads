class BinaryHeapPriorityQueue:
    def __init__(self):
        self.heap = []

    def bubble_up(self, idx):
        while idx > 0:
            prnt = (idx - 1) // 2
            if self.heap[idx] < self.heap[prnt]:
                self.heap[idx], self.heap[prnt] = self.heap[prnt], self.heap[idx]
                idx = prnt
            else:
                break

    def bubble_down(self, idx):
        size = len(self.heap)
        while 2 * idx + 1 < size:
            l = 2 * idx + 1
            r = 2 * idx + 2
            smallest = l

            if r < size and self.heap[r] < self.heap[l]:
                smallest = r

            if self.heap[idx] > self.heap[smallest]:
                self.heap[idx], self.heap[smallest] = self.heap[smallest], self.heap[idx]
                idx = smallest
            else:
                break

    def add(self, e):
        self.heap.append(e)
        self.bubble_up(len(self.heap) - 1)

    def offer(self, e):
        self.add(e)

    def peek(self):
        return self.heap[0] if self.heap else None

    def poll(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.bubble_down(0)
        return root

    def remove(self, o):
        for i in range(len(self.heap)):
            if self.heap[i] == o:
                self.heap[i] = self.heap.pop()
                self.bubble_down(i)
                return True
        return False

    def clear(self):
        self.heap = []

    def contains(self, o):
        return o in self.heap

    def size(self):
        return len(self.heap)

    def iterator(self):
        return iter(self.heap) 