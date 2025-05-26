class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        def dfs(i, j):
            if i == len(s1) and j == len(s2):
                return True
            if (i, j) in cache:
                return cache[(i, j)]
                
            if (len(s1) > i and s1[i] == s3[i + j] and dfs(i + 1, j)):
                return True
            
            if (len(s2) > j and s2[j] == s3[i + j] and dfs(i, j + 1)):
                return True

            cache[(i, j)] = False
            return False
        
        cache = {}
        return dfs(0, 0)

# m = len(s1), n len(s2)
# Time complexity: O(m * n)
# Space complexity: O(m * n)