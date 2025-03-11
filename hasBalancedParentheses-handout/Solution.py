class ArrayListADT:
    def __init__(self) -> None:
        self.data = []
        self.size = 0

    def add(self, e):
        self.data.append(e)
        self.size += 1
        return e

    def contains(self, o):
        for i in self.data:
            if i == o:
                return True
        return False
    
    def index_of(self,ele):
        temp=1
        for i in range(len(self.data)-1,-1,-1):
            if self.data[i]==ele:
                return temp
            temp+=1
        return -1

    def is_empty(self):
        return self.size==0
    
    def size_(self):
        return len(self.data)
    def remove(self):
        temp=self.data[-1]
        self.data.pop(-1)
        self.size-=1
        return temp
    
    def get(self):
        return self.data[-1]

    
    def clear(self):
        self.data = []
        self.size =0

class Stack:
    def __init__(self) -> None:
 
        self.linked_list=ArrayListADT()
    
    def empty(self):
        return self.linked_list.is_empty()
    def peek(self):
        if self.linked_list.is_empty():
            raise IndexError
        return self.linked_list.get()
    def pop(self):
        if self.linked_list.is_empty():
            raise IndexError

        self.linked_list.remove()
    def push(self,ele):
        self.linked_list.add(ele)
    def search(self,ele):
        return self.linked_list.index_of(ele)
class Solution:
    def __init__(self) -> None:
        self.store=Stack()
    

    def inputread(self,s):
        for i in s:
            if i=="(":
                self.store.push(i)
            elif i==")":
                if self.store.empty():
                    return False
                self.store.pop()
        return self.store.empty()   
input=input()
re=Solution()
print(re.inputread(input))
