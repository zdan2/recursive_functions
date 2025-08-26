#024 Lv.6の問題をメモ化（計算結果を保存）して効率化する。

def fib_memo(n,memo=None):
    '''
    フィボナッチ数列をメモで計算量（スタック領域）を減らす
    '''
    if memo is None:
        memo = {0:1,1:1}
    if n in memo:
        return memo[n]
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]

print(fib_memo(5))