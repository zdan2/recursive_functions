def ep_sum(a,d,n):
    if n==0:
        return a
    return a*d**(n-1)+ep_sum(a,d,n-1)

print(ep_sum(5,5,5))