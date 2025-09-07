def find_parent(a,b):
    if a==b:
        return a
    if a>b:
        a,b=b,a
    return find_parent(a//2,b//2-1)

print(find_parent(7,10))