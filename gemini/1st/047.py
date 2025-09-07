def abc(s):
    if s=='':
        return ['']
    f=s[0]
    nxt=abc(s[1:])
    new=[]
    for e in nxt:
        new.append(f+e)
    return nxt+new
    
print(abc('abc'))