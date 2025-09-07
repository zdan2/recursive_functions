def flatten(arr,r=[]):
    if arr==[]:
        return r
    for e in arr:
        if isinstance(e,list):
            flatten(e,r)
        else:
            r.append(e)
    return r

arr=[1, [2, [3, 4], 5],[10,[7,8],[9,6]]]
print(flatten(arr))