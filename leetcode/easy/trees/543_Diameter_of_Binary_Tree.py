class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        diameter = 0

        def findLongestPath(node):
            if not node:
                return 0
            
            nonlocal diameter

            left = findLongestPath(node.left)
            rihgt = findLongestPath(node.rihgt)

            diameter = max(diameter, left + right)

            return max(left, right) + 1
        
        findLongestPath(root)

        return diameter
