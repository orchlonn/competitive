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



# Soltion #2 (Bottom up)
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        N = len(questions)
        cache = {}

        for i in reversed(range(N)):
            points, brainpower = questions[i]
            next_i = i + 1 + brainpower 

            choose = points + (cache[next_i] if next_i < N else 0)
            skip = cache[i + 1] if i + 1 < N else 0
            
            cache[i] = max(choose, skip)
    
        return cache[0]

# Time complexity: O(N)
# Space complexity: O(N) = [only cache]