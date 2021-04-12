class duclass():
    def dufunc3():
        f = open("dulist.txt",'r',encoding='UTF8')
        lines = f.read()
        print(lines)
        f.close()
    def dufunc4():
        with open("dulist.txt",'r',encoding='UTF8') as f:
            print(f.readlines())