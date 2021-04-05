#du = ['com', 'info', 'smart', 'secu']
import pickle
#f = open('dupickle.bin', 'wb')
#pickle.dump(du, f)
#f.close()
#f = open('dupickle.bin', 'rb')
#du2 = pickle.load(f)
#f.close()
#print(du2)
class duclass:
    var = None
instance2 = duclass()
instance2.var = 'computer imformation'
f = open('duclass2.bin', 'wb')
pickle.dump(instance2, f)
f.close()
f = open('duclass2.bin', 'rb')
instance1 = pickle.load(f)
f.close() 
print(instance1.var)