class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.next=None
        self.prev=None

class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self._size = 0
    
    def add_to_front(self,value):
        new_node =Node(value)
        new_node.next=self.head
        if self.head is not None:
            self.head.prev = new_node 
        self.head =new_node

        if self.tail is None:
            self.tail = new_node
        self._size+=1
    def add_to_end(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head=self.tail=new_node
        else:
            self.tail.next=new_node
            new_node.prev = self.tail
            self.tail=new_node
        self._size+=1
    def remove_from_front(self):
        if self.head is None:
            return None
        removed_data=self.head.value
        self.head = self.head.next
        # self.head.prev = None
        # self.head =self.head.next
        if self.head is None:
            self.tail = None
        else:
            self.head.prev = None
        self._size-=1
        return removed_data
    
    def remove_from_end(self):
        if self.head is None:
            return None
        removed_data=self.tail.value
        if self.head==self.tail:
            self.head = self.tail =None
        else:
            self.tail=self.tail.prev
            self.tail.next = None
        self._size -= 1
        return removed_data
    def check_empty(self):  
        return self._size == 0
    def clear_list(self):
        self.head = self.tail = None
        self._size = 0
    def get_size(self):
        return self._size
    def get_at(self,ind):
        # print(ind)
        if ind <0 or ind >=self._size:
            return None
        current =self.head
        # print("hi")
        for i in range(ind):
            current =current.next
        # print(current.data)
        return current.value
    
    def get_node_at(self,ind):
        # print(ind)
        if ind <0 or ind >=self._size:
            return None
        current =self.head
        # print("hi")
        for i in range(ind):
            current =current.next
        # print(current.data)
        return current.value

    def find(self,s):
        curr=self.head
        while curr:
            if curr.value==s:
                return True
            curr=curr.next
        return False
    def insert_at(self,i,value):
        
        if i < 0 or i > self._size:
            return
        if  i == 0:
            self.add_to_front(value)
            return
        if i == self._size:
            self.add_to_end(value)
            return
        new_node = Node(value)
        c = self.head
        for i in range(i-1):
            c = c.next
        c.next.prev = new_node
        new_node.prev = c
        new_node.next = c.next
        c.next = new_node
        self._size+=1
    # def get_at(self):
    def remove_at(self,indx):
        
        if indx==0:
            self.remove_from_front()
        if indx ==self._size:
            self.remove_from_end()
        
        current=self.head
            
        for i in range(indx): 
            current = current.next

        removed_data = current.value
        # current.prev.next = current.next
        if current.prev:
            current.prev.next = current.next
        
        if current.next:
            current.next.prev = current.prev
        
        self._size -= 1
        return removed_data
    def reverse_traversal(self):
        if self.tail is None:
            print("DoublyLinkedList is empty")
        curr=self.tail
        re=[]
        # while curr:
        #     re.append(f"({curr.value})")
        #     curr=curr.prev
        # print("<->".join(re))

        for i in range(self._size):
            print(curr.value, end=" ")
            curr = curr.prev
        print()
    
    def print_list(self):
        if self.head is None:
            print("DoublyLinkedList is empty")
        curr=self.head
        re=[]
        # while curr:
        #     re.append(f"{curr.value}")
        #     curr=curr.prev
        # print("<->".join(re))
        for i in range(self._size):
            print(curr.value, end=" ")
            curr = curr.next
        print()

    def swap_nodes(self, index1, index2):
        if index1 == index2:
            return
        node1 = self.get_node_at(index1)
        node2 = self.get_node_at(index2)
        if node1 == None or node2 == None:
            return
        
        self.insert_at(index1,node2)
        self.remove_at(index1+1)
        self.insert_at(index2,node1)
        self.remove_at(index2+1)
        
            
    def __str__(self) -> str:
        if self.head is None:
            print("DoublyLinkedList is empty")
        curr=self.head
        re=[]
        while curr:
            re.append(f"({curr.value})")
            curr=curr.prev
        return ("<->".join(re))



        
        
    def detect_cycle(self):
        slow=self.head
        fast=self.head
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
            if slow ==fast:
                return True
        return False



    
    

    