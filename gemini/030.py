import sys
sys.setrecursionlimit(100000000)

def ackermann(m,n):
    if m==0:
        return n+1
    if n==0:
        return ackermann(m-1,1)
    return ackermann(m-1,ackermann(m,n-1))

print(ackermann(4,2))