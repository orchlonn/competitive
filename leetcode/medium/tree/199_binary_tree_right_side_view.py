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

        queue = deque([(root)])
        ans = []
        ans.append(root.val)
        
        while queue:
            temp = []
            for _ in range(len(queue)):
                node = queue.popleft()
            
                if node and node.left:
                    queue.append(node.left)
                    temp.append(node.left.val)
                if node and node.right:
                    queue.append(node.right)
                    temp.append(node.right.val)

            if len(temp) > 1:
                ans.append(temp[len(temp) - 1])
            elif len(temp) == 1:
                ans.append(temp[0])

        return ans


# Time complexity: O(n)
# Space complexity: O(n)