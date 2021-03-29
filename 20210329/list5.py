L = [1, 2, 3]
def Add10(i):
    return i+10
for i in map(Add10, L):
    print("Item: {0}".format(i))
X = [1, 2, 3]
Y = [2, 3, 4]
print(list(map(pow, X,  Y)))