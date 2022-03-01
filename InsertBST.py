class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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