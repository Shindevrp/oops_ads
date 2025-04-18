# Assume the student provides the implementations for all the methods below.
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# ---------- Binary Trees (BT) Methods ----------

def boundary_traversal(root):
    # STUDENT IMPLEMENTATION HERE
    r = []
    if root is None:
        return []
    def leaf_node(node):
        return node.left is None and node.right is None

    def left_nodes(node):
        c = node.left
        while c:
            if not leaf_node(c):
                r.append(c.val)
            if c.left:
                c = c.left
            else:
                c = c.right
    def leave_nodes(node):
        if node is None:
            return
        if leaf_node(node):
            r.append(node.val)
        else:
            leave_nodes(node.left)
            leave_nodes(node.right)

    def right_nodes(node):
        c = node.right
        tmp = []
        while c:
            if not leaf_node(c):
                tmp.append(c.val)
            c = c.right if c.right else c.left
        r.extend(tmp[::-1])

    if not leaf_node(root):
        r.append(root.val)

    left_nodes(root)
    leave_nodes(root)
    right_nodes(root)

    return r

def vertical_order_traversal(root):
    # STUDENT IMPLEMENTATION HERE
    if root is None:
        return []
    
    q = [(root,0)]
    d = {}
    while q:
        node, ele = q.pop(0)
        if ele in d:
            d[ele].append(node.val)
        else:
            d[ele] = [node.val]

        if node.left:
            q.append((node.left,ele - 1))
        if node.right:
            q.append((node.right,ele + 1))

    l = []
    for k in sorted(d.keys()):
        l.append(d[k])
    return l
    

def bottom_view(root):
    if root is None:
        return []
    
    d = {}
    queue = [(root, 0)]
    
    while queue:
        node, ele = queue.pop(0)
        d[ele] = node.val

        if node.left:
            queue.append((node.left, ele - 1))
        if node.right:
            queue.append((node.right, ele + 1))

    return [d[ele] for ele in sorted(d.keys())]
        


def sum_at_kth_level(root, k):
    if root is None:
        return 0
    def levelOrder():
        if root is None:
            return []
        queue = [root]
        result = []
        while queue:
            level_nodes = []
            for i in range(len(queue)):
                node = queue.pop(0)
                level_nodes.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level_nodes)
        return result
    result = levelOrder()
    if k >= len(result):
        return 0
    return sum(result[k])


# ---------- Binary Search Trees (BST) Methods ----------

def is_full_bst(root):
    # STUDENT IMPLEMENTATION HERE
    if root is None:
        return True
    if (root.left and not root.right) or (root.right and not root.left): 
        return False  
    return is_full_bst(root.right) and is_full_bst(root.left)          

def second_largest(root):
    # STUDENT IMPLEMENTATION HERE
    if root is None:
        return None
    a = inorder_traversal(root)
    # print(a)
    if len(a)<=1:
        return None
    else:
        return a[-2]


def floor_ceil(root, key):
    # STUDENT IMPLEMENTATION HERE
    # Return tuple: (floor, ceil) with -1 for none.
    floor , ceil = -1, -1
    while root:
        if root.val == key:
            return (key, key)
        elif root.val < key:
            floor = root.val
            root = root.right
        else:
            ceil = root.val
            root = root.left

    return (floor, ceil)

def count_nodes_in_range(root, low, high):
    # STUDENT IMPLEMENTATION 
    if root is None:
        return 0
    count = 0
    if low <= root.val <= high:
        count = 1
    if root.val > low:
        count+= count_nodes_in_range(root.left, low, high)
    if root.val < high:
        count += count_nodes_in_range(root.right, low, high)
    return count

# ---------- Balanced BST (BBST) Methods ----------

def construct_balanced_bst(sorted_array):
    # STUDENT IMPLEMENTATION HERE
    if len(sorted_array) == 0:
        return None
    a = len(sorted_array)//2
    root = TreeNode(sorted_array[a])
    
    root.left = construct_balanced_bst(sorted_array[:a])
    root.right = construct_balanced_bst(sorted_array[a+1:])

    return root


def is_avl(root):
    def height(node):
        if not node:
            return 0
        return 1 + max(height(node.left), height(node.right))

    def is_balanced(node):
        if not node:
            return True
        left_h = height(node.left)
        right_h = height(node.right)
        if abs(left_h - right_h) > 1:
            return False
        return is_balanced(node.left) and is_balanced(node.right)

    return is_balanced(root)

