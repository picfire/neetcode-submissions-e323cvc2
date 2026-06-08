# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        values = []

        def addRoot(node):
            if not node:
                return  
            values.append(node.val)

            addRoot(node.left)
            addRoot(node.right)


        addRoot(root)

        values.sort()

        return values[k - 1]
    

            
