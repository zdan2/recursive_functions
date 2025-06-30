def com_arr(arr):
    if len(arr)==1:
        return arr[0]
    return com_arr([arr[0]+arr[1]]+arr[2:])

print(com_arr([[1,2],[3],[4,5]]))