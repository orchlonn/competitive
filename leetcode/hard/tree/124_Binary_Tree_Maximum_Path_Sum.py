class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
      res = root.val

      def dfs(node):
        if not node:
          return 0
        nonlocal res        
        leftMax = dfs(node.left)
        rightMax = dfs(node.right)
        leftMax = max(0, leftMax)
        rightMax = max(0, rightMax)
        
        res = max(res, node.val + leftMax + rightMax)
        return node.val + max(leftMax, rightMax)

      dfs(root)
      return res