def delete_from_avl(root, key):
    def find_min(node):
        while node.left:
            node = node.left
        return node

    def height(node):
        if not node:
            return 0
        return 1 + max(height(node.left), height(node.right))

    def get_balance(node):
        if not node:
            return 0
        return height(node.left) - height(node.right)

    if not root:
        return root

    if key < root.val:
        root.left = delete_from_avl(root.left, key)
    elif key > root.val:
        root.right = delete_from_avl(root.right, key)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        temp = find_min(root.right)
        root.val = temp.val
        root.right = delete_from_avl(root.right, temp.val)

    balance = get_balance(root)

    if balance > 1 and get_balance(root.left) >= 0:
        return rotate_right(root)
    if balance > 1 and get_balance(root.left) < 0:
        root.left = rotate_left(root.left)
        return rotate_right(root)
    if balance < -1 and get_balance(root.right) <= 0:
        return rotate_left(root)
    if balance < -1 and get_balance(root.right) > 0:
        root.right = rotate_right(root.right)
        return rotate_left(root)

    return root

def rotate_left(node):
    right_child = node.right
    temp = right_child.left
    right_child.left = node
    node.right = temp
    return right_child

def rotate_right(node):
    left_child = node.left
    temp = left_child.right
    left_child.right = node
    node.left = temp
    return left_child

def convert_to_balanced_bst(root):
    # STUDENT IMPLEMENTATION HERE
    if root is None:
        return None
    sorted_values = inorder_traversal(root)
    return construct_balanced_bst(sorted_values)
# ---------- Utility Function ----------
def inorder_traversal(root):
    if not root:
        return []
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)

# ---------- Test Functions ----------

def test_boundary_traversal():
    print("Testing Boundary Traversal:")
    passed = 0
    # Test 1: Empty tree
    root = None
    result = boundary_traversal(root)
    expected = []
    if result == expected:
        print("Test 1 Passed")
        passed += 1
    else:
        print("Test 1 Failed")

    # Test 2: Single node
    root = TreeNode(1)
    result = boundary_traversal(root)
    expected = [1]
    if result == expected:
        print("Test 2 Passed")
        passed += 1
    else:
        print("Test 2 Failed")

    # Test 3: Tree with both left & right children
    #         1
    #        / \
    #       2   3
    #      / \   \
    #     4   5   6
    root = TreeNode(1)
    root.left = TreeNode(2); root.right = TreeNode(3)
    root.left.left = TreeNode(4); root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
    result = boundary_traversal(root)
    expected = [1,2,4,5,6,3]
    if result == expected:
        print("Test 3 Passed")
        passed += 1
    else:
        print("Test 3 Failed")

    # Test 4: Only left subtree
    #   1
    #  /
    # 2
    #/
    #3
    root = TreeNode(1)
    root.left = TreeNode(2); root.left.left = TreeNode(3)
    result = boundary_traversal(root)
    expected = [1,2,3]
    if result == expected:
        print("Test 4 Passed")
        passed += 1
    else:
        print("Test 4 Failed")

    # Test 5: Only right subtree
    # 1
    #  \
    #   2
    #    \
    #     3
    root = TreeNode(1)
    root.right = TreeNode(2); root.right.right = TreeNode(3)
    result = boundary_traversal(root)
    # (Assuming right boundary is returned in reverse order)
    expected = [1,3,2]
    if result == expected:
        print("Test 5 Passed")
        passed += 1
    else:
        print("Test 5 Failed")
    print("Boundary Traversal Passed", passed, "/5 tests\n")

def test_vertical_order_traversal():
    print("Testing Vertical Order Traversal:")
    passed = 0
    # Test 1: Empty tree
    root = None
    result = vertical_order_traversal(root)
    expected = []
    if result == expected:
        print("Test 1 Passed")
        passed += 1
    else:
        print("Test 1 Failed")

    # Test 2: Single node
    root = TreeNode(1)
    result = vertical_order_traversal(root)
    expected = [[1]]
    if result == expected:
        print("Test 2 Passed")
        passed += 1
    else:
        print("Test 2 Failed")

    # Test 3:
    #         1
    #        / \
    #       2   3
    #      / \   \
    #     4   5   6
    root = TreeNode(1)
    root.left = TreeNode(2); root.right = TreeNode(3)
    root.left.left = TreeNode(4); root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
    result = vertical_order_traversal(root)
    expected = [[4], [2], [1,5], [3], [6]]
    if result == expected:
        print("Test 3 Passed")
        passed += 1
    else:
        print("Test 3 Failed")

    # Test 4: Left skewed tree
    root = TreeNode(1)
    root.left = TreeNode(2); root.left.left = TreeNode(3)
    result = vertical_order_traversal(root)
    expected = [[3], [2], [1]]
    if result == expected:
        print("Test 4 Passed")
        passed += 1
    else:
        print("Test 4 Failed")

    # Test 5: Right skewed tree
    root = TreeNode(1)
    root.right = TreeNode(2); root.right.right = TreeNode(3)
    result = vertical_order_traversal(root)
    expected = [[1], [2], [3]]
    if result == expected:
        print("Test 5 Passed")
        passed += 1
    else:
        print("Test 5 Failed")
    print("Vertical Order Traversal Passed", passed, "/5 tests\n")

