n=[45,67,78,34,45,65,76]
no=int(input("enter number you want to find: "))
cnt=0
for i in range(0,len(n)):
    if(n[i]==no):
        print("no is at =",i)
    cnt+=1
    
if(cnt==0):
    print("the list is empty")
else:
    print("there are ",cnt,"elements")
