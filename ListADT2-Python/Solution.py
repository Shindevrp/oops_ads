class ArrayListADT:
    def __init__(self) -> None:
        self.data = []
        self.size = 0

    def add(self, e):
        self.data.append(e)
        self.size += 1

    def add_at(self, index, element):

        if index == self.size:
            self.data.append(element)
        else:
            self.data.append(None)
            for i in range(self.size, index, -1):
                self.data[i] = self.data[i - 1]
            self.data[index] = element
        self.size += 1

    def add_all(self, c):
        for i in c:
            self.data.append(i)

    def add_all_at(self,index,ele):
        j = index
        for i in ele:
            self.add_at(j,i)
            j+=1
        


    def contains(self, o):
        for i in self.data:
            if i == o:
                return True
        return False

    def ensure_capacity(self, minCapacity):
        if minCapacity > len(self.data):
            while len(self.data) < minCapacity:
                self.data.append(None)

    def get(self, index):
        re=[]
        for i in self.data:
            if i != None:
                re.append(i)
        self.data=re
        self.size=len(re)
        return self.data[index]
    
    def index_of(self,ele):
        for i in range(len(self.data)):
            if self.data[i]==ele:
                return i
        return -1
    def last_index_of(self,ele):
        for i in range(len(self.data)-1,0,-1):
            if self.data[i]==ele:
                return i
        return -1
        


    def is_empty(self):
        return len(self.data)==0
    def size_(self):
        return len(self.data)

    def remove_at(self,index):
        re=[]
        a=self.data[index]
        for i in range(len(self.data)):
            if i!=index:
                re.append(self.data[i])
        self.data=re
        self.size=len(self.data)
        return a
    def remove(self,ele):
        re=[]
        for i in self.data:
            if i!=ele:
                re.append(i)
        self.data=re
        self.size=len(self.data)
        return True

    def set(self,index, ele):
        
        a=self.data[index]
        for i in range(len(self.data)):
            if i==index:
                self.data[index]=ele
                return a

    def trim_to_size(self):
        return len(self.data)

    
    def clear(self):
        self.data = []
        self.size =0

    def __str__(self) -> str:
        return "[" + ", ".join(str(e) for e in self.data) + "]"