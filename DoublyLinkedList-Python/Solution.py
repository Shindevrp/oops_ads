class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.next=None
        self.prev=None

class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self._size = 0
    
    def add(self,s):
        new_node = Node(s)
        if self.head is None:
            self.head=self.tail=new_node
        else:
            self.tail.next=new_node
            new_node.prev = self.tail
            self.tail=new_node
        self._size+=1
    
    def add_first(self,s):
        new_node =Node(s)
        new_node.next=self.head
        self.head =new_node
        if self.tail is None:
            self.tail = new_node
        self._size+=1
    
    def contains(self,s):
        curr=self.head
        while curr:
            if curr.data==s:
                return True
            curr=curr.next
        return False
    def get_first(self):
        if self.head is None:
            return None
        else:
            return self.head.data
    
    def get_last(self):
        if self.tail is None:
            return None
        else:
            return self.tail.data
        
    def size(self):
        return self._size

    def remove(self):
        if self.head is None:
            return None
        removed_data=self.head.data
        self.head.prev = None
        self.head =self.head.next
        if self.head is None:
            self.tail = None
        self._size-=1
        return removed_data
    def remove_last(self):
        if self.head is None:
            return None
        if self.head==self.tail:
            removed_data=self.head.data
            self.head = self.tail =None
            self._size = 0  
            return removed_data
        current = self.tail
        self.tail=self.tail.prev
        self.tail.next = None

        # while current.next != self.tail:
        #     current = current.next
        # removed_data = self.tail.data
        # current.next = None
        # self.tail = current
        self._size -= 1

        
        return current.data
    def get(self,ind):
        # print(ind)
        if ind <0 or ind >=self._size:
            return None
        current =self.head
        # print("hi")
        for i in range(ind):
            current =current.next
        # print(current.data)
        return current.data
    def clear(self):
        self.head = self.tail = None
        self._size = 0
    def __str__(self) -> str:
        if self.head is None:
            return "DoublyLinkedList is empty"
        result = []
        current = self.head
        while current:
            result.append(f"[{current.data}]")
            current = current.next
        # print("<->".join(result))
        return "<->".join(result)

    