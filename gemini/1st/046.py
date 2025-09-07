def sum_num_path(m,n):
    if m==n==1:
        return 1
    if m>1 and n>1:
        return sum_num_path(m-1,n)+sum_num_path(m,n-1)
    if m>1 and n==1:
        return sum_num_path(m-1,1)
    if m==1 and n>1:
        return sum_num_path(1,n-1)
    

print(sum_num_path(5,5))