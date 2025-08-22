def test(*args):
    for x in range(0,len(args)):
        print(args[x])

test(45,67,78)
test()
test(34,56)