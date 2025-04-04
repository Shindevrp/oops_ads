class BTNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def copy_tree(node):
    if node is None:
        return None
    new_node = BTNode(node.data)
    new_node.left = copy_tree(node.left)
    new_node.right = copy_tree(node.right)
    return new_node

def replace(node, old, new):
    if node is None:
        return 0
    c = 0
    if node.data == old:
        node.data = new
        c += 1
    c += replace(node.left, old, new)
    c += replace(node.right, old, new)
    return c

def countNodesAtDepth(node, depth):
    if node is None:
        return 0
    if depth == 0:
        return 1
    left_count = countNodesAtDepth(node.left, depth - 1)
    right_count = countNodesAtDepth(node.right, depth - 1)
    return left_count + right_count

def allSame(node):
    if node is None:
        return True
    value = node.data
    stack = [node]
    while stack:
        curr = stack.pop()
        if curr.data != value:
            return False
        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)
    return True

def leafList(node):
    if node is None:
        return []
    res = []
    stack = [node]
    while stack:
        curr = stack.pop()
        if curr.left is None and curr.right is None:
            res.append(curr.data)
        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)
    return res

def reflect(node):
    if node is None:
        return
    queue = [node]
    while queue:
        curr = queue.pop(0)
        curr.left, curr.right = curr.right, curr.left
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)

def condense(node):
    if node is None:
        return None
    while node and (node.left is None or node.right is None):
        node = node.left if node.left else node.right
    if node:
        node.left = condense(node.left)
        node.right = condense(node.right)
    return node

def print_preorder(node):
    if node is None:
        return
    print(node.data, end=" ")
    print_preorder(node.left)
    print_preorder(node.right)
