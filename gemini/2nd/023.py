#023 n 個の円盤がある場合のハノイの塔の手順を出力する関数。

def hanoi(n, start, end, temp):
    '''
    ハノイの塔を再帰で実装
    手順を示すコードにする
    '''
    if n==1:
        print(f'{n}番目の円盤:from {start} to {end}')
        return
    hanoi(n-1,start,temp,end)
    print(f'{n}番目の円盤:from {start} to {end}')
    hanoi(n-1,temp,end,start)

hanoi(4,'左','右','中')