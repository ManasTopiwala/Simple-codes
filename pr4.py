#write a program to increase value by 3 using func decorator
def outer(n):
    def inner(n):
        return n+3
    ans=inner(n)
    print(ans)
    
