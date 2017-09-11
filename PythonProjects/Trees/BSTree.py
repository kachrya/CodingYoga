import copy

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BSTree:
    def __init__(self):
        self.root = None

    def insert_key(self, key):
        new_node = Node(key)
        if self.root is None:
            self.root = new_node
            return
        current = self.root
        while current:
            if key < current.data:
                if current.left is None:
                    current.left = new_node
                else:
                    current = current.left
            elif key == current.data:
                return
            else:
                if current.right is None:
                    current.right = new_node
                else:
                    current = current.right
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


def delete_key(root, key):
    if key == root.data:
        if root.left and root.right:
            [parent_succ, succ] = find_min(root.right, root)
            if parent_succ.left == succ:
                parent_succ.left = succ.right
            else:
                parent_succ.right = succ.right
            succ.left = root.left
            succ.right = root.right
            return succ
        else:
            if root.left:
                return root.left
            else:
                return root.right
    else:
        if key < root.data:
            if root.left:
                root.left = delete_key(root.left, key)
        else:
            if root.right:
                root.right = delete_key(root.right, key)
    return root


def find_min(root, parent):
    if root.left:
        return find_min(root.left, root)
    else:
        return [parent, root]


def least_common_ancestor_bst(root, value1, value2):
    # assume both values exists
    current = root
    minval = min(value1, value2)
    maxval = max(value1, value2)
    while current:
        if minval <= current.data <= maxval:
            return current.data
        # if above condition is not true, it means
        # both minval and maxval lie on the same side of
        # current node, hence comparing with one of them
        # is same as comparing with both of them
        if minval < current.data:
            current = current.left
        else:
            current = current.right


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







bst_tree = BSTree()
bst_tree.insert_key(6)
bst_tree.insert_key(2)
bst_tree.insert_key(9)
bst_tree.insert_key(8)
bst_tree.insert_key(1)





"""
bst_tree.insert_key(7)
bst_tree.insert_key(4)
bst_tree.insert_key(18)
bst_tree.insert_key(5)
bst_tree.insert_key(1)
bst_tree.insert_key(10)
bst_tree.insert_key(9)
bst_tree.insert_key(6)
bst_tree.insert_key(13)
bst_tree.insert_key(2)
bst_tree.insert_key(3)
bst_tree.insert_key(12)
"""
bst_tree.print_nice_tree()
#delete_key(bst_tree.root, 4)
#bst_tree.print_nice_tree()
print(least_common_ancestor_bst(bst_tree.root, 9, 13))
print("\n%r" % check_if_bst(bst_tree.root))
