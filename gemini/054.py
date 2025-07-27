def lev(s, t):
    if s == "":
        return len(t)
    if t == "":
        return len(s)

    if s[0] == t[0]:
        return lev(s[1:], t[1:])
    else:
        return min(1 + lev(s[1:], t[1:]), lev(s[1:], t) + 1, lev(s, t[1:]) + 1)


print(lev("jellyfish", "ssssmellyfish"))
