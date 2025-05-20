class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        def dfs(i, one_sum, zero_sum):
            if i >= len(strs):
                return 0
            
            if (i, one_sum, zero_sum) in cache:
                return cache[(i, one_sum, zero_sum)]
            
            ones = strs[i].count('1')
            zeros = strs[i].count('0')
            
            take = 0
            if ones + one_sum <= n and zeros + zero_sum <= m:
                # include element i
                take = 1 + dfs(i + 1, ones + one_sum, zeros + zero_sum)
            # skip el i
            skip = dfs(i + 1, one_sum, zero_sum)

            cache[(i, one_sum, zero_sum)] = max(take, skip)
            return cache[(i, one_sum, zero_sum)]
            
        cache = {}
        return dfs(0, 0, 0)

# | Complexity Type  | Value        |
# | ---------------- | ------------ |
# | Time Complexity  | O(L * m * n) |
# | Space Complexity | O(L * m * n) |

#  Because for each state (i, one_sum, zero_sum) you do constant work (either take or skip).

