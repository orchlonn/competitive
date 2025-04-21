class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        N = len(questions)
        memoization = {}

        def dp(i):
            if i >= N:
                return 0
            
            if i in memoization:
                return memoization[i]

            points, brainpower = questions[i]
            memoization[i] = max(
                dp(i + 1),
                points + dp(i + 1 + brainpower)
            )
            return memoization[i]

        return dp(0)

# Time complexity: O(N)
# Space complexity: O(N) = [cache + recursion stack]



# Soltion #2 (Bottom up)
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        cache = {}
        N = len(questions)

        for i in reversed(range(N)):
            points, brainpower = questions[i]
            next_i = brainpower + 1 + i

            skip = cache[i + 1] if (i + 1) < N else 0
            choose = points + (cache[next_i] if next_i < N else 0)

            cache[i] = max(skip, choose)

        return cache[0]

# Time complexity: O(N)
# Space complexity: O(N) = [only cache]