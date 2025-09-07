def count_length(s):
    if s=='':
        return 0
    return 1+count_length(s[1:])

print(count_length('Hello'))