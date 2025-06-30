def rep_show(s,n):
    if n==0:
        return
    rep_show(s,n-1)
    print(s)

rep_show('Hello',5)