n=int(input("enter the number of player you want to enter:"))
d={}
for i in range(n):
    name=input("enter name of the player: ")
    run=input("enter score: ")
    d[name]=run
    
print(d)
name=input("enter the player you want to find: ")
if name in d:
    print("score= ",d[name])
else:
    print("record not found")