# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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
            
            if rootTree.val != subTree.val:
                return False
            
            left = sameTree(rootTree.left, subTree.left)
            right = sameTree(rootTree.right, subTree.right)

            return left and right

        if not subRoot: return True
        if not root: return False

        if sameTree(root, subRoot): return True

        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)

        return left or right
# R = root tree. S = sub tree
# Time complexity: O(R * S)
# Space complexity: O(R * S)