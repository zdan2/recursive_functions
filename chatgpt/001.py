def factoral(n):
    if n==1:
        return 1
    return n*factoral(n-1)

if __name__ == "__main__":
    print(factoral(5))