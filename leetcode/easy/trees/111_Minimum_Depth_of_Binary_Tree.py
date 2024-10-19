# BFS solution

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        q = collections.deque([root])
        res = 1

        while q:
            for _ in range(len(q)):
                node = q.popleft()

                if not node:
                    continue

                if node.left == None and node.right == None:
                    return res
                
                q.append(node.left)
                q.append(node.right)

            res += 1

        return -1