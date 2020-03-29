#模块 module
import Class            #现在目录查找，未找到则去PYTHONPATH环境变量查找
import sys
from Class import Friend
from Class import my_name as uname
#from Class improt *        #自定义会替换模块
import Class as C

print(C.my_name)
print(Class.my_name)
print(Class.name_list)
print(uname)

jack =Class.Staff("JacKK",222,"male")
jack.who_am_i()

#for line in sys.path:
    #print(line)

mark = Friend("Mark",26,"Male")
mark.who_am_i()

def foo():
    import sys
    print(sys.path)
foo()

#dir
print(dir())
print(dir(C))