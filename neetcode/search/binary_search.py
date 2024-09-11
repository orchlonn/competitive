def binary_search(sorted_arr, target):
        l, r = 0, len(sorted_arr) - 1

        while l <= r:
            mid = (l + r) // 2

            if sorted_arr[m] > target:
                r = mid - 1
            else if sorted_arr[m] < target:
                l = mid + 1
            else:
                 return mid
        
        return -1



# Find the exact number not the index
# low = 1, high = 100

# Binary search on some range of value
def binarySearch(low, high):

    while low <= high:
        mid = (low + high) // 2

        if isCorrect(mid) > 0:
            high = mid - 1
        elif isCorrect(mid) < 0:
            low = mid + 1
        else:
            return mid
    return -1

# Return 1 if n is too big, -1 if too small, 0 if correct
def isCorrect(n):
    if n > 10:
        return 1
    elif n < 10:
        return -1
    else:
        return 0
