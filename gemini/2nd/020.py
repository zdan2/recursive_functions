#020 [[1, 2], [3], [4, 5]] のようなリストを [1, 2, 3, 4, 5] に変換する関数。

def flatten(l):
    '''
    ネストしたリストの平坦化
    入れ子になったリストの要素を一つのリストに変換する
    再帰関数で実装する
    空間計算量をO(1)とする
    '''

    if l==[]:
        return []
    

    last_element=l.pop()
    if type(last_element)==list:
        return flatten(l)+flatten(last_element)
    else:
        return flatten(l)+[last_element]

print(flatten([[1,2],[3],[4,5]]))

assert flatten([[1,2],[3],[4,5]])==[1,2,3,4,5]
assert flatten([1,2,3,4,5])
