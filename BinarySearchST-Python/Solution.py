class BinarySearchST:
    def __init__(self):
        self.key=[]
        self.value=[]
        self.length=0

    def isEmpty(self):
        return self.length==0
    
    def size(self):
        return self.length
    
    def selection_sort(self):
        for i in range(len(self.key)):
            min_idx = i
            for j in range(i+1, len(self.key)):
                if self.key[j] < self.key[min_idx]:
                    min_idx = j
            self.key[i], self.key[min_idx] = self.key[min_idx], self.key[i]
            self.value[i], self.value[min_idx] = self.value[min_idx], self.value[i]
    
    def binary_search(self,target):
        l=0
        r=self.length-1
        while l<=r:
            mid=(l+r)//2
            if self.key[mid]==target:
                return mid
            elif self.key[mid]>target:
                r=mid-1
            else:
                l=mid+1
        return None
    
    def put(self,key,val):
        if self.length==0:
            self.key.append(key)
            self.value.append(val)
            self.length+=1
            self.selection_sort()
        else:
            temp=self.binary_search(key)
            if temp is None:
                self.key.append(key)
                self.value.append(val)
                self.length+=1
                self.selection_sort()
            else:
                self.value[temp]=val

    def get(self,key):
        temp=self.binary_search(key)
        return self.value[temp]
    
    def contains(self,key):
        temp=self.binary_search(key)
        return temp!=None
    
    def delete(self,key):
        temp=self.binary_search(key)
        if temp!=None:
            self.key.pop(temp)
            self.value.pop(temp)
            self.length-=1
    
    def min(self):
        return self.key[0]
    
    def max(self):
        return self.key[self.length-1]
    
    def floor(self,key):
        temp=self.binary_search(key)
        return self.key[temp]
    
    def ceiling(self,key):
        temp=self.binary_search(key)
        return self.key[temp]
    
    def rank(self,key):
        temp=self.binary_search(key)
        return temp
    
    def select(self,idx):
        return self.key[idx]
    
    def deleteMin(self):
        self.key.pop(0)
        self.value.pop(0)
        self.length-=1

    def deleteMax(self):
        self.key.pop(self.length-1)
        self.value.pop(self.length-1)
        self.length-=1

    def size_range(self,key1,key2):
        idx1=self.binary_search(key1)
        idx2=self.binary_search(key2)
        temp=self.key[idx1:idx2+1]
        return len(temp)
    
    def keys_all(self):
        return self.key
    
    def keys_range(self,key1,key2):
        idx1=self.binary_search(key1)
        idx2=self.binary_search(key2)
        return self.key[idx1:idx2+1]