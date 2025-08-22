def outer(n):
    def inner(n):
        return n+3
    ans=inner(n)
    print(ans)

n=int(input("enter num: "))
outer(n)