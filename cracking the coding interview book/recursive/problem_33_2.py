def nested_array_sum(arr):
    res = 0
    for el in arr:
        if insinstance(el, int):
            res += el
        else:
            res += nested_array_sum(arr)
    return res