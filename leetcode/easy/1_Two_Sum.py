class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res_map = {}
        
        for index, value in enumerate(nums):
            temp = target - value

            if temp in res_map:
                return [res_map[temp], index]
            
            res_map[value] = index
        
        return 