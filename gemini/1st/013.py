def find_max(arr,m=float('inf')):
    if len(arr)==0:
        return m
    if arr[0]<m:
        m=arr[0]
    return find_max(arr[1:],m)

print(find_max([1,5,3,4,7,2,1]))