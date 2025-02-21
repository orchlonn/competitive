# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxVal):
            if not node:
                return 0
            
            left = dfs(node.left, max(node.val, maxVal))
            right = dfs(node.right, max(node.val, maxVal))

            ans = right + left

            if node.val >= maxVal:
                ans += 1
            
            return ans
        
        return dfs(root, float('-inf'))