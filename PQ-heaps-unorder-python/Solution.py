class BinaryHeapPriorityQueue:
    def __init__(self) -> None:
        self.pq_list=[]
        self._size=0

        
    def add(self, e):
        self.pq_list.append(e)
        self._size+=1

    def offer(self,e):
        self.add(e)
    def clear(self):
        self.pq_list=[]
        self._size=0
    def contains(self,o):
        if o in self.pq_list:
            return True
        else:
            return False
        
    def iterator(self):
        return sorted(self.pq_list)
    
    def peek(self):
        min=99999
        for i in self.pq_list:
            if i<min:
                min=i
        return min

    
    def poll(self):
        min=99999
        for i in self.pq_list:
            if i<min:
                min=i
        s = self.pq_list.index(min)
        a = self.pq_list[s]
        self.pq_list.remove(a)
        self._size-=1
        return a

    def remove(self,o):
        rm_ele=[]
        for i in self.pq_list:
            if i!=o:
                rm_ele.append(i)
                self.pq_list = rm_ele
                return True
        return False
        
    def size(self):
        return self._size
