f = open('20210405/dulist.txt','rt',encoding='UTF8')
for line in f :
    if line.find('정보보안') == -1 :
        continue
    print(line)
fname = input('Enter the file name: ')
try:
    f = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()