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
  

## TensorFlow篇   

环境：Anaconda、TensorFlow2.1  
编辑器：Jupyter Notebook  
配合[【北京大学】Tensorflow学习笔记](https://www.icourse163.org/course/PKU-1002536002)使用
  
##### 第一篇 神经网络计算与优化
1.[张量Tensor和常用函数](https://github.com/Sanduoo/LearnPython/blob/master/TensoFlow%E7%AF%87/1.1_%E5%BC%A0%E9%87%8FTensor%E5%8F%8A%E5%B8%B8%E7%94%A8%E5%87%BD%E6%95%B0.ipynb)  
2.[神经网络实现鸢尾花分类](https://github.com/Sanduoo/LearnPython/blob/master/TensoFlow%E7%AF%87/1.2_%E7%A5%9E%E7%BB%8F%E7%BD%91%E7%BB%9C%E5%AE%9E%E7%8E%B0%E9%B8%A2%E5%B0%BE%E8%8A%B1%E5%88%86%E7%B1%BB.ipynb)  
3.[复杂度、学习率、激活函数、损失函数](https://github.com/Sanduoo/LearnPython/blob/master/TensoFlow%E7%AF%87/1.3_%E5%A4%8D%E6%9D%82%E5%BA%A6%E3%80%81%E5%AD%A6%E4%B9%A0%E7%8E%87%E3%80%81%E6%BF%80%E6%B4%BB%E5%87%BD%E6%95%B0%E3%80%81%E6%8D%9F%E5%A4%B1%E5%87%BD%E6%95%B0.ipynb)  
4.[缓解过拟合](https://github.com/Sanduoo/LearnPython/blob/master/TensoFlow%E7%AF%87/1.4_%E7%BC%93%E8%A7%A3%E8%BF%87%E6%8B%9F%E5%90%88.ipynb)  
5.[优化器](https://github.com/Sanduoo/LearnPython/blob/master/TensoFlow%E7%AF%87/1.5_%E4%BC%98%E5%8C%96%E5%99%A8.ipynb)  
##### 第二篇 神经网络八股
1.[搭建神经网络八股](https://github.com/Sanduoo/LearnPython/blob/master/TensoFlow%E7%AF%87/2.1_%E6%90%AD%E5%BB%BA%E7%A5%9E%E7%BB%8F%E7%BD%91%E7%BB%9C%E5%85%AB%E8%82%A1.ipynb)  
2.[MNIST数据集](https://github.com/Sanduoo/LearnPython/blob/master/TensoFlow%E7%AF%87/2.2_MNIST%E6%95%B0%E6%8D%AE%E9%9B%86.ipynb)  
3.[FASHION数据集](https://github.com/Sanduoo/LearnPython/blob/master/TensoFlow%E7%AF%87/2.3_FASHION%E6%95%B0%E6%8D%AE%E9%9B%86.ipynb)  
##### 第三篇 神经网络拓展
1.[自制数据集](https://github.com/Sanduoo/LearnPython/blob/master/TensoFlow%E7%AF%87/3.1_%E8%87%AA%E5%88%B6%E6%95%B0%E6%8D%AE%E9%9B%86.ipynb)  
2.[数据增强](https://github.com/Sanduoo/LearnPython/blob/master/TensoFlow%E7%AF%87/3.2_%E6%95%B0%E6%8D%AE%E5%A2%9E%E5%BC%BA.ipynb)  
3.[断点续训](https://github.com/Sanduoo/LearnPython/blob/master/TensoFlow%E7%AF%87/3.3_%E6%96%AD%E7%82%B9%E7%BB%AD%E8%AE%AD.ipynb)  
4.[参数提取](https://github.com/Sanduoo/LearnPython/blob/master/TensoFlow%E7%AF%87/3.4%E5%8F%82%E6%95%B0%E6%8F%90%E5%8F%96.ipynb)  
5.[acc&loss可视化](https://github.com/Sanduoo/LearnPython/blob/master/TensoFlow%E7%AF%87/3.5_acc%26loss%E5%8F%AF%E8%A7%86%E5%8C%96.ipynb)  
6.[给图识物](https://github.com/Sanduoo/LearnPython/blob/master/TensoFlow%E7%AF%87/3.6_%E7%BB%99%E5%9B%BE%E8%AF%86%E7%89%A9.ipynb)  
##### 第四篇 卷积神经网络