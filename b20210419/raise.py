class NegativeDivisionError(Exception):
    def __init__(self, value):
        self.value = value

def RaiseErrorFunc():
    raise NameError
    
def PositiveDivide(a, b):
    if(b < 0):
        raise NegativeDivisionError(b)
    return a / b

try:
    ret = PositiveDivide(10, -3)
    print('10 / 3 = {0}'.format(ret))
except NegativeDivisionError as e: # 사용자 정의 예외인 경우
    print('Error - Second argument of PositiveDivide is ', e.value)
except ZeroDivisionError as e: # '0'으로 나누는 경우
    print('Error - ', e.args[0])
except : # 그 외 모든 예외의 경우
    print(e.args)
#try:
#    RaiseErrorFunc()
#except: 
#    print("NameError is Catched")