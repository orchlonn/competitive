# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, curr):
            if not node:
                return 0

            curr += node.val

            if (node.left == None and node.right == None):
                return curr == targetSum
            
            left = dfs(node.left, curr)
            right = dfs(node.right, curr)

            return left or right
        
        return dfs(root, 0)
