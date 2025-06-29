def convert_to_binary(n):
    if n==0:
        return ""
    return convert_to_binary(n//2)+str(n%2)
if __name__ == "__main__":
    print(convert_to_binary(10))