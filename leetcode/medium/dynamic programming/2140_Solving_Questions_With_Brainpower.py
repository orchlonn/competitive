class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        N = len(questions)
        cache = {}

        def dp(i):
            if i >= N:
                return 0
            
            if i in cache:
                return cache[i]
            
            points, brainpower = questions[i]

            cache[i] = max(
                dp(i + 1), # skip
                points + dp(1 + i + brainpower) # choose
            )
            return cache[i]
        
        return dp(0)

# Time complexity: O(N)
# Space complexity: O(N) = [cache + recursion stack]