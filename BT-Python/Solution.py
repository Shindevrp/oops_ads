class BinaryTree:
    class BTNode:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

        def __str__(self):
            return str(self.data)

    def __init__(self, element=None, left_tree=None, right_tree=None):
        if element is None:
            self.root = None
        else:
            self.root = BinaryTree.BTNode(element)
            if left_tree is not None:
                self.root.left = left_tree.root
            if right_tree is not None:
                self.root.right = right_tree.root

    def countInternal(self, node=None):
        if node is None:
            node = self.root
        if node is None:
            return 0
        else:
            if node.left is None and node.right is None:
                return 0
            else:
                if node.left:
                    left_count = self.countInternal(node.left)
                else:
                    left_count = 0
                if node.right:
                    right_count = self.countInternal(node.right)
                else:
                    right_count = 0
                return 1 + left_count + right_count

    def height(self, node=None):
        if node is None:
            node = self.root

        if node is None:
            return 0
        else:
            if node.left:
                left_height = self.height(node.left)
            else:
                left_height = 0
            if node.right:
                right_height = self.height(node.right)
            else:
                right_height = 0

            return 1 + max(left_height, right_height)


    def isPerfect(self, node=None, depth=None, level=0):
        if node is None:
            node = self.root
            depth = self.getDepth(self.root)
        if node is None:
            return True
        if node.left is None and node.right is None:
            return depth == level + 1
        if node.left is None or node.right is None:
            return False
        return self.isPerfect(node.left, depth, level + 1) and self.isPerfect(node.right, depth, level + 1)

    def getDepth(self, node):
        if node is None:
            return 0
        return 1 + self.getDepth(node.left)
    
    def __str__(self):
        lines = []
        self._preOrderTraversal(self.root, 0, lines)
        return "\n".join(lines)

    def _preOrderTraversal(self, node, depth, lines):
        indent = "  " * (depth - 1) if depth > 0 else ""
        if node is None:
            lines.append(indent + "null")
        else:
            lines.append(indent + str(node))
            self._preOrderTraversal(node.left, depth + 1, lines)
            self._preOrderTraversal(node.right, depth + 1, lines)