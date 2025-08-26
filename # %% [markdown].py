# %% [markdown]
# R1
# 仕様: n==0 → 1。n は 0〜12 程度でテスト。
# 
# サンプル: factorial(5) == 120

# %%
def factorials(n):
    if n==0:#ベースケース
        return 1
    return n*factorials(n-1)

factorials(5)

# %% [markdown]
# R2 sum_digits(n)
# 
# 仕様: 負数は絶対値で扱う。
# 
# サンプル: sum_digits(490) == 13

# %%
def sum_digits(num):
    num=abs(num)
    if num==0:#Base case
        return 0
    return num%10+sum_digits(num//10)

sum_digits(-490)
    

# %% [markdown]
# R3 reverse_str(s)
# 
# 仕様: スライス（s[::-1]）禁止、再帰で。
# 
# サンプル: reverse_str("recursion") == "noisrucer"

# %%
def reverse_str(s):
    if s=='':#Base case
        return ''
    return s[-1]+reverse_str(s[:-1])

reverse_str("recursion")

# %% [markdown]
# R4 is_sorted(a)
# 
# 仕様: 厳密昇順（a[i] < a[i+1]）。長さ0,1は True。
# 
# サンプル: is_sorted([1,2,3]) == True, is_sorted([1,1]) == False

# %%
def is_sorted(a):
    if len(a)==0 or len(a)==1:#仕様
        return True
    if a[0]>=a[1]:#大きかったらだめ
        return False
    return is_sorted(a[1:])

is_sorted([1,2,1])

# %% [markdown]
# R5 bin_search(a, x)
# 
# 仕様: 昇順配列 a。見つからなければ -1。
# 
# サンプル: bin_search([1,3,4,8,10], 8) == 3, bin_search([1,3,4], 2) == -1

# %%
def bin_search(a, x, l = 0, r = None):
    if r is None:
        r=len(a)
    mid=(l+r)//2
    if a[mid]==x:#Base case
        return mid
    if l>=r:
        return -1
    if a[mid]>x:
        return bin_search(a,x,l,mid-1)
    else:
        return bin_search(a,x,mid+1,r)

bin_search([1,3,4,8,10], 8)
bin_search([1,3,4], 2)

# %% [markdown]
# R6 pow_rec(a, b)
# 
# 仕様: 繰り返し禁止・再帰で（まずは線形版）。後日 R13 で高速化。
# 
# サンプル: pow_rec(2, 5) == 32, pow_rec(7, 0) == 1

# %%
def pow_rec(a,b):
    if b==0:
        return 1
    if b%2==1:
        return a*pow_rec(a,b//2)*pow_rec(a,b//2)
    else:
        return pow_rec(a,b//2)*pow_rec(a,b//2)

pow_rec(2,5)
pow_rec(7,0)


