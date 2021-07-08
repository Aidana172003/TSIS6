def fact(n):
    if n==0:
        return 1
    total=1
    for i in range(n):
        total*=n
        n=n-1
    return total
print(fact(5))