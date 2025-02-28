# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ans = True

        def dfs(node):
            if not node:
                return 1
                
            left = dfs(node.left)
            right = dfs(node.right)

            nonlocal ans
            if left - right > 1 or right - left > 1:
                ans = False
            return max(left, right) + 1

        dfs(root)
        return ans

# Time complexity: O(n)
# Space complexity: O(n)