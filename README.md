# LearnPython  
2020-03-29  
重新学习一下Python基础  
会包含基本类型、常见的一些操作  
目的是为了重新熟练起来Pyhton的操作  
细细想来距离上一次写Python，已经有一段日子了  
****
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
  
不可变的tuple有什么意义？因为tuple不可变，所以代码更安全。  
如果可能，能用tuple代替list就尽量用tuple。  
tuple的陷阱：当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来  
  
###一个“可变”的元组###  
例图  
![Image text](https://github.com/Sanduoo/LearnPython/blob/master/variable/tuple.jpg)  
****
目录  
****  
1.[常用数据类型](https://github.com/Sanduoo/LearnPython/tree/master/variable)  
2.[函数](https://github.com/Sanduoo/LearnPython/tree/master/def)

