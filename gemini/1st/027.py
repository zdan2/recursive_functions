def count_upper(s):
    if s=='':
        return 0
    return s[0].isupper()+count_upper(s[1:])

print(count_upper('Hello,WORLD!!'))