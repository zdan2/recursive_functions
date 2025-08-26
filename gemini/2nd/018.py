#18　整数 n の各桁の数字の和を求める関数 (例: 123 -> 1+2+3=6)。

def add_n(num):
    '''
    数字の各桁の和
    １０で割ったあまりを足していく計算を再帰関数で行う
    '''
    if num < 10:
        return num
    else:
        return num % 10 + add_n(num // 10)

assert add_n(123) == 6
assert add_n(49) == 13
assert add_n(11) == 2

print('OK')