def x_inc(arr,x):
    if len(arr)==0:
        return False
    if arr[0]==x:
        return True
    return x_inc(arr[1:],x)

print(x_inc([1,2,3],3))