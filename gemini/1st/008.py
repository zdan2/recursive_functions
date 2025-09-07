def head(arr):
    if len(arr)==0:
        return
    print(arr[0])
    return head(arr[1:])

head([1,2,3,4,5])