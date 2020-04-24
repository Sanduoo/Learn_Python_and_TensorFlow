"""
extend
append
insert
remove
clear
pop
index
count
sort
reverse
copy
"""

#list 列表
lFruits = ["苹果","apple",True,109.1]
lNum = [1,4,9,16,25,36]
#           0       1       2   3
#           -4      -3      -2  -1
#index
print(lFruits)
print(lFruits[2])
print(lFruits[-3])          #反向索引从-1开始

#slice-切片
print(lFruits[1:3])

#替换
lFruits[0] = "apple"
print(lFruits)

#extend追加
lNum.extend(lFruits)
print(lNum)

#append
lFruits.append("grape")
print(lFruits)

#insert
lFruits.insert(0,"Apple")
print(lFruits)

#remove
lFruits.remove(109.1)
print(lFruits)

#clear清空
#lNum.clear()
print(lNum)

#pop 最后一个清除
lFruits.pop(3)
print(lFruits)
print(lFruits.index("apple"))

#count()查找列表中某个元素的个数
print(lFruits.count("apple"))

#sort排序 reverse反转
print(lNum)
#lNum.sort()
lNum.reverse()
print(lNum)

lNum2 = lNum.copy()
print(lNum2)