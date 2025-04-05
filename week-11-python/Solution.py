# Define the Node class used by both BinaryTree and BinarySearchTree.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# BinaryTree with methods: levelOrder, isComplete, countLeaves, and pathSum.
class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    # 1. Level Order Traversal: returns list of lists of node values per hight.
    def levelOrder(self):

        if self.root is None:
            return []

        lst = []
        nodes = [self.root]

        while len(nodes) > 0:
            level_size = len(nodes)
            hight = []

            for i in range(level_size):
                node = nodes[0]
                nodes = nodes[1:]

                hight.append(node.val)

                if node.left is not None:
                    nodes.append(node.left)
                if node.right is not None:
                    nodes.append(node.right)

            lst.append(hight)

        return lst



    # 2. Check Completeness: returns True if the tree is complete.
    def isComplete(self):

        nodes= [self.root]
        empty= False

        if self.root is None:
            return True
        
        while len(nodes) > 0:
            node= nodes[0]
            nodes= nodes[1:]
            
            if node is None:
                empty= True
            else:
                if empty:
                    return False
                
                nodes.append(node.left)
                nodes.append(node.right)
        return True

    # 3. Count Leaf Nodes: returns the number of leaf nodes.
    def countLeaves(self):

        nodes = [self.root]

        if self.root is None:
            return 0
        
        c= 0
        while len(nodes) > 0:
            node = nodes.pop()
            if node.left is None and node.right is None:
                c += 1
            if node.right is not None:

                nodes.append(node.right)
            if node.left is not None:
                nodes.append(node.left)


        return c

    # 4. Root-to-Leaf Path Sum: returns True if a root-to-leaf path enodesuals target sum.
    def pathSum(self, target):
        nodes = [self.root]


        if self.root is None:
            return 0
        
        c= 0

        while len(nodes) > 0:
            node = nodes.pop()

            # if 





            
        return c
        

# BinarySearchTree (inherits from BinaryTree) with methods: validateBST, rangeSearch, balance.
class BinarySearchTree(BinaryTree):
    def __init__(self, root=None):
        super().__init__(root)

    # 5. Validate BST: returns True if the tree satisfies BST properties.
    def validateBST(self):
        lst = []  
        cur= self.root
        last =None  

        while True:
            while cur is not None:
                lst.append(cur)
                cur= cur.left

            if len(lst)== 0:
                break

            cur= lst.pop()
            if last is not None :
                if cur.val <=last:
                    return False

            last= cur.val
            cur =cur.right

        return True


    # 6. Range Search: returns a sorted list of node values within [low, high].
    def rangeSearch(self, low, high):
        lst = []
        nodes= [self.root]  

        i =0  
        while i < len(nodes):
            cur =nodes[i]
            i += 1

            if cur is None:
                continue

            
            if cur.val > low:
                nodes.append(cur.left)
            if low <= cur.val <=high:
                lst.append(cur.val)

            
            if cur.val <high:
                nodes.append(cur.right)

        return lst


    

    # 7. Balance BST: rebuilds the tree so that it is balanced.
    def balance(self):
   
        lst =[]
        nodes= []
        cur=self.root

        while True:

            while cur is not None:
                nodes.append(cur)
                cur =cur.left

            if len(nodes) ==0:
                break
            cur =nodes.pop()
            lst.append(cur)
            cur =cur.right

        
        def make_bal(l, r):
            if l <r:
                return None
            mid =(l + r) // 2
            root =lst[mid]
            root.left =make_bal(r, mid - 1)
            root.right =make_bal(mid + 1, r)
            return root

        self.root =make_bal(0, len(lst) - 1)




