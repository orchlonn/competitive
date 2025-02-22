# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # Base case #1
        if not root:
            return 0
        
        q = deque([(root, 0)])
        ans = float('inf')

        while q:
            node, length = q.popleft()
            if node.left:
                q.append((node.left, length + 1))
            if node.right:
                q.append((node.right, length + 1))
            
            if not node.left and not node.right:
                ans = min(ans, length)
        
        return ans + 1
                
            

            