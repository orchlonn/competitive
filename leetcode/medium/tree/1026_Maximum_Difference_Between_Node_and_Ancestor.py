class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        if not root:
            return 0 
        
        def dfs(node, currMax, currMin):
            if not node:
                return currMax - currMin
            
            currMax = max(currMax, node.val)
            currMin = min(currMin, node.val)

            left = dfs(node.left, currMax, currMin)
            right = dfs(node.right, currMax, currMin)

            return max(left, right)
        
        return dfs(root, root.val, root.val)
