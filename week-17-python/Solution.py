import sys


def to_read_file(file_path):
    """
    Read a file and return all whitespace-separated tokens as a list of strings.
    """
    with open(file_path, 'r') as f:
        return f.read().split()


def load_dictionary(file_path):
    """
    Build a frequency dictionary from the words in the given file. Make sure to lower the words
    Returns a dict mapping word -> count.
    """
    w=to_read_file(file_path)
    d={}
    for i in range(len(w)):
        x= w[i].lower()
        if x in d:
            d[x]=d[x]+1
        else:
            d[x] = 1

    return d
class T9:
    """
    Basic T9 predictive text implementation.
    """
    t9_map = {
        '2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno','7':"pqrs",
        '8':'tuv','9':'wxyz'
    }


    def __init__(self, dictionary):
        """
        Initialize with a word-frequency dict (word -> frequency).
        """
        self.dictionary = dictionary
        self.l= []
        for k in dictionary:
            self.l.append(k)



    def get_all_words(self, prefix):
        """
        Return all dictionary words that start with the given prefix, sorted lexicographically.
        """
        r=[]
        for i in range(len(self.l)):
            words = self.l[i]
            if words.startswith(prefix):
                r.append(words)
        r.sort()
        return r



    def potential_words(self, signature):
        """
        Enumerate all valid dictionary words matching the T9 numeric signature.
        """
        g =[]
        for i in range(len(signature)):
            x=signature[i]
            if x in T9.t9_map:
                g.append(T9.t9_map[x])
            else:
                g.append("")

        r = []
        self._generate_words(g,0,"", r)

        v=[]
        for i in range(len(r)):
            if r[i] in self.dictionary:
                v.append(r[i])
        v.sort()
        return v
    def _generate_words(self,g,i,c,o):
        if i== len(g):
            o.append(c)
            return
        grp=g[i]
        for j in range(len(grp)):
            ch =grp[j]
            self._generate_words(g,i+1,c+ch,o)

    


    def get_suggestions(self, words, k):
        """
        From an iterable of words, return the top-k suggestions by frequency (desc),
        then by word length (asc), then lex order.
        """
        a =[]
        for i in range(len(words)):
            x=words[i]
            f=self.dictionary[x]
            a.append((x,f))
        for i in range(len(a)):
            for j in range(i+1,len(a)):
                w1,f1=a[i]
                w2,f2 =a[j]

                if f1<f2:
                    a[i],a[j]=a[j],a[i]
                elif f1 ==f2:
                    if len(w1) > len(w2):
                        a[i],a[j]=a[j],a[i]
                    elif len(w1) == len(w2):
                        if w1 >w2:
                            a[i],a[j]=a[j],a[i]
        r =[]
        c = 0
        for i in range(len(a)):
            if c<k:
                r.append(a[i][0])
                c=c+1
        return r 
                      



    def t9(self, signature, k):
        """
        Combined method: get top-k suggestions for the given numeric signature.
        """
        p= self.potential_words(signature)
        return self.get_suggestions(p,k)




def main():
    dict_path = "./Files/t9.csv"
    # Read operation
    case = sys.stdin.readline().strip()
    if not case:
        return

    if case == "loadDictionary":
        st = load_dictionary(dict_path)
        # For each key in remaining input, print frequency
        for line in sys.stdin:
            key = line.strip()
            if key:
                print(st.get(key))

    elif case == "getAllPrefixes":
        t9 = T9(load_dictionary(dict_path))
        # For each prefix, list all matching words
        for line in sys.stdin:
            prefix = line.strip()
            if prefix:
                for word in t9.get_all_words(prefix):
                    print(word)

    elif case == "potentialWords":
        t9 = T9(load_dictionary(dict_path))
        count = 0
        # For each numeric signature, list all potential words
        for line in sys.stdin:
            signature = line.strip()
            if signature:
                for word in t9.potential_words(signature):
                    count += 1
                    print(word)
        if count == 0:
            print("No valid words found.")

    elif case == "topK":
        t9 = T9(load_dictionary(dict_path))
        # First line is k
        k_line = sys.stdin.readline().strip()
        if not k_line:
            return
        k = int(k_line)
        # Remaining lines are words to consider
        words = [line.strip() for line in sys.stdin if line.strip()]
        for word in t9.get_suggestions(words, k):
            print(word)

    elif case == "t9Signature":
        t9 = T9(load_dictionary(dict_path))
        # First line is k
        k_line = sys.stdin.readline().strip()
        if not k_line:
            return
        k = int(k_line)
        # Remaining lines are numeric signatures
        for line in sys.stdin:
            signature = line.strip()
            if signature:
                for word in t9.t9(signature, k):
                    print(word)

if __name__ == "__main__":
    main()

