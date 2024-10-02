from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def bfs(root):
    queue = deque()
    ans = []

    if root:
        queue.append(root)

    level = 0
    while queue:
        for i in range(len(queue))
            cur = queue.popleft()
            ans.append(cur.val)
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)

        level += 1
    return ans
