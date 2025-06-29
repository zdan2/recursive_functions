def find_max(arr):
    if len(arr)==1:
        return arr[0]
    return max(arr[0],find_max(arr[1:]))
if __name__ == "__main__":
    print(find_max([10,2,3,4,5]))