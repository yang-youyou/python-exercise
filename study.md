
# Python 学习
## 1. numpy
*  导入numpy包以及重命名，将numpy命名为np，即import numpy as np。
*  np.arange 函数：生成数组,1是起始数字，10 是末尾数字，2是步长，默认是 1。调用此函数：`arr = np.arrange(1,10,2)`，类型：class 'numpy.ndarray'。返回一个左闭右开的1-10范围内的等差数列，差为2，类型为数组。数据类型，int、float。 一维。
* 内置：type 函数，判断类型，输出arr 类型。调用此函数：`print(type(arr))`。
* 内置：help 函数， 输出 np.arange 函数的具体用法。调用此函数：`help(np.arange)`。
* 内置：print 函数，输出值。调用此函数：
    ```
    arr9 = np.random.randn(2,4)
    print(arr9, type(arr9), arr9.shape, arr9.dtype)
   #下面是返回的结果
    [[ 1.1809036   0.1501467  -1.16126497  1.02549244]
    [-0.50767198  0.47586712  1.13661941  1.6897925 ]] <class 'numpy.ndarray'> (2, 4) float64
    ```
  代表一个2*4的正态分布随机数矩阵，类型为numpy.ndarray，shape为（2,4）矩阵，数据类型为浮点型。
* np.array 函数：连接内置list与numpy包的函数。例子:
  ```
    arr1 = [1,2,3,4,5,6,7,8,9,10]
    print(arr1)
    print(type(arr1))
    #arr2 = np.array([1, 2, 345, 2, 6, 2, 7, 8])
    arr2 = np.array(arr1)
    print(arr2)
    print(type(arr2))
  ```
* np.random.random 函数，生成矩阵随机数。入参shape，返回一个多维矩阵。调用函数：
  ```
  arr3 = np.random.random((3, 4, 5))
  print(arr3)
  ```
  返回3个4*5的数值在0-1之间的浮点型矩阵随机数。
* **生成a-b范围内浮点型矩阵随机数**。调用函数：
  ```
  a = 400
  b = 1000
  arr3 = np.random.random(10)*(b-a)+a
  print(arr3)
  ```
即可得到10个a-b范围内的浮点型矩阵随机数。
* np.random.randint 函数，调用函数：
  ```
  arr4 = np.random.randint(0, 9, 10))
  print(arr4)
  ```
  返回10个0-9之间的随机数，10可以换成shape（2，2），即返回一个2*2的0-9之间的矩阵随机数。最后加上`*1000`即可得到原浮点型矩阵随机数放大1000倍的浮点型矩阵随机数。
