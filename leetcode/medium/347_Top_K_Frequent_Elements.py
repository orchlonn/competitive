class Solution:
    def topKFrequent(nums, k):
        numbers_hash = {}
        ans = []
        for i in nums:
            if i in numbers_hash:
                numbers_hash[i] += 1
            else:
                numbers_hash[i] = 1
        while k > len(ans) :
            max_key = max(numbers_hash, key=numbers_hash.get)
            ans.append(max_key)
            del numbers_hash[max_key]

        return ans
print(topKFrequent([1,1,1,2,2,3], 2))