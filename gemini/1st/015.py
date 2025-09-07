def count_arr(arr,x,c=0):
    if len(arr)==0:
        return c
    if arr[0]==x:
        c+=1
    return count_arr(arr[1:],x,c)

print(count_arr([1,0,0,0,1,1,1,1],0))