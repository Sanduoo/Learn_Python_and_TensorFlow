from math import *      #比起improt math可以省去math.~,可以直接调用

#变量
#String,number,bool,十进制实数decimal,序列sequence#
sName = "三多"        #转义字符 escape character"三\"多\""
sCountry = "China"
#"三多"就是一个字符序列（0）三|（1）多
nAge = 18
bIsMale = True

print("My name is:%s\nMy age is:%d"%(sName,nAge))       #slash \   backslash  /
print(f'My name is:{sName},My age is:{nAge}')           #f'｛｝，｛｝',字符串格式化
print("I am a Male:",bIsMale)
print(sName[0])

#字符串
print(sName+"is good boy")
print(sName*3)
print("s" in sName)         #return Ture/False
print(sCountry.islower())   #判断是否为大小写
print(sCountry.upper())
print(len(sName))
print(sName.index("多"))
print(sName.replace("三","四"))
print(sName.isdigit())
print(sName.isalpha())

#数字number
n1 = 5
n2 = 2
print(1.5e2)
print(2**3)
print(pow(2,3))
print(5%2)          #求模
print(n1%n2)
print(str(n1)+"数字")
print(abs(n2-n1))
print(max(4,3))     #min()
print(round(4.3))

#math
print(floor(4.5))
print(sqrt(5))

#input()
while(1):
    str = input("请输入：")
    if("吗" in str):
        print(str.replace("吗", "")+"，你呢？")
    elif("怎么样" in str):
        print(str.replace("怎么样","很好"))
    else:
        print("还不错，聊点别的吧")




