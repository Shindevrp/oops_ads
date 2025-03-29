class MedianFinder:
    
    def __init__(self):

        self.data = []


    def insert(self,x):

        self.data +=[x]
        self.data =self.merge_sort(self.data)

    def merge_sort(self,arr):

        if len(arr)<= 1:
            return arr
        mid = len(arr)// 2

        left =self.merge_sort(arr[:mid])
        right= self.merge_sort(arr[mid:])
        return self.merge(left,right)
    

    def merge(self, left, right):

        merged =[]
        i, j = 0, 0


        while i<len(left) and j<len(right):
            if left[i] <= right[j]:
                merged +=[left[i]]
                i += 1
            else:
                merged +=[right[j]]
                j += 1

        while i <len(left):
            merged +=[left[i]]
            i += 1
        while j < len(right):
            merged +=[right[j]]
            j +=1
        return merged
    
    def get_median(self):
        n = 0
        for _ in self.data:
            n +=1
        if n ==0:
            return "Invalid"
        

        mid = (n - 1)// 2
        return self.data[mid]
    
    def remove_median(self):
        n = 0
        for _ in self.data:
            n += 1
        if n == 0:
            return "Invalid"
        

        mid = (n - 1) // 2
        med =self.data[mid]
        new_data =[]
        i =0

        while i <n:
            if i !=mid:
                new_data +=[self.data[i]]
            i += 1
        self.data =new_data
        return med

def main():
    
    results =[]


    while True:
        try:
            ip = input().strip()
        except EOFError:
            break

        if ip == "":
            continue

        s = ip.split()
        if s[0] == "I":
            mf.insert(int(s[1]))
        elif s[0] == "M":
            results += [str(mf.get_median())]
        elif s[0] == "R":
            results += [str(mf.remove_median())]


    if results:
        out = ""
        i = 0
        while i < len(results):
            out += results[i]
            if i != len(results) - 1:
                out += "\n"
            i += 1
        print(out)

if __name__ == "__main__":
    mf = MedianFinder()
    main()





