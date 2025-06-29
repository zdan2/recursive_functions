def euclidean_gcd(a,b):
    if b==0:
        return a
    return euclidean_gcd(b,a%b)

if __name__ == "__main__": 
    print(euclidean_gcd(10,15))