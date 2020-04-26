# LearnPython  
2020-03-29  
重新学习一下Python基础  
会包含基本类型、常见的一些操作  
目的是为了重新熟练起来Pyhton的操作  
细细想来距离上一次写Python，已经有一段日子了  

### list和tuple的关系  
#### 相同点：  
都是序列都可以存储任何数据类型 可以通过索引访问  
#### 语法差异：  
使用方括号[]创建列表，而使用括号()创建元组  
#### 重用与拷贝：  
元组无法复制。原因是元组是不可变的。如果运行tuple(tuple_name)将返回自己  
  
可以修改列表的值，但是不修改元组的值  
不能将列表用作字典中的key，但可以使用元组作为字典key（hash值不变）  
  
#### 大小差异：  
Python将低开销的较大的块分配给元组，因为它们是不可变的，列表的长度是可变的。  
对于列表则分配小内存块。  
与列表相比，元组的内存更小。  
当你拥有大量元素时，元组比列表快。  
  
不可变的tuple有什么意义？因为tuple不可变，所以代码更安全。  
如果可能，能用tuple代替list就尽量用tuple。  
#### tuple的陷阱：  
当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来  
  
### 一个“可变”的元组  
  
如何创建一个“可变”的元组  
```
t = ('a','b','c',['A','B','C'])         此时元组只有四个元素
print(t)
t[3][0] = 'X'
t[3][1] = 'Y'
t[3][2] = 'Z'
print(t)
```
为何此时元组会改变？
其实元组不变指的是元组元素指向不变，
所以t中的第四个元素为list时，
我们改变的是list中的元素，而不是元组中元素的指向
且元组中元素的指向并不变
</h1>

# 目录  

## 基础篇  
可以作为Python的入门  

1.[变量与数据类型VariableAndDatetype](https://github.com/Sanduoo/LearnPython/tree/master/variable)  
2.[函数Function](https://github.com/Sanduoo/LearnPython/tree/master/def)  
3.[解包Unpacking](https://github.com/Sanduoo/LearnPython/blob/master/Unpacking.py)  
4.[异常处理Exception](https://github.com/Sanduoo/LearnPython/blob/master/Error_Exception.py)  
5.[文件操作FileOperator](https://github.com/Sanduoo/LearnPython/blob/master/FileOperator.py)  
6.[类Class、构造函数Constructor、类函数ClassFunction、继承inheritance](https://github.com/Sanduoo/LearnPython/blob/master/Class.py)  
7.[模块Module1](https://github.com/Sanduoo/LearnPython/blob/master/module.py)  
8.[模块Module2](https://github.com/Sanduoo/LearnPython/blob/master/module2.py)  
9.[包Package](https://github.com/Sanduoo/LearnPython/blob/master/packages.py)  
****
  
环境：Anaconda、TensorFlow2.1  
编辑器：Jupyter Notebook  
配合[【北京大学】Tensorflow学习笔记，从零基础入门到项目实战分享学习教程](https://www.bilibili.com/video/BV1GE411k7Q2)使用
## TensorFlow篇   
  
1.[张量Tensor和常用函数](https://github.com/Sanduoo/LearnPython/blob/master/TensoFlow%E7%AF%87/1.1_Tensor_Graph_Session.ipynb)  
2.[前向传播](https://github.com/Sanduoo/LearnPython/blob/master/TensoFlow%E7%AF%87/1.2_%E5%89%8D%E5%90%91%E4%BC%A0%E6%92%AD.ipynb)  
3.[反向传播](https://github.com/Sanduoo/LearnPython/blob/master/TensoFlow%E7%AF%87/1.3%E5%8F%8D%E5%90%91%E4%BC%A0%E6%92%AD.ipynb)  
4.[损失函数](https://github.com/Sanduoo/LearnPython/blob/master/TensoFlow%E7%AF%87/1.4%E6%8D%9F%E5%A4%B1%E5%87%BD%E6%95%B0.ipynb)  
5.[指数衰减学习率](https://github.com/Sanduoo/LearnPython/blob/master/TensoFlow%E7%AF%87/1.5%E6%8C%87%E6%95%B0%E8%A1%B0%E5%87%8F%E5%AD%A6%E4%B9%A0%E7%8E%87.ipynb)  
6.[滑动平均]()  