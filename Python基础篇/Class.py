#类  class
#实例 实体 instance

"""
class Student:
    pass

sanduo = Student()
sanduo.name = "SanDuo"
#print(sanduo.name)

"""
my_name = "sanduo"
name_list = ["yiduo","erduo","sanduo"]
#构造函数 constructor
#封装
class Person:
    def __init__(self,name,age,sex):     #self指向实例本身：
                            # 例如sanduo = Frined(),此时self指向sanduo
        self.__name = name
        self.__age = age
        self.__sex = sex
        print("__init__ is run")

    #class的内部函数
    def who_am_i(self):
        print(f'{self.__name}-{self.__age}-{self.__sex}')

    def get_name(self):
        return  self.__name
    def set_name(self,name):
        self.__name = name

    def get_age(self):
        return  self.__age
    def set_age(self,age):
        self.__age = age

    def get_sex(self):
        return  self.__sex
    def set_sex(self,sex):
        self.__sex = sex

"""
sanduo = Person("SanDuo",20,"male")
yiduo = Person("YiDuo",25,"male")
erduo = Person("ErDuo",22,"male")

#erduo.name = "EErDuo"           #class内部的属性可以被外部访问（__name就无法访问）
erduo.set_name("EErDuo")
sanduo.who_am_i()
print(erduo.get_name())

#继承 inheritance
sanduo.set_name("SSanDuo")
sanduo.set_age(30)
"""
class Friend(Person):
    def who_am_i(self):         #override 重写
        print(f"i am your friend,{self.get_name()}|{self.get_age()}|{self.get_sex()}")
    def play(self):
        print("happy play")

class Staff(Person):
    def work(self):
        print("happy work")

print(__name__)
if(__name__ == "__main__"):     #当name属性为main时则会执行

    jack = Staff("Jack",33,"male")
    jack.who_am_i()
    jack.work()


