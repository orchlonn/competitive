class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        def backtrack(n , num):
            if n == 0:
                ans.append(num)
                return
            
            tailDigit = num % 10
            nextDigits = set([tailDigit - k, tailDigit + k])

            for nextDigit in nextDigits:
                if 0 <= nextDigit < 10:
                    newDigit = num * 10 + nextDigit
                    backtrack(n - 1, newDigit)

        ans = []
        for num in range(1, 10):
            backtrack(n - 1, num)

        return ans


# Time complexity: O(2^n)
# Space complexity: O(2^n)