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
        queue = deque([(target)])
        visit = set([(target)])

        while queue and distance < k:
            current_level = len(queue)  
            for _ in range(current_level):
                node = queue.popleft()
                for nei in [node.left, node.right, node.parent]:
                    if nei and nei not in visit:
                        visit.add((nei))
                        queue.append((nei))

            distance += 1

        
        return [node.val for node in queue] 