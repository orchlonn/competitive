class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        diameter = 0 

        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            nonlocal diameter

            diameter = max(diameter, left + right)

            return max(left, right) + 1
        
        dfs(root)

        return diameter