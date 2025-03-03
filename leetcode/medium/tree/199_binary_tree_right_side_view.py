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

        q = deque([(root)])
        ans = []
        ans.append(root.val)

        while q:
            temp = []
            for _ in range(len(q)):
                node = q.popleft()
                print(node)
                if node and node.left:
                    q.append(node.left)    
                    temp.append(node.left.val)
                if node and node.right:
                    q.append(node.right)
                    temp.append(node.right.val)

            if len(temp) > 1:
                ans.append(temp[len(temp) - 1])
            elif len(temp) == 1:
                ans.append(temp[0])

        return ans

# Time complexity: O(n)
# Space complexity: O(n)