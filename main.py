from b20210419 import module1
module1.Duclass.divide(6,1)
try:
    c = module1.Duclass.divide(6,0)
except (ZeroDivisionError, OverflowError, FloatingPointError):
    print('arithmetic error')
except TypeError as e:
    print('error: ' , e.args[0])
else :
    print('Result: {0}'.format(c))
finally :
    print('unknown error')