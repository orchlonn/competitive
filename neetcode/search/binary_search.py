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