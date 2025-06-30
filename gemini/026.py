def rev_arr(arr):
    if len(arr)==1:
        return arr
    return [arr[-1]]+rev_arr(arr[:-1])

print(rev_arr([1,2,3,4,5]))
