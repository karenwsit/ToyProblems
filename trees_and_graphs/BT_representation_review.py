#List of Lists Representation of Binary Trees

def make_binary_tree(r):
    return [r, [], []]

def insert_left(root, new_branch):
    left_subtree = root.pop(1)
    if len(left_subtree) > 1:
        root.insert(1, [new_branch, left_subtree, []])
    else:
        root.insert(1, [new_branch, [], []])
    return root

def insert_right(root, new_branch):
    right_subtree = root.pop(2)

    if len(right_subtree) > 1:
        root.insert(2, [new_branch, [], right_subtree])
    else:
        root.insert(2, [new_branch, [], []])
    return root

def get_root_value(root):
    return root[0]

def set_root_value(root, new_value):
    root[0] = new_value

def get_left_subtree(root):
    return root[1]

def get_right_subtree(root):
    return root[2]
