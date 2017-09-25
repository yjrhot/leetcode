# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        
        while root:
            tmp_child = TreeLinkNode(0)
            cur_child = tmp_child
            while root:
                if root.left:
                    cur_child.next = root.left
                    cur_child = cur_child.next
                if root.right:
                    cur_child.next = root.right
                    cur_child = cur_child.next
                root = root.next
            root = tmp_child.next
