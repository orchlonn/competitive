class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        L, res = 0, 0
        q = deque()

        for R in range(len(arr)):
            if R - L + 1 > k:
                L += 1
                q.popleft()
            
            q.append(arr[R])
            if R - L + 1 == k and sum(q) // k >= threshold:
                res += 1
            
        return res

# Time complexity: O(N^2)
# Time complexity: O(K)

# Solution #2:
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        L, res = 0, 0
        cur_sum = sum(arr[0:k - 1])

        for L in range(len(arr) - k + 1):
            cur_sum += arr[L + k - 1]
            if cur_sum // k >= threshold:
                res += 1

            cur_sum -= arr[L]
        
        return res

# Time complexity: O(N)
# Time complexity: O(1)