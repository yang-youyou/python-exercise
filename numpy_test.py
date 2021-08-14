import numpy
import numpy as np

# arange 生成数组,1是起始数字，11 是末尾数字，2是步长，默认是 1
# arr = np.arange(1, 11, 2.1)
arr = np.arange(1, 10, 1.1) #(2,2) error
# 输出函数print， 输出arr
print(arr)
# type 函数，判断类型，输出arr 类型
print(type(arr))
# help 函数， 输出 np.arange 函数的具体用法
#help(np.arange)


arr1 = [1,2,3,4,5,6,7,8,9,10]
print(arr1)
print(type(arr1))

#arr2 = np.array([1, 2, 345, 2, 6, 2, 7, 8])
arr2 = np.array(arr1)
print(arr2)
print(type(arr2))

arr3 = np.random.random((3,4,5))
print(arr3)

a = 400
b = 1000
arr3 = np.random.random(10)*(b-a)+a
print(arr3)

arr4 = np.random.randint(0, 9, 10)
print(arr4)
#arr4 = np.random.rand(1.0, 9.9, 5)
print(arr4)

arr5 = np.zeros((2, 3))
print(arr5)

arr6 = np.ones((2, 2))
print(arr6)

arr7 = np.full((2, 4), 2)
print(arr7)

arr8 = np.eye(4)
print(arr8)

arr9 = np.random.randn(2,4)
print(arr9, type(arr9), arr9.shape, arr9.dtype)