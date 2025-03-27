class Node:
    def __init__(self, key, value, next = None):
        self.key = key
        self.value = value
        self.next = next

class SequentialSearchST:
    def __init__(self):
        self.head = None
        self.size_ = 0

    def isEmpty(self):
        return self.size_ == 0
    
    def size(self):
        return self.size_
    

    def put(self, key, value):
        curr = self.head
        while curr:
            if curr.key == key:
                curr.value = value
                return
            curr = curr.next
        new_node = Node(key, value, self.head)
        self.head = new_node
        self.size_ += 1

    

    def get(self, key):
        curr = self.head
        while curr:
            if curr.key == key:
                return curr.value
            curr = curr.next
        return None
    
    def contains(self, key):
        return self.get(key) is not None
    
    def delete(self, key):
        if not self.head:
            return
        if self.head.key == key:
            self.head = self.head.next
            self.size_ -= 1
            return
        
        prevs, curr = None, self.head
        while curr:
            if curr.key == key:
                prevs.next = curr.next
                self.size_ -= 1
                return
            prevs, curr = curr, curr.next

    
    def min(self):
        if self.isEmpty():
            return None
        minimum = self.head.key
        curr = self.head.next
        while curr:
            if curr.key < minimum:
                minimum = curr.key
            curr = curr.next
        return minimum
    

    def max(self):
        if self.isEmpty():
            return None
        maximun = self.head.key
        curr = self.head.next
        while curr:
            if curr.key > maximun:
                maximun = curr.key
            curr = curr.next
        return maximun
    

    def floor(self, key):
        floor_key = None
        curr = self.head
        while curr:
            if curr.key <= key and (floor_key is None or curr.key > floor_key):
                floor_key = curr.key
            curr = curr.next
        return floor_key
    
    def ceiling(self, key):
        ceiling_key = None
        curr = self.head
        while curr:
            if curr.key >= key and (ceiling_key is None or curr.key < ceiling_key):
                ceiling_key = curr.key
            curr = curr.next
        return ceiling_key
    
    def rank(self, key):
        c = 0
        curr = self.head
        while curr:
            if curr.key < key:
                c += 1
            curr = curr.next
        return c
    
    def select(self, k):
        list_keys = self.keys()
        list_keys.sort()
        if 0 <= k < len(list_keys):
            return list_keys[k]
        return None
    
    def deleteMin(self):
        min_key = self.min()
        if min_key is not None:
            self.delete(min_key)
    
    def deleteMax(self):
        max_key = self.max()
        if max_key is not None:
            self.delete(max_key)
    
    def size_range(self, lo, hi):
        count = 0
        curr = self.head
        while curr:
            if lo <= curr.key <= hi:
                count += 1
            curr = curr.next
        return count
    
    def keys(self):
        keys_list = []
        curr = self.head
        while curr:
            keys_list.append(curr.key)
            curr = curr.next
        return keys_list
    
    def keys_range(self, lo, hi):
        keys_list = []
        curr = self.head
        while curr is not None:
            if lo <= curr.key <= hi:
                keys_list.append(curr.key)
            curr = curr.next
        
        keys_list.sort()
        return keys_list
