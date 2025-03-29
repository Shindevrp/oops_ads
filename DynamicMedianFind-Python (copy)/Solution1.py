# class MedianFinder:
#     def __init__(self):
        
#         self.lower = [] 
#         self.upper = []  

#     def heap_push(self, heap, value, is_max):
#         heap.append(value)
#         idx = len(heap) - 1
#         while idx > 0:
#             parent = (idx - 1) // 2
#             if (is_max and heap[idx] > heap[parent]) or (not is_max and heap[idx] < heap[parent]):
#                 heap[idx], heap[parent] = heap[parent], heap[idx]
#                 idx = parent
#             else:
#                 break

#     def heap_pop(self, heap, is_max):
#         if not heap:
#             return None
#         root = heap[0]
#         heap[0] = heap[-1]
#         heap.pop()
#         idx, n = 0, len(heap)
#         while True:
#             left = 2 * idx + 1
#             right = 2 * idx + 2
#             swap = idx
#             if left < n and ((is_max and heap[left] > heap[swap]) or (not is_max and heap[left] < heap[swap])):
#                 swap = left
#             if right < n and ((is_max and heap[right] > heap[swap]) or (not is_max and heap[right] < heap[swap])):
#                 swap = right
#             if swap == idx:
#                 break
#             heap[idx], heap[swap] = heap[swap], heap[idx]
#             idx = swap
#         return root

#     def insert(self, x):
#         if not self.lower or x <= self.lower[0]:
#             self.heap_push(self.lower, x, True)
#         else:
#             self.heap_push(self.upper, x, False)
#         self.balance()

#     def balance(self):
#         if len(self.lower) > len(self.upper) + 1:
#             temp = self.heap_pop(self.lower, True)
#             self.heap_push(self.upper, temp, False)
#         elif len(self.lower) < len(self.upper):
#             temp = self.heap_pop(self.upper, False)
#             self.heap_push(self.lower, temp, True)

#     def get_median(self):
#         if not self.lower:
#             return "Invalid"
#         return self.lower[0]

#     def remove_median(self):
#         if not self.lower:
#             return "Invalid"
#         median = self.heap_pop(self.lower, True)
#         self.balance()
#         return median


# def main():
#     median_finder = MedianFinder()
#     results = []
    
#     try:
#         while True:
#             try:
#                 line = input().strip()
#                 if not line:
#                     continue
#                 s = line.split()
#                 if s[0] == 'I':
#                     median_finder.insert(int(s[1]))
#                 elif s[0] == 'M':
#                     results.append(str(median_finder.get_median()))
#                 elif s[0] == 'R':
#                     results.append(str(median_finder.remove_median()))
#             except EOFError:
#                 break
#     except KeyboardInterrupt:
#         pass

#     if results:
#         print("\n".join(results))


# if __name__ == "__main__":
#     main()


class MedianFinder:
    def __init__(self):
        self.lower = []  
        self.upper = [] 

    def push(self, heap, num, is_max):
        heap.append(num)
        i = len(heap) - 1
        while i > 0:
            parent = (i - 1) // 2
            if is_max:
                if heap[i] > heap[parent]:
                    heap[i], heap[parent] = heap[parent], heap[i]
                    i = parent
                else:
                    break
            else:
                if heap[i] < heap[parent]:
                    heap[i], heap[parent] = heap[parent], heap[i]
                    i = parent
                else:
                    break

    def pop(self, heap, is_max):
        if len(heap) == 0:
            return None
        root = heap[0]
        heap[0] = heap[-1]
        heap.pop()
        i = 0
        n = len(heap)
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            swap = i
            if left < n:
                if is_max:
                    if heap[left] > heap[swap]:
                        swap = left
                else:
                    if heap[left] < heap[swap]:
                        swap = left
            if right < n:
                if is_max:
                    if heap[right] > heap[swap]:
                        swap = right
                else:
                    if heap[right] < heap[swap]:
                        swap = right
            if swap == i:
                break
            heap[i], heap[swap] = heap[swap], heap[i]
            i = swap
        return root

    def balance(self):
        if len(self.lower) > len(self.upper) + 1:
            num = self.pop(self.lower, True)
            self.push(self.upper, num, False)
        elif len(self.lower) < len(self.upper):
            num = self.pop(self.upper, False)
            self.push(self.lower, num, True)

    def insert(self, num):
        if len(self.lower) == 0 or num <= self.lower[0]:
            self.push(self.lower, num, True)
        else:
            self.push(self.upper, num, False)
        self.balance()

    def get_median(self):
        if len(self.lower) == 0:
            return "Invalid"
        return self.lower[0]

    def remove_median(self):
        if len(self.lower) == 0:
            return "Invalid"
        med = self.pop(self.lower, True)
        self.balance()
        return med


def main():
    mf = MedianFinder()
    results = []
    while True:
        try:
            line = input().strip()
        except EOFError:
            break
        if line == "":
            continue
        parts = line.split()
        if parts[0] == "I":
            mf.insert(int(parts[1]))
        elif parts[0] == "M":
            results.append(str(mf.get_median()))
        elif parts[0] == "R":
            results.append(str(mf.remove_median()))
    if results:
        print("\n".join(results))


if __name__ == "__main__":
    main()
