def ed_sum(a,d,n):
    if n==0:
        return a
    return a+d*(n-1)+ed_sum(a,d,n-1)

print(ed_sum(5,5,5))