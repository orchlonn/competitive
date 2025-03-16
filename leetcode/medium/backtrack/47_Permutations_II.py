class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(i):
            if i == len(nums):
                return [[]]
            
            resPerms = []
            perms = backtrack(i + 1)

            for p in perms:
                for j in range(len(p) + 1):
                    pCopy = p.copy()
                    pCopy.insert(j, nums[i])
                    if pCopy not in resPerms:
                        resPerms.append(pCopy)
            
            return resPerms
        
        return backtrack(0)

# Time complexitiy: O(n^2 * n!)
# Space complexitiy: O(n^2 * n!)