

#def
def sayHello(name,age):
    print("hello "+name+",your age:"+str(age))

sayHello("SanDuo",1)

lFriend = ["yiduo","erduo","sanduo"]
lAge = [1,2,3,4]
sayHello(lFriend[1],lAge[1])

#return
def nDouble_Nmuber(num):
    return num*2

print(nDouble_Nmuber(5))

#loqical operators:and/or/and not
bIs_Good_Singer = False
bIs_Good_Dancer = True
if bIs_Good_Dancer and bIs_Good_Singer:
    print("and")
if bIs_Good_Dancer and not bIs_Good_Singer:
    print("and not")
if bIs_Good_Dancer or bIs_Good_Singer:
    print("or")

#comparison operators:>/>=/</<=/==/!=

#for loop
for item in "Apple":
    print(item)

for item in ["yiduo","erduo","sanduo"]:
    print(item)

for i in range(10,20):
    print(i)

for i in range(1,20,2):
    print(i)

#mested loop
lNum1 = [1,2,3,4]
lNum2 = [5,6,7,8]

for num1 in lNum1:
    for num2 in lNum2:
        print(f'({num1},{num2})')