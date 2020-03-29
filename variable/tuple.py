#元祖 tuple
"""
list和tuple的关系
相同点：都是序列 都可以存储任何数据类型 可以通过索引访问
语法差异；使用方括号[]创建列表，而使用括号()创建元组
重用与拷贝：元组无法复制。原因是元组是不可变的。如果运行tuple(tuple_name)将返回自己

可以修改列表的值，但是不修改元组的值
不能将列表用作字典中的key，但可以使用元组作为字典key（hash值不变）

大小差异：Python将低开销的较大的块分配给元组，因为它们是不可变的，列表的长度是可变的。
        对于列表则分配小内存块。
        与列表相比，元组的内存更小。
        当你拥有大量元素时，元组比列表快。
"""
#不可变的tuple有什么意义？因为tuple不可变，所以代码更安全。
#如果可能，能用tuple代替list就尽量用tuple。
#tuple的陷阱：当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来

tCompany = ("Google","Microsoft","Alibaba","Tencent")
lCompany = ["Google","Microsoft","Alibaba","Tencent"]
tup1 =(1,)

print(tCompany[0])
tup2 = tup1+tCompany
print(tup2)
#del tup2
#print(cmp(tup2,tup1))
print(len(tup2))
print(max(tup1))
tCompany2 = tuple(lCompany)
print(tCompany2)

#如何创建一个“可变”的元祖
t = ('a','b','c',['A','B','C'])         #此时元祖只有四个元素
print(t)
t[3][0] = 'X'
t[3][1] = 'Y'
t[3][2] = 'Z'
print(t)

"""
为何此时元祖会改变？
其实元祖不变指的是元祖元素指向不变，
所以t中的第四个元素为list时，
我们改变的是list中的元素，而不是元祖中元素的指向
且元祖中元素的指向并不变
"""
