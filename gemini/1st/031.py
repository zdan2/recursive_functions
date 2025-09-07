def bin_ser(arr,target,l=0,r=float('inf')):
    if r==float('inf'):
        r=len(arr)-1
    mid=(l+r)//2
    if arr[mid]==target:
        return mid
    if l>=r:
        return -1
    if arr[mid]<target:
        l=mid+1
    else:
        r=mid-1
    return bin_ser(arr,target,l,r)

print(bin_ser([1,2,3,4,5,10,15],11))