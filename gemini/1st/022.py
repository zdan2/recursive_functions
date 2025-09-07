def pasc_tri(n,k):
    if k==0 or n==k:
        return 1
    return pasc_tri(n-1,k-1)+pasc_tri(n-1,k)

print(pasc_tri(4,2))