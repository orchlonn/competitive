def largestUniqueNumber(self, nums: List[int]) -> int:
    # create default counter dictionary
    counter = {}
    
    for num in nums:
        counter[num] = counter.get(num, 0) + 1

    result = -1
    for num, count in counter.items():
        if count == 1:
            result = max(result, num)

    return result