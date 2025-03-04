# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = []

        def dfs(node):
            nonlocal ans
            if not node: return 0
            left = dfs(node.left)
            ans.append(node.val)
            right = dfs(node.right)
        
        dfs(root)

        return ans[k-1]


# Time complexity: O(n)
# Space complexity: O(n)