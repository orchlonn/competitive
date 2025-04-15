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
        N = len(questions)
        memoization =  {}
        
        for i in range(N - 1, -1, -1):
            points, brainpower = questions[i]
            next_i = i + 1 + brainpower

            skip = memoization[i + 1] if i + 1 < N else 0
            choose = points + (memoization[next_i] if next_i < N else 0)

            memoization[i] = max(skip, choose)
        
        return memoization[0]

# Time complexity: O(N)
# Space complexity: O(N) = [only cache]