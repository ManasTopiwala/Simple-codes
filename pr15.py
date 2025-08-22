name=input("enter name: ")
def revfun(name):
    rev=name[::-1]
    print(name)
    print(rev)
    if(name==rev):
        print("pallindrome")
    else:
        print("not a pallindrome")

revfun(name)