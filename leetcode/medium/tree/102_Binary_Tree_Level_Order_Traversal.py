# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        ans = []

        if root:
            queue.append(root)
        
        level = 0
        while queue:
            val = []
            for i in range(len(queue)):
                cur = queue.popleft()
                val.append(cur.val)

                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

            level += 1
            ans.append(val)

        return ans
            