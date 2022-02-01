from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def bstFromPreorder(preorder: List[int]) -> TreeNode:
    root = TreeNode(preorder[0])
    index = 1
    while index < len(preorder):
        print(preorder[index])
        insert(root, preorder[index])
        index += 1
    return root
def insert(root, val):
    if val < root.val and root.left == None:
        root.left = TreeNode(val)

        return
    elif val < root.val and root.left != None:

        insert(root.left, val)

    elif val > root.val and root.right == None:
        root.right = TreeNode(val)

        return
    elif val > root.val and root.right != None:

        insert(root.right, val)    