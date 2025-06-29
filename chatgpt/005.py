def count_length(arr):
    if not arr:
        return 0
    return 1+count_length(arr[1:])
if __name__ == "__main__":
    print(count_length([1,2,3,4,5,6,7]))