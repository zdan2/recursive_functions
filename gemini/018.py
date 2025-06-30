def sum_int(n):
    s=str(n)
    if s=='':
        return 0
    return int(s[0])+sum_int(s[1:])

print(sum_int(1234))