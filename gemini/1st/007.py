def rev_str(s):
    if len(s)==0:
        return 
    rev_str(s[1:])
    print(s[0])

rev_str('Hello')