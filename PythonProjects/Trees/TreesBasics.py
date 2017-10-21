import queue
import copy


class Node:
    def __init__(self, data=None, left=None, right=None):
        self.left = left
        self.right = right
        self.data = data

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_right(self, data):
        new_node = Node()
        new_node.set_data(data)
        current = self.root
        if current is None:
            self.root = new_node
            return
        while current.right is not None:
            current = current.right
        current.right = new_node
        return

    def insert_left(self, data):
        new_node = Node(data)
        #new_node.set_data(data)
        current = self.root
        if current is None:
            self.root = new_node
            return
        while current.left is not None:
            current = current.left
        current.left = new_node
        return

    def print_nice_tree(self):
        if self.root is None:
            return
        full_result = []
        current_level = []
        current_level.append(self.root)
        level = 0
        while current_level:
            next_level = []
            result = []
            for current in current_level:
                if current == "e":
                    next_level.append("e") # left
                    next_level.append("e") # right
                    result.append("e")
                    continue
                result.append(current.data)
                if current.left is not None:
                    next_level.append(current.left)
                else:
                    next_level.append("e")
                if current.right is not None:
                    next_level.append(current.right)
                else:
                    next_level.append("e")
            current_level = next_level
            print(result)
            full_result.append(result)
            level += 1
            # check if next level is all e's; this will be the end
            all_empty = True
            for n in next_level:
                if n != "e":
                    all_empty = False
                    break
            if all_empty is True:
                break
        depth = len(full_result)
        for level in range(0, depth):
            this_level = full_result[level]
            for value in this_level:
                if value == 'e':
                    value = ' '
                print("%s%s" % (' ' * pow(depth-level,2), value), sep="", end=' ')
            print("\n")


# dlr
def preorder_recursive(root):
    current = root
    if current is None:
        return
    print(current.data, end=" ")
    if current.left is not None:
        preorder_recursive(current.left)
    if current.right is not None:
        preorder_recursive(current.right)


def preorder_iterative(root):
    stack = []
    if root is not None:
        stack.append(root)
    print("\nPre-Order iterative: ")
    while stack:
        current = stack.pop()
        print(current.data, end=" ")
        if current.right is not None:
            stack.append(current.right)
        if current.left is not None:
            stack.append(current.left)


# ldr
def inorder_recursive(root):
    current = root
    if current is None:
        return
    if current.left is not None:
        inorder_recursive(current.left)
    print(current.data, end=" ")
    if current.right is not None:
        inorder_recursive(current.right)


def inorder_iterative(root):
    stack = []
    if root is None:
        return
    current = root
    print("\nIn-Order iterative: \n")
    while stack or current is not None:
        if current is not None:
            stack.append(current)
            current = current.left
        else:
            current = stack.pop()
            print(current.data, end=" ")
            current = current.right
    return


# lrd
def postorder_recursive(root):
    current = root
    if current is None:
        return
    if current.left is not None:
        postorder_recursive(current.left)
    if current.right is not None:
        postorder_recursive(current.right)
    print(current.data, end=" ")

# this one is most difficult
def postorder_iterative(root):
    if root is None:
        return
    stack = []
    visited = set()
    current = root
    print("\nPost-Order Iterative:\n")
    while stack or current is not None:
        if current is not None:
            stack.append(current)
            current = current.left
        else:
            current = stack.pop()
            if current.right is not None and current.right not in visited:
                stack.append(current)
                current = current.right
            else:
                visited.add(current)
                print(current.data, end=" ")
                current = None


def bfs_levelorder(root):
    if root is None:
        return
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        current = q.get()
        print(current.data, end=" ")
        if current.left is not None:
            q.put(current.left)
        if current.right is not None:
            q.put(current.right)

max_val = float("-inf")
def max_element_in_btree(root):
    if root is None:
        return
    current = root
    global max_val
    max_val = max(max_val, current.data)
    if current.left is not None:
        max_element_in_btree(current.left)
    if current.right is not None:
        max_element_in_btree(current.right)


def find_num_leaf(root):
    if root is None:
        return
    q = queue.Queue()
    numleaf = 0
    q.put(root)
    while not q.empty():
        current = q.get()
        if current.left is None and current.right is None:
            numleaf += 1
        if current.left is not None:
            q.put(current.left)
        if current.right is not None:
            q.put(current.right)
    return numleaf


def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))


def diameter_of_tree(root):
    if root is None:
        return 0
    lheight = height(root.left)
    rheight = height(root.right)
    ldiameter = diameter_of_tree(root.left)
    rdiameter = diameter_of_tree(root.right)
    return max(lheight + rheight + 1, max(ldiameter, rdiameter))


