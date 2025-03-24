class BinaryHeapPriorityQueue:
    def __init__(self) -> None:
        self.pq_list=[]
        self._size=0

        
    def add(self, e):
        self.pq_list.append(e)
        self._size+=1
        self.pq_list=sorted(self.pq_list)
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
        return self.pq_list
    def peek(self):
        return self.pq_list[0]
    def poll(self):
        s=self.pq_list[0]
        self.pq_list.remove(s)
        self._size-=1
        return s

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
