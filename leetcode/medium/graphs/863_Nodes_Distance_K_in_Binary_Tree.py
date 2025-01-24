# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def dfs(node, parent):
            if not node:
                return
            node.parent = parent
            dfs(node.left, node)
            dfs(node.right, node)
        
        dfs(root, None)
        distance = 0
        visit = {target}
        queue = deque([(target)])

        while queue and distance < k:
            curr_len = len(queue)
            for _ in range(curr_len):
                node = queue.popleft()
                for neighbor in [node.left, node.right, node.parent]:
                    if neighbor and neighbor not in visit:
                        visit.add((neighbor))
                        queue.append((neighbor))
            
            distance += 1
        
        return [node.val for node in queue]
