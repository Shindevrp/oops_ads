class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def add(self, s):
      
        new_node = Node(s)
        if self.head is None:
            self.head = new_node
            self.size+=1
            return s
        temp=self.head
        self.head=new_node
        self.head.next=temp
        self.size+=1
        return s
    def add_last(self, s):
        new_node = Node(s)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
        return True
        

    def add_first(self, s):
        new_node = Node(s)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
        return s
    
   

    
    def get_first(self):
        if self.head is None:
            raise IndexError("Queue is empty")
        return self.head.data

    def get(self):
        if self.head is None:
            raise IndexError
        return self.head.data 
    
    def index_of(self,ele):
        temp=self.head
        for i in range(self.size):
            if temp.data==ele:
                return i+1
            temp =temp.next

        return -1
    def is_empty(self):
        return self.size==0
    

    def remove(self):
        
        if self.head is None:
            return None
        removed_data = self.head.data
        self.head = self.head.next
        self.size -= 1
        return removed_data

    def remove_last(self):
        if self.head is None:
            return None
        if self.head.next is None:  
            removed_data = self.head.data
            self.head = None
            self.size = 0
            return removed_data
        current = self.head
        while current.next.next:  
            current = current.next
        removed_data = current.next.data
        current.next = None  
        self.size -= 1
        return removed_data

    def clear(self):
        
        self.head = None
        self.size = 0

    def remove_first(self):
        if self.head is None:
            raise IndexError("Queue is empty")
        removed_data = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None  
        self.size -= 1
        return removed_data
    
    def is_empty(self):
        return self.size == 0
    
    def get_size(self):
        return self.size

class FullQueueException(Exception):
    pass

    

     
class MyQueue:
    def __init__(self, capacity=float("inf")):
        self.list = MyLinkedList()
        self.capacity = capacity
    
    def add(self, e):
        if self.list.get_size() >= self.capacity:
            raise FullQueueException("Queue is full")
        return self.list.add_last(e)
    
    def offer(self, e):
        if self.list.get_size() >= self.capacity:
            return False
        return self.list.add_last(e)
    
    def element(self):
        return self.list.get_first()
    
    def peek(self):
        if self.list.is_empty():
            return None
        return self.list.get_first()

    def poll(self):
        if self.list.is_empty():
            return None
        return self.list.remove_first()

    def remove(self):
        return self.list.remove_first()
    
    def is_empty(self):
        return self.list.is_empty()
