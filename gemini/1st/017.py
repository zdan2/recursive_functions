def check_pari(s):
    if len(s)<2:
        return True
    if s[0]!=s[-1]:
        return False
    return check_pari(s[1:-1])

print(check_pari('ABCCBA'))