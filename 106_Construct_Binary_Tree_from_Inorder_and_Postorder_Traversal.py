# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            ind = inorder.index(postorder.pop())
            root = TreeNode(inorder[ind])
            
            #下面两行的顺序不能反，因为涉及到postorder 这个list的pop的顺序
            root.right = self.buildTree(inorder[ind + 1:], postorder)
            root.left = self.buildTree(inorder[:ind], postorder)
            
        
            return root
