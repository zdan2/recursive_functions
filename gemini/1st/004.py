def add_nums(n):
    if n==0:
        return 0
    return n+add_nums(n-1)

print(add_nums(10))