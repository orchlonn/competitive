class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        self.res = 0

        def helper(node, curr_max, curr_min):
            if not node:
                return
            
            self.res = max(self.res, abs(curr_max - node.val), abs(curr_min - node.val))

            curr_max = max(curr_max, node.val)
            curr_min = min(curr_min, node.val)

            helper(node.left, curr_max, curr_min)
            helper(node.right, curr_max, curr_min)
        
        helper(root, root.val, root.val)

        return self.res
