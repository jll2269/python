 #f = open('du.txt', 'w')
#f.write('computer\nand information')
#f.close() 
#f = open('du.txt')
#du = f.close
#f.read(du)
#'computer\nand information'
# f.close()
#print(f.closed)
 with open('du.txt') as f :
    print( f.readlines() )
    print( f.closed )
['computer\nand information']
print(f.closed)
