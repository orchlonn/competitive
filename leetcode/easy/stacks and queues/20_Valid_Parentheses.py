class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching = {"(": ")", "[": "]", "{": "}"}

        for c in s:
            if c in matching:
                stack.append(c)
            else:
                if not stack:
                    return False

                prev_opening = stack.pop()
                if matching[prev_opening] != c:
                    return False
            
        return not stack