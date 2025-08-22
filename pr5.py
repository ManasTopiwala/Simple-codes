def test(x):
    global a
    a=a+x
    print("function a= ",a)
    
a=30
print("a=",a)
test(80)
print("a=",a)