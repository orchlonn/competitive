# BFS solution
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
          return 0
        level = 0
        q = deque([root])

        while q: 
          for i in range(len(q)):
            node = q.popleft()
            if node.left:
              q.append(node.left)
            if node.right:
              q.append(node.right)
          
          level += 1
        
      return level

# DFS solution
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [[root, 1]]
        res = 0

        while stack:
          node, depth = stack.pop()

          if node:
            stack.append([node.left, depth + 1])
            stack.append([node.right, depth + 1])
            res = max(res, depth)
          
        
        return res