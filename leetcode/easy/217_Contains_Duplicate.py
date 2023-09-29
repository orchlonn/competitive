from collections import Counter

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counter = Counter(nums)
        
        for i in nums:
            if counter[i] > 1:
                return True
        
        return False

class Solution2:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashSet = set()

        for i in nums:
            if i in hashSet:
                return True
        
            hashSet.add(i)
        
        return False
