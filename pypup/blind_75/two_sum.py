def two_sum(nums, target):
    nums.sort()
    dic = {}
    for i in range(len(nums)):
        num = nums[i]
        complement = target - num

        if complement in dic:
            return [i, dic[complement]]

        dic[num] = i
        
def two_sum(nums, target):
    dic = {}
   
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in dic:
            return [dic[complement], i]
        
        dic[nums[i]] = i

    return []  


def two_sum(nums, target):
    nums.sort()
    a=[]
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if (nums[i]+nums[j]==target):
                a.append(i)
                a.append(j)
                break
            else:
                continue    
             
        if len(a) == 2:
            return a 
        
    return a