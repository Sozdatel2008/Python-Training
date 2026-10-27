def minimum(arr):
    tmp1 = arr[0]
    for x in arr:
        if x < tmp1:
            tmp1 = x
    return tmp1

def maximum(arr):
    tmp2 = arr[0]
    for x in arr:
        if x > tmp2:
            tmp2 = x
    return tmp2