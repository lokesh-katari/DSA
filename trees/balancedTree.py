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

tree =[1,2,2,3,None,None,3,4,None,None,4]

root  = build_binary_tree(tree)

def balanceTree(root):
    # if the root is None we can say that the tree is already baalnced
    if not root:
        return True
    
    # we are gettign the height of the subtrees along with the if there are balanced nodes or not 
    def dfs(root):
        if not root:
            return [True,0]
        left = dfs(root.left)
        right = dfs(root.right)
        balanced = left[0] and right[0] and abs(left[1]-right[1])<=1
        return [balanced,1+max(left[1],right[1])]
    return dfs(root)[0]

print(balanceTree(root))