class TreeNode:
    def __init__(self, left, right, val):
        self.left = left
        self.right = right
        self.val = val
    
def inorder(self, root):
    stack = []
    curr = root

    while curr or stack:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            curr = stack.pop()
            print(curr.val)
            curr = curr.right


def preorder(self, root):
    stack = []
    curr = root

    while curr or stack:
        if curr:
            print(curr.val)
            if curr.right:
                stack.append(curr.right)
                curr = curr.left
            else:
                curr = stack.pop()
    
def postorder(self, root):
    stack = [root]
    visit = [False]

    while stack:
        curr, visited = stack.pop(), visit.pop()
        if curr:
            if visited:
                print(curr.val)
            else:
                stack.append(curr)
                visit.append(True)
                stack.append(curr.left)
                visit.append(False)
                stack.append(curr.right)
                visit.append(False)

            