# 10進数の整数を2進数の文字列に変換する関数。

def to_binary(n):
    '''
    10進数を2進数文字列に変換する。
    再帰関数を使うので、2で割ったあまりを累積して文字列を作る
    '''
    if n == 0:
        return '0'
    if n == 1:
        return '1'
    
    return to_binary(n // 2) + str(n % 2)

assert to_binary(0) == '0'
assert to_binary(1) == '1'
assert to_binary(2) == '10'
assert to_binary(3) == '11'
assert to_binary(4) == '100'
assert to_binary(5) == '101'
assert to_binary(6) == '110'
assert to_binary(7) == '111'
assert to_binary(8) == '1000'
assert to_binary(9) == '1001'   

print('OK')