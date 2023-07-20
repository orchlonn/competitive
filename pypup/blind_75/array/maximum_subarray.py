def maximum_subarray(arr):
    maxSub = nums[0]
    curSum = 0
    
    for i in arr:
        if(curSum < 0):
            curSum = 0
        curSum += arr[i]
        maxSub = max(maxSub, curSum)
        
    return maxSub
        
