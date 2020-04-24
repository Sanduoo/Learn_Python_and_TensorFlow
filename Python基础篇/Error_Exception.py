#错误Error
#异常Exception

def iTest_Fails(num):
    return  1/num


try:
    iNum = int(input("please input number:"))
    Num = iTest_Fails(iNum)
    print(Num)
except ZeroDivisionError as error:
    print("ZeroDivisionError")
    print(error)
except ValueError as error:
    print("ValueError")
    print(error)