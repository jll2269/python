L = [10, 25, 30]
IterL = filter(None, L)
for i in IterL:
print("Item: {0}".format(i))

def GetBiggerThan20(i):
return i > 20
print(list(filter(GetBiggerThan20, L)))
print(list(filter(lambda i: i>20, L)))