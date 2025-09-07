def fib_memo(n,memo={0:0,1:1}):
    if n in memo:
        return memo[n]
    else:
        memo[n]=fib_memo(n-1,memo)+fib_memo(n-2,memo)
    return fib_memo(n-1,memo)+fib_memo(n-2,memo)

print(fib_memo(10))
