class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None
        self.size = 1


class BST:
    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    def size(self):
        return self._size(self.root)

    def _size(self, node):
        if node is None:
            return 0
        return node.size

    def put(self, key, val):
        def insert(node, key, val):
            if node is None:
                return Node(key, val)
            if key < node.key:
                node.left = insert(node.left, key, val)
            elif key > node.key:
                node.right = insert(node.right, key, val)
            else:
                node.val = val
            node.size = 1 + self._size(node.left) + self._size(node.right)
            return node

        self.root = insert(self.root, key, val)

    def get(self, key):
        node = self.root
        while node is not None:
            if key < node.key:
                node = node.left
            elif key > node.key:
                node = node.right
            else:
                return node.val
        return None

    def contains(self, key):
        return self.get(key) is not None

    def min(self):
        if self.is_empty():
            raise ValueError("Tree is empty")
        node = self.root
        while node.left is not None:
            node = node.left
        return node.key

    def max(self):
        if self.is_empty():
            raise ValueError("Tree is empty")
        node = self.root
        while node.right is not None:
            node = node.right
        return node.key

    def floor(self, key):
        def floor_node(node, key):
            if node is None:
                return None
            if key == node.key:
                return node
            if key < node.key:
                return floor_node(node.left, key)
            temp = floor_node(node.right, key)
            return temp if temp else node

        node = floor_node(self.root, key)
        if node:
            return node.key
        raise ValueError("No floor found")

    def floor2(self, key):
        x = self.root
        res = None
        while x is not None:
            if key == x.key:
                return x.key
            elif key < x.key:
                x = x.left
            else:
                res = x.key
                x = x.right
        if res is not None:
            return res
        raise ValueError("No floor found")

    def ceiling(self, key):
        x = self.root
        res = None
        while x is not None:
            if key == x.key:
                return x.key
            elif key > x.key:
                x = x.right
            else:
                res = x.key
                x = x.left
        if res is not None:
            return res
        raise ValueError("No ceiling found")

    def select(self, k):
        def select_node(node, k):
            if node is None:
                return None
            t = self._size(node.left)
            if t > k:
                return select_node(node.left, k)
            elif t < k:
                return select_node(node.right, k - t - 1)
            else:
                return node

        node = select_node(self.root, k)
        if node:
            return node.key
        raise ValueError("Rank out of bounds")

    def rank(self, key):
        def rank_node(node, key):
            if node is None:
                return 0
            if key < node.key:
                return rank_node(node.left, key)
            elif key > node.key:
                return 1 + self._size(node.left) + rank_node(node.right, key)
            else:
                return self._size(node.left)

        return rank_node(self.root, key)

    def keys(self, lo=None, hi=None):
        res = []

        def inorder(node):
            if node is None:
                return
            if lo is None or node.key >= lo:
                inorder(node.left)
            if (lo is None or node.key >= lo) and (hi is None or node.key <= hi):
                res.append(node.key)
            if hi is None or node.key <= hi:
                inorder(node.right)

        inorder(self.root)
        return res

    def size_range(self, lo, hi):
        c = 0
        keys = self.keys(lo, hi)
        for _ in keys:
            c += 1
        return c

    def height(self):
        def get_height(node):
            if node is None:
                return -1
            return 1 + max(get_height(node.left), get_height(node.right))

        return get_height(self.root)

    def level_order(self):
        if self.root is None:
            return []
        res = []
        queue = [self.root]
        while len(queue) > 0:
            curr = queue.pop(0)
            res.append(curr.key)
            if curr.left is not None:
                queue.append(curr.left)
            if curr.right is not None:
                queue.append(curr.right)
        return res

    def delete_min(self):
        def delete_min_node(node):
            if node.left is None:
                return node.right
            node.left = delete_min_node(node.left)
            node.size = 1 + self._size(node.left) + self._size(node.right)
            return node

        if self.is_empty():
            raise ValueError("Tree is empty")
        self.root = delete_min_node(self.root)

    def delete_max(self):
        def delete_max_node(node):
            if node.right is None:
                return node.left
            node.right = delete_max_node(node.right)
            node.size = 1 + self._size(node.left) + self._size(node.right)
            return node

        if self.is_empty():
            raise ValueError("Tree is empty")
        self.root = delete_max_node(self.root)

    def delete(self, key):
        def delete_node(node, key):
            if node is None:
                return None
            if key < node.key:
                node.left = delete_node(node.left, key)
            elif key > node.key:
                node.right = delete_node(node.right, key)
            else:
                if node.left is None:
                    return node.right
                if node.right is None:
                    return node.left
                temp = node
                node = self._min_node(temp.right)
                node.right = self._delete_min(temp.right)
                node.left = temp.left
            node.size = 1 + self._size(node.left) + self._size(node.right)
            return node

        self.root = delete_node(self.root, key)

    def _delete_min(self, node):
        if node.left is None:
            return node.right
        node.left = self._delete_min(node.left)
        node.size = 1 + self._size(node.left) + self._size(node.right)
        return node

    def _min_node(self, node):
        while node.left is not None:
            node = node.left
        return node
