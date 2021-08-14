dict = {}
dict['one'] = 'This is one'
dict[2] = 'This is two'
tinydict = {'name': 'john', 'code': 5762, 'dept': 'sales'}

print(1, dict['one'])  # 输出键为'one'的值
print(2, dict[2])  # 输出键为2的值
print(3, tinydict)  # 输出完整的字典
print(4, tinydict.keys())  # 输出所有键
print(5, tinydict.values())  # 输出所有值
l = [1,2,3,45,5]
print(l)
l[0] = [234,5,63,4567,"ew"]
print(l)

t = (23454,65,324,3)
print(t)
t = (213454,53,245365,46,356)
print(t)
s = {1,"apple",2,'love'}
s.add(500)
print(s,type(s))
s = set({'a':2,'b':3})
print(s,type(s))
s.add(800)
print('test',s,type(s))
t = tuple({'a':2,'b':3})
print(t,type(t))
l = list({'a':2,'b':3})
print('test1',l,type(l))
l = [1,1,1,2,3,4]
l = set(l)
print(l)
l = list(s)
print(l,type(l))