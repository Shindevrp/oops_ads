class Node:
    def __init__(self, data):
        self.data = data
        self.next =None
    
class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def is_empty(self):
        if self._size == 0:
            return 'true'
        return "false"

    def size(self):
        return self._size

    def add_first(self, item):
        if item is None:
            raise ValueError("Invalid argument: None")
        new_node = Node(item)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
           
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self._size += 1
        
        


    def add_last(self, item):
        new_node = Node(item)

        if self.head is None:
            self.head = new_node
            self.tail =new_node
        else:
            self.tail.next = new_node
            self.tail.prev = new_node
            self.tail = new_node
        self._size += 1


    def remove_first(self):
        if not self.head:
            return "Deque is empty"
        
        removed_data = self.head.data
        self.head = self.head.next
        self._size -= 1

        return removed_data

    
    def remove_last(self):
        if not self.head:
            return "Deque is empty"
        
        if self.head == self.tail:
            removed_data = self.head.data
            self.head = None
            self.tail = None
        else:
            cur = self.head
            while cur.next != self.tail:
                cur = cur.next
            removed_data = self.tail.data
            self.tail = cur
            self.tail.next = None

        self._size -= 1
        return removed_data
        
    


    def iterator(self):
        cur = self.head
        while cur:
            cur = cur.next
        return cur



    def __str__(self):
        if self._size == 0:
            return "Steque is empty"

        cur = self.head
        l = []
        while cur:
            l.append(f"{str(cur.data)}")
            cur = cur.next
        return ", ".join(l)

    




def main():
    deque = Deque()

    while True:
        try:
            s = input()
            if s == "":
                break

            s = s.split()

            if s[0] == 'isEmpty()':
                print(deque.is_empty())

            elif s[0] == 'Deque()':
                deque.__init__()

            elif s[0] == 'addLast()':
                (deque.add_last(s[1]))
                # print(s[1])

            elif s[0] == 'addFirst()':
                (deque.add_first(s[1]))
                # print(s[1])

            elif s[0] == 'removeFirst()':
                print(deque.remove_first())
                
            
            elif s[0] == 'removeLast()':
                print(deque.remove_last())

            elif s[0] == 'iterator()':
                print(deque.iterator())
            
            elif s[0] == 'toString()':
                print(deque.__str__())
            
            elif s[0] == "size()":
                print(deque.size())

        except:
            break


if __name__ == '__main__':
    # deque = Deque()
    main()






