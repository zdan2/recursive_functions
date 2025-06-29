def sum_nums(n):
    if n==0:
        return 0
    return n+sum_nums(n-1)

if __name__ == "__main__":
    print(sum_nums(5))