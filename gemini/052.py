def part_sum(arr,target,w=0):
    if arr==[]:
        return False
        
    if w==target:
        return True
    f=arr[0]
    rest=arr[1:]

    return part_sum(rest, target, w + f) or part_sum(rest, target, w)

arr=[1,2,3,4,5]
print(part_sum(arr,10))