def test_bottom_view():
    print("Testing Bottom View:")
    passed = 0
    # Test 1: Empty tree
    root = None
    result = bottom_view(root)
    expected = []
    if result == expected:
        print("Test 1 Passed")
        passed += 1
    else:
        print("Test 1 Failed")

    # Test 2: Single node
    root = TreeNode(1)
    result = bottom_view(root)
    expected = [1]
    if result == expected:
        print("Test 2 Passed")
        passed += 1
    else:
        print("Test 2 Failed")

    # Test 3:
    #         20
    #        /  \
    #       8    22
    #      / \     \
    #     5   3     25
    #        / \
    #       10 14
    root = TreeNode(20)
    root.left = TreeNode(8); root.right = TreeNode(22)
    root.left.left = TreeNode(5); root.left.right = TreeNode(3)
    root.right.right = TreeNode(25)
    root.left.right.left = TreeNode(10); root.left.right.right = TreeNode(14)
    result = bottom_view(root)
    expected = [5,10,3,14,25]
    if result == expected:
        print("Test 3 Passed")
        passed += 1
    else:
        print("Test 3 Failed")

    # Test 4: Left skewed tree
    root = TreeNode(1)
    root.left = TreeNode(2); root.left.left = TreeNode(3)
    result = bottom_view(root)
    expected = [3,2,1]
    if result == expected:
        print("Test 4 Passed")
        passed += 1
    else:
        print("Test 4 Failed")

    # Test 5: Right skewed tree
    root = TreeNode(1)
    root.right = TreeNode(2); root.right.right = TreeNode(3)
    result = bottom_view(root)
    expected = [1,2,3]
    if result == expected:
        print("Test 5 Passed")
        passed += 1
    else:
        print("Test 5 Failed")
    print("Bottom View Passed", passed, "/5 tests\n")

def test_sum_at_kth_level():
    print("Testing Sum of Nodes at Kth Level:")
    passed = 0
    # Test 1: Empty tree
    root = None
    result = sum_at_kth_level(root, 2)
    expected = 0
    if result == expected:
        print("Test 1 Passed")
        passed += 1
    else:
        print("Test 1 Failed")

    # Test 2: Single node (level 0)
    root = TreeNode(5)
    result = sum_at_kth_level(root, 0)
    expected = 5
    if result == expected:
        print("Test 2 Passed")
        passed += 1
    else:
        print("Test 2 Failed")

    # Test 3: Two-level tree
    #      1
    #     / \
    #    2   3
    root = TreeNode(1)
    root.left = TreeNode(2); root.right = TreeNode(3)
    result = sum_at_kth_level(root, 1)
    expected = 5  # 2+3
    if result == expected:
        print("Test 3 Passed")
        passed += 1
    else:
        print("Test 3 Failed")

    # Test 4: Deeper tree
    #      1
    #     / \
    #    2   3
    #   /
    #  4
    root = TreeNode(1)
    root.left = TreeNode(2); root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    result = sum_at_kth_level(root, 2)
    expected = 4
    if result == expected:
        print("Test 4 Passed")
        passed += 1
    else:
        print("Test 4 Failed")

    # Test 5: Non-existent level
    result = sum_at_kth_level(root, 5)
    expected = 0
    if result == expected:
        print("Test 5 Passed")
        passed += 1
    else:
        print("Test 5 Failed")
    print("Sum of Nodes at Kth Level Passed", passed, "/5 tests\n")

