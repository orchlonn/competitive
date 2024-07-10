class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        one, zero = 0, 0
        res = 0

        diff_index = {}

        for i, n in enumerate(nums):
            if n == 0:
                zero += 1
            else: 
                one += 1
            
            if one - zero not in diff_index: # checking if index not in diff_index
                diff_index[one - zero] = i
            
            if one == zero:
                res = one + zero
            else:
                idx = diff_index[one - zero] # if number of 1 is greater than 0, take the extra one off from the index
                res = max(res, i - idx)

        return res
