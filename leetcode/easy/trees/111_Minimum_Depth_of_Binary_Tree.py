# BFS solution

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: 
            return 0
        
        q = collections.deque([root])
        depth = 1

        while q:
            for _ in range(len(q)):
                node = q.popleft()

                if not node:
                    continue
                    
                if not node.left and not node.right:
                    return depth
                
                q.append(node.left)
                q.append(node.right)
            
            depth += 1
        
        return -1
