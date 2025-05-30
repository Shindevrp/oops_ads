import re
class MyString:
    def __init__(self,*args):
        self.s = ""
        if len(args) == 0:
            self.s = ""
        elif type(args[0]) == list:
            for i in args[0]:
                
                self.s += i
            
        elif type(args[0]) == MyString:
           
            self.s = args[0]
    
    def length(self):
        c = 0
        for i in self.s:
            c+=1
        return c
    
    def String(self,v):
        for i in v:
            print(i)
            self.s += i
        return self.s
    
    def char_at(self,index):
        return self.s[index]
    
    def substring(self,*args):
        if len(args) == 2:
            k1 = self.s[args[0]:args[1]]
            k = "".join(k1)
            return k
        elif len(args) == 1:
            k1 =self.s[args[0]:]
    
            return k1
        
    def compare_to(self, str1):
        if isinstance(str1, MyString):
            return (self.to_lower_case() > str1.to_lower_case()) - (self.to_lower_case() < str1.to_lower_case())
        return None

    
    def compare_to_ignore_case(self, str1):
        if isinstance(str1, MyString):
            return (self.to_lower_case() > str1.to_lower_case()) - (self.to_lower_case() < str1.to_lower_case())
        return None
    
    def equals_ignore_case(self, str1):
        if isinstance(str1, MyString):
            return self.to_upper_case() == str1.to_upper_case()
        return False
    
    def concat(self,str1):
        if isinstance(str1, MyString):
            return self.s + str1.s
        
    def replace(self, old_char, new_char):
        result = []
        for char in self.s:
            if char == old_char:
                result.append(new_char)
            else:
                result.append(char)
       
        return ''.join(result)
    
    def replace_seq(self, target:'MyString' , replacement:'MyString'):
        target_str = target.s
        replacement_str = replacement.s
        res = ""
        i = 0
        
        while i < self.length():
            if (self.substring(i,i + target.length()) == target_str):
                res += replacement_str
                i += target.length()
            else:
                res += self.s[i]
                i += 1
       
        return res
    
    def replace_all(self, regex, replacement:'MyString'):
        new_string = re.sub(regex, replacement.s, self.s)
       
        
        return new_string
    
    def replace_first(self, regex, replacement:'MyString'):
        new_string = re.sub(regex, replacement.s, self.s, count=1)
        
        return (new_string)
    

    def contains(self, s):
     
        return s.s in self.s
    
    def index_of(self, sub: 'MyString'):
        return self.index_of_from(sub, 0)
    
    def index_of_from(self, sub: 'MyString', idx: int):
        sub_str = sub.s if isinstance(sub, MyString) else str(sub)
        index = self.s.find(sub_str, idx)
        if index != -1:
            return index
        else:
            return -1
    
    def last_index_of_from(self, sub: 'MyString', idx: int):
        sub_str = sub.s if isinstance(sub, MyString) else str(sub)
        index = self.s.rfind(sub_str, 0, idx + 1)
        if index != -1:
            return index
        else:
            return -1

    def last_index_of(self, sub: 'MyString'):
        return self.last_index_of_from(sub, self.length() - 1)
    
    def is_empty(self):
        return len(self.s) == 0
    
    def to_char_array(self):
        l = []
        for i in self.s:
            l.append(i)
        return l
    
    def to_lower_case(self):
        res = ""
        for i in self.s:
            if (ord(i)) >= 65 and (ord(i)) <=90:
                diff = chr(ord(i) + 32)
                res+=diff
            else:
                res+=i
            
        return res
    
    def to_upper_case(self):
        res = ""
        for i in self.s:
            if (ord(i)) >= 97 and (ord(i)) <=122:
                diff = chr(ord(i) - 32)
                res+=diff
            else:
                res+=i
            
        return res  
    
    def trim(self):
        start = 0
        end = len(self.s) - 1
        
        while start <= end and self.s[start] == ' ':
            start += 1
        
        while end >= start and self.s[end] == ' ':
            end -= 1
        
        return self.s[start:end + 1]


    def starts_with_from(self, other:'MyString', idx):
        n = other.length()
        return self.s[idx:idx + n] == other.s
    
    def starts_with(self,other):
        return self.starts_with_from(other,0)
    
    def split(self, delimiter: 'MyString'):
        delimiter_str = ""

        if isinstance(delimiter, MyString):
            delimiter_str = delimiter.s  
        else: 
            delimiter_str = str(delimiter)
        k = []

        for i in self.s:
            if i == delimiter_str:
                continue
            k.append(i)
        
        return k

    def split_limit(self, delimiter: 'MyString', limit: int):
        
        delimiter_str = ""

        if isinstance(delimiter, MyString):
            delimiter_str = delimiter.s  
        else: 
            delimiter_str = str(delimiter)

        k = self.s.split(delimiter_str)

        res = k[:limit-1]

        a = ""

        for i in range(limit - 1, len(k)):
            if i > limit - 1:
                a += ","
            a += k[i]

        res.append(a)

        return res

    
    
    def __str__(self):
        return f"{self.s}"