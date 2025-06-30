def kuri(a,n):
    if n==0:
        return 1
    if n==1:
        return a
    h=kuri(a,n//2)
    if n%2==0:
        return h*h
    else:
        return a*h*h

print(kuri(2,10))
print(kuri(5,13))