def mirror_of_tree(root):
    if root is None:
        return
    temp = root.left
    root.left = root.right
    root.right = temp
    mirror_of_tree(root.left)
    mirror_of_tree(root.right)

def printpaths(root):
    path = [0]*100
    print("printing all paths\n")
    printallpaths(root, path, 0)


def printallpaths(root, path, pathlen):
    if root is None:
        return
    if root is not None:
        print(root.data, path)
        path[pathlen] = root.data
        pathlen += 1
    if root.left is None and root.right is None:
        print("pathlen = %r" % pathlen)
        for i in range(0, pathlen):
            print(path[i], sep=" ", end=" ")
        print("\n--> %r " %path )
    else:
        printallpaths(root.left, path, pathlen)
        printallpaths(root.right, path, pathlen)


def are_trees_mirrors(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False
    if root1.data != root2.data:
        return False
    return are_trees_mirrors(root1.left, root2.right) \
           and are_trees_mirrors(root1.right, root2.left)


def least_common_ancestor_binary_tree(root, data1, data2):
    if root is None:
        return None
    # note that we return the node, not the node data *********
    if root.data == data1 or root.data == data2:
        return root
    else:
        left = least_common_ancestor_binary_tree(root.left, data1, data2)
        right = least_common_ancestor_binary_tree(root.right, data1, data2)
        if left and right:
            return root
        elif left:
            # print("left = %r" %left.data)
            return left
        elif right:
            # print("right = %r" %right.data)
            return right


result = []
def all_ancestors_of_node(root, data):
    global result
    if root is None:
        return 0
    if (root.left and root.left.data == data) or (root.right and root.right.data == data) \
        or all_ancestors_of_node(root.left, data) or all_ancestors_of_node(root.right, data):
        result.append(root.data)
        return 1
    return 0


def zigzag_traversal(root):
    if root is None:
        return
    current_level = list()
    next_level = list()
    current_level.append(root)
    print_r_to_l = True
    while current_level:
        current = current_level.pop()
        print(current.data, end=" ")
        if print_r_to_l is True:
            if current.left is not None:
                next_level.append(current.left)
            if current.right is not None:
                next_level.append(current.right)
        else:
            if current.right is not None:
                next_level.append(current.right)
            if current.left is not None:
                next_level.append(current.left)
        if not current_level and next_level:
            current_level = next_level
            next_level = []


prev = float("-inf")
# do inorder traversal, and compare with previous
def check_if_bst(root):
    global prev
    if root is None:
        return True
    if check_if_bst(root.left) is False:
        return False
    if prev > root.data:
        return False
    prev = root.data
    if check_if_bst(root.right) is False:
        return False
    return True


#  driver
new_node1 = Node(6, Node(2, Node(1), Node(9)), Node(8))
#new_node1 = Node(1, Node(2, None, Node(4, Node(9), Node(10))), Node(100, Node(5, Node(6), Node(7, Node(8), None)), None))
new_node2 = Node(1, Node(2), None)
btree = BinaryTree()
test_btree = BinaryTree()
btree.root = new_node1
test_btree.root = new_node2
btree.print_nice_tree()
preorder_iterative(btree.root)
print("\n")
preorder_recursive(btree.root)
print("\n")
inorder_iterative(btree.root)
print("\n")
inorder_recursive(btree.root)
print("\n")
postorder_iterative(btree.root)
print("\n")
postorder_recursive(btree.root)
print("\n")
bfs_levelorder(btree.root)
print("\n")
max_element_in_btree(btree.root)
print("max element %d\n" % max_val)
print("\nNumber of leaf nodes %d" % find_num_leaf(btree.root))
print("\nDiameter of tree %d" % diameter_of_tree(btree.root))

print("Mirroring tree now\n")
mirror_btree = copy.deepcopy(btree)
mirror_of_tree(mirror_btree.root)
mirror_btree.print_nice_tree()
btree.print_nice_tree()
#print("All paths:")
#printpaths(btree.root)
#print(are_trees_mirrors(btree.root, test_btree.root))
lca = least_common_ancestor_binary_tree(btree.root, 6, 8)
print(lca.data)
all_ancestors_of_node(btree.root, 4)
print(result)
#a = [1, 2, 3, 4, 5, 6, 7]
#print(a[0: 2])
print("Zigzag: \n")
zigzag_traversal(btree.root)
print("\n%r" % check_if_bst(btree.root))


