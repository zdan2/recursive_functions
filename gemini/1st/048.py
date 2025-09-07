def bracket_set(n,l=0,r=0,b=None):
    if b==None:
        yield from bracket_set(n,l+1,r,'(')
        return
    if r==l==n:
        yield b
        return
    if l<n:
        yield from bracket_set(n,l+1,r,b+'(')
    if r<l:
        yield from bracket_set(n,l,r+1,b+')')
        
r=[]
for e in bracket_set(3):
    r.append(e)
print(r)