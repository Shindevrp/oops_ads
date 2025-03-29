# class MedianFinder:
#     def __init__(self):
#         self.max_heap = []  
#         self.min_heap = []  
    
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
#         if not self.max_heap or x <= -self.max_heap[0]:
#             self.heap_push(self.max_heap, -x, True)  
#         else:
#             self.heap_push(self.min_heap, x, False)  
#         self.balance()
    
#     def get_median(self):
#         return -self.max_heap[0] if self.max_heap else "Invalid"
    
#     def remove_median(self):
#         if not self.max_heap:
#             return "Invalid"
#         median = self.heap_pop(self.max_heap, True)
#         self.balance()
#         return -median
    
#     def balance(self):
#         if len(self.max_heap) > len(self.min_heap) + 1:
#             self.heap_push(self.min_heap, -self.heap_pop(self.max_heap, True), False)
#         elif len(self.min_heap) > len(self.max_heap):
#             self.heap_push(self.max_heap, -self.heap_pop(self.min_heap, False), True)


# def main():
#     median = MedianFinder()
    
#     try:
#         while True:
#             line = input().strip()
#             if not line:
#                 continue
#             s = line.split()
#             if s[0] == 'I':
#                 median.insert(int(s[1]))
#             elif s[0] == 'M':
#                 print(median.get_median())
#             elif s[0] == 'R':
#                 print(median.remove_median())
#     except KeyboardInterrupt:
#         pass
#     except EOFError:
#         pass


# if __name__ == "__main__":
#     main()


# class MedianFinder:
#     def __init__(self):
#         self.max_heap = []  
#         self.min_heap = []  

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
#         if not self.max_heap or x <= -self.max_heap[0]:
#             self.heap_push(self.max_heap, -x, True)  
#         else:
#             self.heap_push(self.min_heap, x, False)
#         self.balance()

#     def get_median(self):
#         return -self.max_heap[0] if self.max_heap else "Invalid"

#     def remove_median(self):
#         if not self.max_heap:
#             return "Invalid"
#         median = self.heap_pop(self.max_heap, True)
#         self.balance()
#         return -median

#     def balance(self):
#         if len(self.max_heap) > len(self.min_heap) + 1:
#             self.heap_push(self.min_heap, -self.heap_pop(self.max_heap, True), False)
#         elif len(self.min_heap) > len(self.max_heap):
#             self.heap_push(self.max_heap, -self.heap_pop(self.min_heap, False), True)


# # def main():
# #     median_finder = MedianFinder()

# #     try:
# #         while True:
# #             line = input().strip()
# #             if not line:
# #                 continue
# #             command = line.split()
# #             if command[0] == 'I':
# #                 median_finder.insert(int(command[1]))
# #             elif command[0] == 'M':
# #                 print(median_finder.get_median())
# #             elif command[0] == 'R':
# #                 print(median_finder.remove_median())
# #     except (KeyboardInterrupt, EOFError):
# #         pass


# # if __name__ == "__main__":
# #     main()


# def main():
#     median_finder = MedianFinder()
    
#     inputs = []
#     try:
#         while True:
#             line = input().strip()
#             if not line:
#                 continue
#             inputs.append(line)
#     except EOFError:
#         pass

#     for command in inputs:
#         parts = command.split()
#         if parts[0] == 'I':
#             median_finder.insert(int(parts[1]))
#         elif parts[0] == 'M':
#             print(median_finder.get_median())
#         elif parts[0] == 'R':
#             print(median_finder.remove_median())


# if __name__ == "__main__":
#     main()

# class MedianFinder:
#     def __init__(self):
#         self.max_heap = []
#         self.min_heap = []  
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
#         if not self.max_heap or x <= -self.max_heap[0]:
#             self.heap_push(self.max_heap, -x, True)  
#         else:
#             self.heap_push(self.min_heap, x, False)
#         self.balance()

#     def get_median(self):
#         return -self.max_heap[0] if self.max_heap else "Invalid"

#     def remove_median(self):
#         if not self.max_heap:
#             return "Invalid"
#         median = self.heap_pop(self.max_heap, True)
#         self.balance()
#         return -median

#     def balance(self):
#         if len(self.max_heap) > len(self.min_heap) + 1:
#             self.heap_push(self.min_heap, -self.heap_pop(self.max_heap, True), False)
#         elif len(self.min_heap) > len(self.max_heap):
#             self.heap_push(self.max_heap, -self.heap_pop(self.min_heap, False), True)


# def main():
#     median_finder = MedianFinder()

#     try:
#         q = int(input().strip())  
#     except ValueError:
#         return 
    

#     for _ in range(q):
#         try:
#             line = input().strip()
#             if not line:
#                 continue
#             command = line.split()
#             if command[0] == 'I':
#                 median_finder.insert(int(command[1]))
#             elif command[0] == 'M':
#                 print(median_finder.get_median())
#             elif command[0] == 'R':
#                 print(median_finder.remove_median())
#         except EOFError:
#             break  


# if __name__ == "__main__":
#     main()




class MedianFinder:
    def __init__(self):
        self.max_heap = []
        self.min_heap = [] 

    def _heap_push(self, heap, value, is_max):
        heap.append(value)
        i = len(heap) - 1
        while i > 0:
            parent = (i - 1) // 2
            if (is_max and heap[i] > heap[parent]) or (not is_max and heap[i] < heap[parent]):
                heap[i], heap[parent] = heap[parent], heap[i]
                i = parent
            else:
                break

    def _heap_pop(self, heap, is_max):
        if not heap:
            return None
        root = heap[0]
        heap[0] = heap[-1]
        heap.pop()
        i, n = 0, len(heap)
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            swap = i
            if left < n and ((is_max and heap[left] > heap[swap]) or (not is_max and heap[left] < heap[swap])):
                swap = left
            if right < n and ((is_max and heap[right] > heap[swap]) or (not is_max and heap[right] < heap[swap])):
                swap = right
            if swap == i:
                break
            heap[i], heap[swap] = heap[swap], heap[i]
            i = swap
        return root

    def insert(self, x):
        if not self.max_heap or x <= -self.max_heap[0]:
            self._heap_push(self.max_heap, -x, True) 
        else:
            self._heap_push(self.min_heap, x, False)  
        self._balance()

    def get_median(self):
        return -self.max_heap[0] if self.max_heap else "Invalid"

    def remove_median(self):
        if not self.max_heap:
            return "Invalid"
        median = self._heap_pop(self.max_heap, True)
        self._balance()
        return -median

    def _balance(self):
        if len(self.max_heap) > len(self.min_heap) + 1:
            self._heap_push(self.min_heap, -self._heap_pop(self.max_heap, True), False)
        elif len(self.min_heap) > len(self.max_heap):
            self._heap_push(self.max_heap, -self._heap_pop(self.min_heap, False), True)


def main():
    median_finder = MedianFinder()
    results = [] 

    try:
        while True:
            try:
                line = input().strip()
                if not line:
                    continue
                command = line.split()
                if command[0] == 'I':
                    median_finder.insert(int(command[1]))
                elif command[0] == 'M':
                    results.append(str(median_finder.get_median()))
                elif command[0] == 'R':
                    results.append(str(median_finder.remove_median()))
            except EOFError:
                break  
    except KeyboardInterrupt:
        pass  

    if results:
        print("\n".join(results))  

if __name__ == "__main__":
    main()
