"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Edge case #1
        if not node:
            return None

        oldToNew = {}
        oldToNew[node] = Node(node.val) 
        queue = deque([node])

        while queue:
            cur = queue.popleft()   
            for nei in cur.neighbors:
                if nei not in oldToNew:
                    queue.append(nei)
                    oldToNew[nei] = Node(nei.val)
                oldToNew[cur].neighbors.append(oldToNew[nei])
        
        return oldToNew[node]

        