# DFS Solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        q = collections.deque([root])
        ans = []

        while q:
            qLenght = len(q)
            max_curr = float('-inf')

            for _ in range(qLenght):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                max_curr = max(max_curr, node.val)

            ans.append(max_curr)

        return ans