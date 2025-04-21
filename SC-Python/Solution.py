class SeparateChainingHashST:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self._size = 0
        self.table = [[] for _ in range(self.capacity)]

    def _hash(self, key):
        return hash(key) % self.capacity

    def put(self, key, value):
        indx = self._hash(key)
        for i in self.table[indx]:
            if i[0] == key:
                i[1] = value
                return
        self.table[indx].append([key, value])
        self._size += 1

    def get(self, key):
        indx = self._hash(key)
        for i in self.table[indx]:
            if i[0] == key:
                return i[1]
        return None

    def is_empty(self):
        return self._size == 0

    def size(self):
        return self._size
    
    def contains(self,item):
        indx = self._hash(item)
        for i in self.table[indx]:
            if i[0] == item:
                return True
        return False
    
    def delete(self, item):
        indx = self._hash(item)
        c = self.table[indx]
        for i in range(len(c)):
            if c[i][0] == item:
                del c[i]
                self._size -= 1
                return
    
    def keys(self):
        list2 =[]
        for i in self.table:
            for j in i:
                list2.append(j[0]) 
        return list2


    def __str__(self):
        return str(self.table)
