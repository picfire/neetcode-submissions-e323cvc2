# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lca = [root] #equals to the tree

        def search(root):
            if not root:
                return


            lca[0] = root #set up the root as the leaf we are currently looking at 
            if root is p or root is q:
                return
            elif root.val < p.val and root.val < q.val:
                search(root.right)
            elif root.val > p.val and root.val > q.val:
                search(root.left)
            else:
                return

        search(root) #toggle the function outside
        return lca[0] #lastly return the leaf we were looking at