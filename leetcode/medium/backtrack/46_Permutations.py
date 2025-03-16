class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(i):
            if i == len(nums):
                return [[]]
            
            resPerms = []
            perms = backtrack(i + 1)
            print(perms, i)

            for p in perms:
                for j in range(len(p) + 1):
                    pCopy = p.copy()
                    pCopy.insert(j, nums[i])
                    resPerms.append(pCopy)
            return resPerms

        return backtrack(0)

# Time complexity: O(n^2 * n!)
# Space complexity: O(n^2 * n!)