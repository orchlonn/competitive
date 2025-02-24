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

        queue = deque([(root)])
        ans = []

        while queue:
            maxCurr = float('-inf')
            for _ in range(len(queue)):
                node = queue.popleft()
                maxCurr = max(maxCurr, node.val)

                if node and node.left:
                    queue.append(node.left)
                if node and node.right:
                    queue.append(node.right)
            
            ans.append(maxCurr)
        
        return ans

# Time complexity: O(n)
# Space complexity: O(n)