def test_is_full_bst():
    print("Testing Check if BST is Full:")
    passed = 0
    # Test 1: Empty tree (assume True)
    root = None
    result = is_full_bst(root)
    expected = True
    if result == expected:
        print("Test 1 Passed")
        passed += 1
    else:
        print("Test 1 Failed")

    # Test 2: Single node
    root = TreeNode(1)
    result = is_full_bst(root)
    expected = True
    if result == expected:
        print("Test 2 Passed")
        passed += 1
    else:
        print("Test 2 Failed")

    # Test 3: Full BST:  2 / \ 1 3
    root = TreeNode(2)
    root.left = TreeNode(1); root.right = TreeNode(3)
    result = is_full_bst(root)
    expected = True
    if result == expected:
        print("Test 3 Passed")
        passed += 1
    else:
        print("Test 3 Failed")

    # Test 4: Not full BST: 2 with left child only
    root = TreeNode(2)
    root.left = TreeNode(1)
    result = is_full_bst(root)
    expected = False
    if result == expected:
        print("Test 4 Passed")
        passed += 1
    else:
        print("Test 4 Failed")

    # Test 5: Larger tree with a missing child
    root = TreeNode(4)
    root.left = TreeNode(2); root.right = TreeNode(6)
    root.left.left = TreeNode(1)
    root.left.left.right = TreeNode(15)
    root.right.left = TreeNode(5); root.right.right = TreeNode(7)
    result = is_full_bst(root)
    expected = False
    if result == expected:
        print("Test 5 Passed")
        passed += 1
    else:
        print("Test 5 Failed")
    print("Check if BST is Full Passed", passed, "/5 tests\n")

def test_second_largest():
    print("Testing Second Largest Element:")
    passed = 0
    # Test 1: One node
    root = TreeNode(10)
    result = second_largest(root)
    expected = None
    if result == expected:
        print("Test 1 Passed")
        passed += 1
    else:
        print("Test 1 Failed")

    # Test 2: Two nodes: 10 -> 20
    root = TreeNode(10)
    root.right = TreeNode(20)
    result = second_largest(root)
    expected = 10
    if result == expected:
        print("Test 2 Passed")
        passed += 1
    else:
        print("Test 2 Failed")

    # Test 3: Multiple nodes
    #      20
    #     /  \
    #   10   30
    #           \
    #            40
    root = TreeNode(20)
    root.left = TreeNode(10); root.right = TreeNode(30)
    root.right.right = TreeNode(40)
    result = second_largest(root)
    expected = 30
    if result == expected:
        print("Test 3 Passed")
        passed += 1
    else:
        print("Test 3 Failed")

    # Test 4: Largest has left subtree
    #      20
    #     /
    #   10
    #     \
    #     15
    root = TreeNode(20)
    root.left = TreeNode(10)
    root.left.right = TreeNode(15)
    result = second_largest(root)
    expected = 15
    if result == expected:
        print("Test 4 Passed")
        passed += 1
    else:
        print("Test 4 Failed")

    # Test 5: Largest with left subtree candidate
    #      20
    #     /  \
    #   10   30
    #         /
    #        25
    root = TreeNode(20)
    root.left = TreeNode(10); root.right = TreeNode(30)
    root.right.left = TreeNode(25)
    result = second_largest(root)
    expected = 25
    if result == expected:
        print("Test 5 Passed")
        passed += 1
    else:
        print("Test 5 Failed")
    print("Second Largest Element Passed", passed, "/5 tests\n")

def test_floor_ceil():
    print("Testing Floor and Ceil of a Value:")
    passed = 0
    # Test 1: Empty tree
    root = None
    result = floor_ceil(root, 15)
    expected = (-1, -1)
    if result == expected:
        print("Test 1 Passed")
        passed += 1
    else:
        print("Test 1 Failed")

    # Test 2: Single node equals key
    root = TreeNode(15)
    result = floor_ceil(root, 15)
    expected = (15, 15)
    if result == expected:
        print("Test 2 Passed")
        passed += 1
    else:
        print("Test 2 Failed")

    # Test 3: Key between nodes
    #       20
    #      /  \
    #    10    30
    root = TreeNode(20)
    root.left = TreeNode(10); root.right = TreeNode(30)
    result = floor_ceil(root, 25)
    expected = (20, 30)
    if result == expected:
        print("Test 3 Passed")
        passed += 1
    else:
        print("Test 3 Failed")

    # Test 4: Key less than smallest
    result = floor_ceil(root, 5)
    expected = (-1, 10)
    if result == expected:
        print("Test 4 Passed")
        passed += 1
    else:
        print("Test 4 Failed")

    # Test 5: Key greater than largest
    result = floor_ceil(root, 35)
    expected = (30, -1)
    if result == expected:
        print("Test 5 Passed")
        passed += 1
    else:
        print("Test 5 Failed")
    print("Floor and Ceil of a Value Passed", passed, "/5 tests\n")

