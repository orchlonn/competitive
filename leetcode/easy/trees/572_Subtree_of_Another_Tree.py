# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(rootTree, subTree):
            if not rootTree and not subTree:
                return True
            
            if not rootTree or not subTree:
                return False            

            if rootTree and subTree and rootTree.val == subTree.val:
                return (sameTree(rootTree.left, subTree.left) and
                        sameTree(rootTree.right, subTree.right))
            
            return False

        if not subRoot: return True

        if not root: return False

        if sameTree(root, subRoot): return True
        
        return( self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))

# R = root tree. S = sub tree
# Time complexity: O(R * S)
# Space complexity: O(R * S)