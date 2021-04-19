import sys
print("sys.flags.debug =",sys.flags.debug)
print("sys.flags.optimize = ",sys.flags.optimize)
print("__debug__ = ", __debug__)

def foo(x):
    assert type(x) == int, "Input value must be integer" # 받은인자의type이 정수형인지검사
    return x*10
ret = foo("a") # AssertionError가 발생
    print(ret)