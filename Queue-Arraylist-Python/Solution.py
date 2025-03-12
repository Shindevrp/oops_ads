class ArrayListADT:
    def __init__(self):
        self.data = []
        self.size = 0
                
    def add(self, num):
            self.data = self.data + [num]
            self.size+=1
            return num
        
    def add_at(self, index, c):  
        index = int(index)  
        
    
    def add_all_at(self,index,col):
        for i in range(len(col)):
            self.add_at(index + i, col[i])
        return True
    
    def add_all(self,c):
        for i in c:
            self.data.append(i)
        self.size = self.size_()
        return self.data

    def contains(self,o):
        for i in self.data:
            if i == o:
                return True
        return False 

    def index_of(self,o):
        for i in range(len(self.data)):
            if self.data[i] == o:
                return i
        return -1

    def get(self,index):
       
        l = []
        for i in self.data:
            if i != None:
                l.append(i)
    
        self.size = len(l)
        self.data = l
        return l[index]
    
    def last_index_of(self,o):
    
        l = []
        for i in range(len(self.data)):
            if self.data[i] == o:
                l.append(i)
        return l[-1]
    
    def is_empty(self):
        return len(self.data) == 0
    
    def size_(self):
        return len(self.data)
    
    def remove_at(self, index):
        l = []
        a = self.data[index]
        for i in range(len(self.data)):
            if i != index:
                l.append(self.data[i])
        self.data = l
        self.size = self.size_()
        return a            
    
    def remove(self,o):
        a = self.data.index(o)
        self.remove_at(a)
        self.size = self.size_()
        return True

            
    def set(self,index,e):
        for i in range(len(self.data)):
            if i == index:
                a = self.data[i]
                self.data[index] = e
        return a
                
    def trim_to_size(self):
        return self.data


    def clear(self):
        self.data = []
        self.size = 0
    
    def ensure_capacity(self, cap):
        self.add_all_at(len(self.data),[None]*cap)

    def __getitem__(self, index):
        return self.data[index]


    def __str__(self):
        return f"{self.data}"


class FullQueueException(Exception):
    def __init__(self, message="Queue is full"):
        super().__init__(message)


class MyQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = ArrayListADT()
        self.front = 0
        self.back = 0
        self.size = 0

    def peek(self):
        if self.size == 0:
            return None
        return self.queue[self.front]

    def poll(self):
        if self.size == 0:
            return None
        element = self.queue[self.front]
        self.remove()
        return element

    def element(self):
        if self.size == 0:
            raise IndexError("Empty Queue")
        return self.queue[self.front]

    def remove(self):
        if self.size == 0:
            raise IndexError("Empty Queue")
        element = self.queue[self.front]
        self.front +=1
        self.size -= 1
        return element

    def add(self, element):
        if self.size == self.capacity:
            raise FullQueueException("Empty Queue")
        self.queue.add(element)
        self.back+=1
        self.size += 1
        return True

    def offer(self, element):
        if self.size == self.capacity:
            return False
        self.queue.add(element)
        self.size+=1
        return True

    def __str__(self):
        return f"{self.queue[:self.size]}"