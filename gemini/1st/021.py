def coraz(n):
    if n==1:
        return 0
    if n%2==0:
        return 1+coraz(n//2)
    else:
        return 1+coraz(3*n+1)

print(coraz(105))

    