* **np.random.randint(low, high=None, size=None, dtype=’l’)**
返回随机整数，范围区间为[low,high），包含low，不包含high参数：low为最小值，high为最大值，size为数组维度大小，dtype为数据类型，默认的数据类型是np.int。high没有填写时，默认生成随机数的范围是[0，low)。
* np.zeros 函数，生成全零矩阵。调用函数：
  ```
  arr5 = np.zeros((2, 3))
  print(arr5)
  ```
  返回一个2*3的全零矩阵。
* np.ones 函数，生成全1矩阵。
* np.full 函数，调用函数：
  ```
  arr7 = np.full((2, 4), 2)
  print(arr7)
  ```
  返回一个2*4的全2矩阵。
* np.eye 函数，生成对角线都是1的对角矩阵。调用函数：
  ```
  arr8 = np.eye(4)
  print(arr8)
  ```
  返回一个4*4的对角线都是1 的对角矩阵。
* np.random.randn，生成正态分布的浮点型矩阵随机数。调用函数：
   ```
  arr9 = np.random.randn(2,4)
  print(arr9)
  ```
  返回一个2*4的浮点型矩阵随机数。


## 2. base
* 标准数据类型
```
Number
String
List
Tuple(元祖)
Sets(集合)
Dictionary(字典)
1）Number
在python中Number一共有四种类型分别为：
int
float(浮点数)
complex(复数)
bool
2) Set
无序、不可重复元素
3）dict
key value 对，key不可重复
```
* 内置：len函数，计算string的长度和list的元素个数。
  ```
  namelist = ['马云','马化腾','王健林','李彦宏']
  namelen = len(namelist)
  print('列表长度:',namelen)
  ```
  返回：列表长度: 4。
### list 数组 list = [1,2,3]/list = ['abc','155','55']/['abc',155,55]
* .append('想增加的元素') 增加list元素函数。
  ```
  namelist.append('刘强东')
  print = namelist
  ```
  返回：['马云','马化腾','王健林','李彦宏','刘强东']。
* del list[想删除的元素下标] 删除list元素函数。
  ```
  del namelist[1]
  print = ('删除第二个元素:',namelist)
  ```
  返回：删除第二个元素：['马云','王健林','李彦宏','刘强东']。
* .pop(想删除的元素下标) 删除list元素函数。
  ```
  namelist.pop(1)
  print namelist
  ```
  返回：['马云','王健林','李彦宏','刘强东']。
* #修改
  ```
  nameList=['a','b','c','d']
  print('the first element now：',nameList)
  nameList[0]='e'
  print('the first element after modifed：',nameList)
  ```
  返回：the first element now： ['a', 'b', 'c', 'd']
      the first element after modifed： ['e', 'b', 'c', 'd']
### string 字符串 string = 'apple'/"apple"
* 删除字符串的某个元素可以将string转化为list，再用del/pop删除，后再将list转化为string。
  ```str = 'apple'
  s_list = list(str)
  del s_list[3]
  str = ''.join(s_list)
  print(str)
  ```
  返回：appe。
* string/list下标既可以0 1 2 ···，也可以···-2 -1 0
  ```
  str = 'apple'
  print(str[0],str[-5])
  print(str[1],str[-4])
  print(str[2],str[-3])
  print(str[3],str[-2])
  print(str[4],str[-1])
  ```
  str[i]=str[i-len(str)]
* string切片： 切片时设置的参数分别 start index， end index， step
[start,end)  是一个左开右闭区间，当只有此范围内有元素时才能切出来。举例：
  ```
  str = 'apple'
  ```
  str[-1:-6:-1] 为逆置， -1 是 'e'，-1 + （-1） 为 -2，-2 在[-1,-6) 中间， -2 为 'l'。 所以下标依次为，-1，-2，-3，-4，-5. 正好截取。返回el
  str[4:5:-1] 为空，4是'e', 4 + （-1）为3，3不在 [4,5), 所以为空
 str[4:2:-1] el, 4是'e', 4+ (-1) 为3， 3 在[4,2) 之间，3是'l', 3+(-1) 为2，2不在[4,2）之间，所以取4.3 即el。
### tuple 元组 tuple = ('abc','155','55')/('abc',155,55)
* tuple可以直接赋值给元素，例如：
  ```
  tuple = ('xy','love','xz')
  a,b,c = tuple
  print(a,b,c)
  ```
  返回:xy love xz。
* tuple和list的区别是，tuple不能被修改，即tuple不能被赋值
  ```
  t = (1,2,3)
  t[0]=(7)#报错，tuple不能被赋值
  print(t)
  ```
  返回会出错

*  #需要注意
tuple=() #空元组；
### set 集合 set = {'a','b','c'}
* .update(['something']),增加函数。
```
gafataSets={'t','ali','g','F'}
gafataSets.update(['apple'])
print(gafataSets)
```
返回：{'g', 'F', 'apple', 't', 'ali'}
  * .discard('something'),删除函数。
```
gafataSets={'t','ali','g','F'}
gafataSets.discard('g')
print(gafataSets)
```
返回：{'F', 't', 'ali'}。
* txBool = 'somethinng'in gafataSets，查找函数。
  ```
  gafataSets={'t','ali','g','F'}
  txBool = 't'in gafataSets
  print(txBool)
  ```
  返回：True。
* 需要注意
  s = {}代表空dict
  s = set()代表空set，此处set是一个生成set的函数，（）只能传入“一个”任意基础类型参数，比如list string tuple dictionary(dict只能把key取出去)
  ```
  s = set({'a':2,'b':3})
  print(s,type(s)) 
  ```
  返回：{'b', 'a'} <class 'set'>
* 因为set特点是无序和不能有重复元素，所以可以用set()函数来去重。
* ```
  l = [1,1,1,2,3,4]
  l = set(l)
  print(l)
  ```
  返回：{1, 2, 3, 4}。
### Dictionary 字典 Dict{'a':1,'b':2,'c':3}，由key:value对组成，key不可重复
* 
```
dict = {} #建一个空字典
dict['one'] = 'This is one'
dict[2] = 'This is two'
print(1, dict['one'])  # 输出键为'one'的值
print(2, dict[2])  # 输出键为2的值
```
返回：1 This is one   
    2 This is two
```
tinydict = {'name': 'john', 'code': 5762, 'dept': 'sales'}
print(3, tinydict)  # 输出完整的字典
print(4, tinydict.keys())  # 输出所有键，注意是keys
print(5, tinydict.values())  # 输出所有值，注意是values
```
返回：3 {'name': 'john', 'code': 5762, 'dept': 'sales'}  
4 dict_keys(['name', 'code', 'dept'])  
5 dict_values(['john', 5762, 'sales'])
## python学习网址
* [Python 5种基础数据类型](https://www.cnblogs.com/snaildev/p/7544558.html)
* [Python 7种基础运算符](https://www.cnblogs.com/snaildev/p/7553087.html)
* [Python 条件及循环](https://www.cnblogs.com/snaildev/p/7560707.html)
* [Python 关键字以及含义，用法](https://www.cnblogs.com/cheng10/p/9634437.html)
* [Python简介](https://zhuanlan.zhihu.com/p/24162430)
* [Consul](https://www.tizi365.com/archives/507.html)