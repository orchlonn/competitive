# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        ans = []
        ans.append(root.val)
        queue = deque([(root)])

        while queue:
            isValid = False

            for i in range(len(queue)):
                cur = queue.popleft()
                if cur.right:
                    if not isValid:
                        ans.append(cur.right.val)
                        isValid = True
                    queue.append(cur.right)
                if cur.left:
                    if not isValid:
                        ans.append(cur.left.val)
                        isValid = True
                    queue.append(cur.left)
        
        return ans
