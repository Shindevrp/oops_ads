class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None
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
        

    def add_first(self, s):
        new_node = Node(s)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
        return s
    
    def contains(self, s):
        current = self.head
        while current:
            if current.data == s:
                return True
            current = current.next
        return False

    def get_first(self):
        return None if self.head is None else self.head.data

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

    def find_middle(self):
        
        if not self.head:
            return None
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data

    def nth_from_end(self, n):
        if n <= 0 or n > self.size:
            return None
        main = ref = self.head
        for _ in range(n):
            if not ref:
                return None
            ref = ref.next
        while ref:
            main = main.next
            ref = ref.next
        return main.data

    def insert_at_position(self, index, s):
        
        if index > self.size or index < 0:
            return None
        new_node = Node(s)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
        self.size += 1

    def insert_before(self, target, s):
        if not self.head:
            return
        if self.head.data == target:
            self.add_first(s)
            return
        current = self.head
        while current.next and current.next.data != target:
            current = current.next
        if current.next:
            new_node = Node(s)
            new_node.next = current.next
            current.next = new_node
            self.size += 1

    def delete_after(self, target):
        current = self.head
        while current and current.data != target:
            current = current.next
        if current and current.next:
            current.next = current.next.next
            self.size -= 1

    def to_string(self):
        if self.size == 0:
            return "LinkedList is empty"
        result = []
        current = self.head
        while current:
            result.append(f"[{current.data}]")
            current = current.next
        return "".join(result)
class Stack:
    def __init__(self) -> None:
        self.stack=MyLinkedList()

    def empty(self):
        return self.stack.is_empty()
    def peek(self):
        if self.stack.is_empty():
            raise IndexError
        return self.stack.get()
    def pop(self):
        if self.stack.is_empty():
            raise IndexError

        return self.stack.remove()
    def push(self,ele):
        self.stack.add(ele)
        return ele
    def search(self,ele):
        return self.stack.index_of(ele)