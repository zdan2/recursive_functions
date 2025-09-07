def c_bin(n):
    if n==1:
        return '1'
    return c_bin(n//2)+str(n%2)

print(c_bin(15))