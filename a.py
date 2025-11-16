a,b,k=map(int,input().split())

str='0'*a+'1'*b
a=int(str,2)
print(bin(a+(2**(b-1))*100))

