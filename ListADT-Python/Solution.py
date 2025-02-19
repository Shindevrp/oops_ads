# class ArrayListADT:
#     def __init__(self) -> None:
#         self.data =[]
#         self.size = 0
#     def add(self, e):
#         # if e not in self.data:
#         self.data.append(e)

#     def add_at(self, index, element):
#         new_data = []  
#         self.size = len(self.data)
#         if index == self.size-1:
#             self.data.append(element)

#         else:
#             for i in range(len(self.data)):  
#                 if i == index:  
#                     new_data.append(element)
#                     new_data.append(self.data[i])
                    
#                 else:
#                     new_data.append(self.data[i])
#             for i in range(len(self.data), index):  
#                     new_data.append(self.data[i])  

#             self.data = new_data
#             # print(self.data)
#             # self.size += 1 
#         # new_data = []
#         # for i in range(self.size):  
#         #     if i == index:  
#         #         new_data.append(element)  # Insert at index
#         #     new_data.append(self.data[i])  # Copy old elements
#         # if index == self.size:  # Append if adding at the last index
#         #     new_data.append(element)
#         # self.data = new_data
#         # self.size += 1 


        
#     def addAll( self,index, c):
#         new_data = []
#         for i in range(index):  
#             new_data.append(self.data[i])  
#         for i in c:  
#             new_data.append(i)
#         for i in range(index, len(self.data)):  
#                 new_data.append(self.data[i])  
#         self.data = new_data 
        
#     def contains(self,o):
#         for i in self.data:
#             if i == o:
#                 return True
#         return False
#     def ensureCapacity(self, minCapacity):
#         if minCapacity > len(self.data):
#             while len(self.data) < minCapacity:
#                 self.data.append(None)
#     def get(self,index):
#        print(index)
#        print(len(self.data), self.data)
#        return self.data[index]

#     def clear(self):
#         # for i in self.data:
#         #     if i in self.data:
#         #         self.data.remove(i)
#         self.data = []
# #         self.size = 0

# #     def __str__(self) -> str:
# #         # return str(self.data)

# #         result = "["
# #         for i in range(len(self.data)):
# #             result += str(self.data[i])
# #             if i != len(self.data) - 1:
# #                 result += ", "
# #         result += "]"
# #         return result


# class ArrayListADT:
#     def __init__(self) -> None:
#         self.data = []
#         self.size = 0

#     def add(self, e):
#         self.data.append(e)
#         self.size += 1

#     def add_at(self, index, element):
#         if index < 0 or index > self.size:
#             print("Index out of bounds!")
#             return

#         if index == self.size:
#             self.data.append(element)
#         else:
#             self.data.append(None)
#             for i in range(self.size, index, -1):
#                 self.data[i] = self.data[i - 1]
#             self.data[index] = element
#         self.size += 1

#     def addAll(self, index, c):
#         if index < 0 or index > self.size:
#             print("Index out of bounds!")
#             return

#         for element in c:
#             self.add_at(index, element)
#             index += 1

#     def contains(self, o):
#         for i in self.data:
#             if i == o:
#                 return True
#         return False

#     def ensureCapacity(self, minCapacity):
#         if minCapacity > len(self.data):
#             while len(self.data) < minCapacity:
#                 self.data.append(None)

#     def get(self, index):
#         if index < 0 or index >= self.size:
#             print("Index out of bounds!")
#             return None
#         return self.data[index]

#     def clear(self):
#         self.data = []
#         self.size =0

#     def __str__(self) -> str:
#         return "[" + ", ".join(str(e) for e in self.data) + "]"















def digitsum(s,k):
    s1=s//k
    print(s1)

print(digitsum(input(),input()))