def quick_sort(arr):
    a=arr.copy()
    if len(a)<=1:
        return a
    pivot=a[0]
    left=[e for e in a if e<pivot]
    mid=[e for e in a if e==pivot]
    right=[e for e in a if e>pivot]
    return quick_sort(left)+mid+quick_sort(right)

print(quick_sort([1,5,2,6,4,9,8,7]))