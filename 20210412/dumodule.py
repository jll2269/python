class duclass():
    def dufunc1():
        f = open("dulist.txt",'r',encoding='UTF8')
        while 1:
            line = f.readline()
            line = line.rstrip()
            if not line: break
            print(line)
        f.close()
        
    def dufunc2():
        f = open("dulist.txt",'r',encoding='UTF8')
        lines = f.readlines()
        for line in lines:
            line = line.rstrip()
        if not line: break
            print(line)
        f.close()