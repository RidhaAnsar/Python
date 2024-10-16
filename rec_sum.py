def rec(n):
    if n==0:
        return 0
    else:
        return n+rec(n-1)
result=rec(10)
print(result)
