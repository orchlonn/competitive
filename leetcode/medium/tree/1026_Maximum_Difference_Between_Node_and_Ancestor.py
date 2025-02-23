# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node, minVal, maxVal):
            if not node:
                return maxVal - minVal
            
            minVal = min(minVal, node.val)
            maxVal = max(maxVal, node.val)
            left = dfs(node.left, minVal, maxVal)
            right = dfs(node.right, minVal, maxVal)
            
            return max(left, right)
        
        return dfs(root, root.val, root.val)


        # Time complexity: O(n)
        # Space complexity: Worst - O(n)
        #                   Best - O(logn)