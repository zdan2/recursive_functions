s=set()
def f(arr,i,cur=0):
    if i==len(arr):
        s.add(cur)
        return
    f(arr,i+1,cur)
    f(arr,i+1,cur+arr[i])

n=int(input())
arr=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))
f(arr,0)
for e in b:
    print('yes' if e in s else 'no')