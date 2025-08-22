def test(n):
    return lambda a:a*n

ans = test(5)
print(ans(2))