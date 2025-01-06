# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_binary_tree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i=1

    while queue and i <len(values):
        curr = queue.popleft()

        if values[i] is not None:
            curr.left = TreeNode(values[i])
            queue.append(curr.left)
        i+=1
        if i<len(values) and values[i] is not  None:
            curr.right = TreeNode(values[i])
            queue.append(curr.right)
        i+=1
    return root

tree = [3,9,20,None,None,15,7]

root  = build_binary_tree(tree)

def depthoftree(root):
    if root == None:
        return 0 
    leftSubtree = 1+ depthoftree(root.left)

    rightSubtree = 1+ depthoftree(root.right)

    return max(rightSubtree,leftSubtree)

print(depthoftree(root))