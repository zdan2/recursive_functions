def beki(x,n,r=1):
    if n==0:
        return r
    return beki(x,n-1,r*x)

print(beki(2,5))
