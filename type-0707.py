str = 'apple'
str1 = ['a','p','p','l','e']
print(1, str,type(str),len(str),str1, type(str1),len(str1))
print(2, str[0],str[4])
print(2.1,str1[0],str1[4])
print(3, str[-1],str[-2])
print(4, str[1:],str[1:4],str[3:5],4.1,str[-3:-1],4.2,str[-2:-1],4.3,str[-1:],4.4,str[0:-1],4.5,str[-1:-6:-1],4.6, str[4:5:-1],str[4:2:-1])
print(5, str * 2)
print(6, str + "google")
str1 = 'my name is %s,my wife is %s' % ('xz', 'xy')
print(7, str1)
# 切片时设置的参数分别 start index， end index， step
# [start,end)  是一个左开右闭区间，当只有
# str[-1:-6:-1] 为逆置， -1 是 'e'，-1 + （-1） 为 -2，-2 在[-1,-6) 中间， -2 为 'l'。 所以下标依次为，-1，-2，-3，-4，-5. 正好截取。
# str[4:5:-1] 为空，4是'e', 4 + （-1）为3，3不在 [4,5), 所以为空
# str[4:2:-1] el, 4是'e', 4+ (-1) 为3， 3 在[4,2) 之间，3是'l', 3+(-1) 为2，2不在[4,2）之间，所以取4.3 即el
#长度
nameList=['猴子','马云','王健林','二爷']
namelen=len(nameList)
print(8,'列表长度：', namelen)
#增加元素
nameList.append('刘强东')
print(9,nameList)
#删除元素
del nameList[1]
print(10,'删除第二个元素：',nameList)
#del str[1]
#print(11,str)
s_list = list(str)
del s_list[1]
str = ''.join(s_list)
print(11,s_list,str)
str = 'apple'
s_list = list(str)
s_list.pop(3)
str = ''.join(s_list)
print(12,str)
#查询元素
name1=nameList[0]
print(name1)



