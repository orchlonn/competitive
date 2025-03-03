# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        goodNode = 0
        def dfs(node, currMax):
            if not node:
                return 

            nonlocal goodNode
            if node.val >= currMax:
                goodNode += 1
                currMax = node.val
            
            dfs(node.left, currMax)
            dfs(node.right, currMax)
            
        dfs(root, root.val)
        return goodNode

# Time complexity: O(n)
# Space complexity: O(n)