def test_count_nodes_in_range():
    print("Testing Count Nodes within Range:")
    passed = 0
    # Test 1: Empty tree
    root = None
    result = count_nodes_in_range(root, 10, 20)
    expected = 0
    if result == expected:
        print("Test 1 Passed")
        passed += 1
    else:
        print("Test 1 Failed")

    # Test 2: Single node inside range
    root = TreeNode(15)
    result = count_nodes_in_range(root, 10, 20)
    expected = 1
    if result == expected:
        print("Test 2 Passed")
        passed += 1
    else:
        print("Test 2 Failed")

    # Test 3: Single node outside range
    root = TreeNode(25)
    result = count_nodes_in_range(root, 10, 20)
    expected = 0
    if result == expected:
        print("Test 3 Passed")
        passed += 1
    else:
        print("Test 3 Failed")

    # Test 4: Larger tree
    #         20
    #        /  \
    #      10   30
    #     /  \
    #    5   15
    root = TreeNode(20)
    root.left = TreeNode(10); root.right = TreeNode(30)
    root.left.left = TreeNode(5); root.left.right = TreeNode(15)
    result = count_nodes_in_range(root, 10, 20)
    expected = 3  # (10,15,20)
    if result == expected:
        print("Test 4 Passed")
        passed += 1
    else:
        print("Test 4 Failed")

    # Test 5: All nodes in range
    result = count_nodes_in_range(root, 0, 40)
    expected = 5
    if result == expected:
        print("Test 5 Passed")
        passed += 1
    else:
        print("Test 5 Failed")
    print("Count Nodes within Range Passed", passed, "/5 tests\n")

def test_construct_balanced_bst():
    print("Testing Construct Balanced BST from Sorted Array:")
    passed = 0
    # Test 1: Empty array
    arr = []
    root = construct_balanced_bst(arr)
    if inorder_traversal(root) == []:
        print("Test 1 Passed")
        passed += 1
    else:
        print("Test 1 Failed")

    # Test 2: Single element
    arr = [10]
    root = construct_balanced_bst(arr)
    if inorder_traversal(root) == [10]:
        print("Test 2 Passed")
        passed += 1
    else:
        print("Test 2 Failed")

    # Test 3: Two elements
    arr = [5,10]
    root = construct_balanced_bst(arr)
    if inorder_traversal(root) == [5,10]:
        print("Test 3 Passed")
        passed += 1
    else:
        print("Test 3 Failed")

    # Test 4: Multiple elements
    arr = [1,2,3,4,5,6,7]
    root = construct_balanced_bst(arr)
    if inorder_traversal(root) == [1,2,3,4,5,6,7]:
        print("Test 4 Passed")
        passed += 1
    else:
        print("Test 4 Failed")

    # Test 5: Non continuous sorted array
    arr = [2,5,8,10,13]
    root = construct_balanced_bst(arr)
    if inorder_traversal(root) == [2,5,8,10,13]:
        print("Test 5 Passed")
        passed += 1
    else:
        print("Test 5 Failed")
    print("Construct Balanced BST Passed", passed, "/5 tests\n")

def test_is_avl():
    print("Testing AVL Tree Check:")
    passed = 0
    # Test 1: Empty tree
    root = None
    if is_avl(root) == True:
        print("Test 1 Passed")
        passed += 1
    else:
        print("Test 1 Failed")

    # Test 2: Single node
    root = TreeNode(10)
    if is_avl(root) == True:
        print("Test 2 Passed")
        passed += 1
    else:
        print("Test 2 Failed")

    # Test 3: Balanced BST
    #      10
    #     /  \
    #    5   15
    root = TreeNode(10)
    root.left = TreeNode(5); root.right = TreeNode(15)
    if is_avl(root) == True:
        print("Test 3 Passed")
        passed += 1
    else:
        print("Test 3 Failed")

    # Test 4: Unbalanced tree
    #      10
    #     /
    #    5
    #   /
    #  2
    root = TreeNode(10)
    root.left = TreeNode(5); root.left.left = TreeNode(2)
    if is_avl(root) == False:
        print("Test 4 Passed")
        passed += 1
    else:
        print("Test 4 Failed")

    # Test 5: Complex unbalanced tree
    #      30
    #     /
    #   20
    #     \
    #     25
    root = TreeNode(30)
    root.left = TreeNode(20); root.left.right = TreeNode(25)
    if is_avl(root) == False:
        print("Test 5 Passed")
        passed += 1
    else:
        print("Test 5 Failed")
    print("AVL Tree Check Passed", passed, "/5 tests\n")

