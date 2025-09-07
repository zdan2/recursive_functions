def count_down(n):
    if n==0:
        return print(0)
    print(n)
    return count_down(n-1)

if __name__=='__main__':
    count_down(10)