class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        
        for c in s:
            if stack and stack[-1] == c:
                stack.pop(c)
            else:
                stack.append(c)

        return "".join(stack)