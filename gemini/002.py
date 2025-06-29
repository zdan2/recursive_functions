def count_up(n,i=0):
    if n==i:
        return print(n)
    print(i)
    return count_up(n,i+1)

if __name__=='__main__':
    count_up(10)