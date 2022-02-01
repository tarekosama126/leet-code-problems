def PreorderTraversal(root):
    res = []
    if root:
        res.append(root.val)
        if root.left != None and root.right == None:
            res = res + PreorderTraversal(root.left)
            res.append(None)
        elif root.right != None and root.left == None:
            res.append(None)
            res = res + PreorderTraversal(root.right)
        else:
            res = res + PreorderTraversal(root.left)
            res = res + PreorderTraversal(root.right)

    return res
