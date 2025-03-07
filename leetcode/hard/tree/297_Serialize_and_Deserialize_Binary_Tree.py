# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        ans = []

        def dfs(node):
            if not node:
                ans.append("N")
                return 

            ans.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(ans)
        

    def deserialize(self, data):
        vals = data.split(",")
        self.i = 0
        def dfs():
            if vals[self.i] == "N":
                self.i += 1
                return None
            
            node = TreeNode(vals[self.i])
            self.i += 1
            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()

# Time complexity: O(n)
# Space complexity: O(n)