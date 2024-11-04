class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(comb, counter):
            if len(comb) == len(nums):
                ans.append(list(comb))
                return
            
            for num in nums:
                if counter[nums] > 0:
                    comb.append(num)
                    counter[nums] -= 1
                    backtrack(comb, counter)
                    # bacltrack 
                    comb.pop()
                    counter[num] += 1

        ans = []
        backtrack([], Counter(nums))
        return ans