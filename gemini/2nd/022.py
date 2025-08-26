#022 パスカルの三角形の n 段目、k 番目の値を求める関数。

def pascal(n,k):
    '''
    パスカルの三角形の n 段目、k 番目の値を求める関数。
    再帰的に求める
    0baseのインデックスで実装
    '''
    if k>n or n<0 or k<0:
        return 0
    elif n==0 or n==k:
        return 1
    
    return pascal(n-1,k-1)+pascal(n-1,k)

print(pascal(0,0))
print(pascal(1,0))
print(pascal(1,1))
print(pascal(2,0))
print(pascal(2,1))
print(pascal(2,2))
print(pascal(3,0))
print(pascal(3,1))
print(pascal(3,2))
print(pascal(3,3))