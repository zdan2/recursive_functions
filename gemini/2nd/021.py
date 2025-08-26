#021　任意の正の整数nについて、nが偶数ならn/2、奇数なら3n+1の操作を繰り返し、1になるまでのステップ数を数える関数。
def steps(n):
    '''
    コラッツの予想についてステップ数を再帰的に調べる
    '''
    if n == 1:
        return 0
    if n % 2 == 0:
        return 1 + steps(n // 2)
    if n % 2 == 1:
        return 1 + steps(3 * n + 1)

res=[]
for i in range(1,101):
    res.append((i,steps(i)))

print(res)