def test_delete_from_avl():
    print("Testing Delete Node from AVL Tree:")
    passed = 0
    # Test 1: Delete from empty tree
    root = None
    root = delete_from_avl(root, 10)
    if root is None:
        print("Test 1 Passed")
        passed += 1
    else:
        print("Test 1 Failed")

    # Test 2: Delete a leaf node
    #      20
    #     /  \
    #   10   30
    root = TreeNode(20)
    root.left = TreeNode(10); root.right = TreeNode(30)
    root = delete_from_avl(root, 10)
    if inorder_traversal(root) == [20,30]:
        print("Test 2 Passed")
        passed += 1
    else:
        print("Test 2 Failed")

    # Test 3: Delete root node with two children
    #      20
    #     /  \
    #   10   30
    root = TreeNode(20)
    root.left = TreeNode(10); root.right = TreeNode(30)
    root = delete_from_avl(root, 20)
    if inorder_traversal(root) == [10,30]:
        print("Test 3 Passed")
        passed += 1
    else:
        print("Test 3 Failed")

    # Test 4: Delete node causing unbalance
    #      30
    #     /  \
    #   20   40
    #   /
    # 10
    root = TreeNode(30)
    root.left = TreeNode(20); root.right = TreeNode(40)
    root.left.left = TreeNode(10)
    root = delete_from_avl(root, 40)
    if inorder_traversal(root) == [10,20,30]:
        print("Test 4 Passed")
        passed += 1
    else:
        print("Test 4 Failed")

    # Test 5: Delete non-existent node
    root = TreeNode(30)
    root.left = TreeNode(20); root.right = TreeNode(40)
    original = inorder_traversal(root)
    root = delete_from_avl(root, 50)
    if inorder_traversal(root) == original:
        print("Test 5 Passed")
        passed += 1
    else:
        print("Test 5 Failed")
    print("Delete Node from AVL Tree Passed", passed, "/5 tests\n")

def test_convert_to_balanced_bst():
    print("Testing Convert BST to Balanced BST:")
    passed = 0
    # Test 1: Empty tree
    root = None
    root = convert_to_balanced_bst(root)
    if root is None:
        print("Test 1 Passed")
        passed += 1
    else:
        print("Test 1 Failed")

    # Test 2: Already balanced tree
    #      20
    #     /  \
    #   10   30
    root = TreeNode(20)
    root.left = TreeNode(10); root.right = TreeNode(30)
    balanced = convert_to_balanced_bst(root)
    if inorder_traversal(root) == inorder_traversal(balanced):
        print("Test 2 Passed")
        passed += 1
    else:
        print("Test 2 Failed")

    # Test 3: Unbalanced tree conversion
    #      10
    #        \
    #        20
    #          \
    #          30
    root = TreeNode(10)
    root.right = TreeNode(20); root.right.right = TreeNode(30)
    balanced = convert_to_balanced_bst(root)
    if inorder_traversal(balanced) == [10,20,30]:
        print("Test 3 Passed")
        passed += 1
    else:
        print("Test 3 Failed")

    # Test 4: Larger unbalanced tree
    arr = [1,2,3,4,5,6,7,8,9]
    root = construct_balanced_bst(arr)
    # Unbalance: attach extra node to rightmost branch
    temp = root
    while temp.right:
        temp = temp.right
    temp.right = TreeNode(10)
    balanced = convert_to_balanced_bst(root)
    if inorder_traversal(balanced) == [1,2,3,4,5,6,7,8,9,10]:
        print("Test 4 Passed")
        passed += 1
    else:
        print("Test 4 Failed")

    # Test 5: BST with duplicate values
    arr = [1,2,2,3,4]
    root = construct_balanced_bst(arr)
    balanced = convert_to_balanced_bst(root)
    if inorder_traversal(balanced) == [1,2,2,3,4]:
        print("Test 5 Passed")
        passed += 1
    else:
        print("Test 5 Failed")
    print("Convert BST to Balanced BST Passed", passed, "/5 tests\n")

if __name__ == "__main__":
    test_boundary_traversal()
    test_vertical_order_traversal()
    test_bottom_view()
    test_sum_at_kth_level()
    test_is_full_bst()
    test_second_largest()
    test_floor_ceil()
    test_count_nodes_in_range()
    test_construct_balanced_bst()
    test_is_avl()
    test_delete_from_avl()
    test_convert_to_balanced_bst()

