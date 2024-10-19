# DFS solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = collections.deque([root])
        ans = 0

        while q:
            qLen = len(q)
            ans = 0

            for _ in range(qLen):
                node = q.popleft()

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

                if node:
                    ans += node.val
        return ans