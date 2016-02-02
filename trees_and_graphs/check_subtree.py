#Exercise 4.10 of Cracking the Coding Interview
#T1 & T2 are two very large binary tress with T1 much bigger than T2.
#Create an alogirthm to determine if T2 is a subtree of T1.
#A tree T2 is a subtree of T1 if there exists a node n in T1 such that the subtree of n is identical to T2.
#################################################################################

class binaryTree(object):
    
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def check_subtree(t1, t2):
    # an empty tree is always a subtree
    if t2 is None:
        return True
    if t1 is None:
        return False
    if t1.value == t2.value and match_tree(t1, t2):
        return True
    return check_subtree(t1.left, t2) or check_subtree(t1.right, t2)

def match_tree(t1, t2):
    if t1 is None and t2 is None:
        return True
    elif t1 is None or t2 is None:
        return False
    elif t1.value != t2.value:
        return False
    else:
        return match_tree(t1.left, t2.left) and match_tree(t2.right, t2.right)
