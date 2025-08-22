def fact(n):
    if(n==1):
        return 1
    else:
        x=n*fact(n-1)
    return x

n=int(input("enter num: "))
ans=fact(n)
print(ans)