class Node:
    """Represents a node in the Binary Search Tree."""
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    """A Binary Search Tree implementation."""
    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    def add(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            curr = self.root
            while True:
                if data < curr.data:
                    if curr.left is None:
                        curr.left = Node(data)
                        break
                    else:
                        curr = curr.left
                elif data > curr.data:
                    if curr.right is None:
                        curr.right = Node(data)
                        break
                    else:
                        curr = curr.right
                else:
                    break

    def contains(self, data):
        curr = self.root
        for _ in range(1000):
            if curr is None:
                return False
            if data == curr.data:
                return True
            elif data < curr.data:
                curr = curr.left
            else:
                curr = curr.right
        return False

    def max(self):
        if self.root is None:
            return None
        curr = self.root
        while curr.right is not None:
            curr = curr.right
        return curr.data

    def size(self):
        def count_nodes(node):
            if node is None:
                return 0
            return 1 + count_nodes(node.left) + count_nodes(node.right)
        return count_nodes(self.root)

    def in_order(self):
        def traverse(node):
            if node is not None:
                traverse(node.left)
                print(node.data, end=' ')
                traverse(node.right)
        traverse(self.root)
        print()

    def pre_order(self):
        def traverse(node):
            if node is not None:
                print(node.data, end=' ')
                traverse(node.left)
                traverse(node.right)
        traverse(self.root)
        print()

