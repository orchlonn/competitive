def constains_duplicate(arr):
    dic = {}
   
    for i in range(len(arr)):
        if arr[i] in dic:
            return True 
        else: 
            dic[i] = arr[i]
            
    return False

print(constains_duplicate([3,3]))