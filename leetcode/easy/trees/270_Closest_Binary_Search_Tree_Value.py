# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        if not root:
            return root

        integer_part = int(target)
        fractional_part = target - integer_part
        if fractional_part == 0.5:
            target = integer_part  
        else:
            target = round(target) 

        ans = 0
        subtract = float('inf')

        def dfs(node, target):
            nonlocal subtract, ans
            if not node:
                return ans

            if abs(target - node.val) < subtract:
                ans = node.val
                subtract = min(subtract, abs(target - node.val))

            if node.val == target:
                return ans
            
            if node.val > target:
                dfs(node.left, target)
            if node.val < target:
                dfs(node.right, target)
            return ans

        return dfs(root, target)

# Time complexity: O(n)
# Space complexity: O(n)