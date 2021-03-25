import redis
import time
"""
set(name, value, ex=None, px=None, nx=False, xx=False)
在 Redis 中设置值，默认，不存在则创建，存在则修改。
ex - 过期时间（秒）
px - 过期时间（毫秒）
nx - 如果设置为True，则只有name不存在时，当前set操作才执行
xx - 如果设置为True，则只有name存在时，当前set操作才执行
"""

pool = redis.ConnectionPool(host='127.0.0.1', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)
# r.set('food', 'mutton', ex=3)    # key是"food" value是"mutton" 将键值对存入redis缓存
r.set('food', 'beef', px=3)
# print(r.set('fruit', 'watermelon', nx=True))    # True--不存在

# print((r.set('fruit', 'watermelon', xx=True)))   # True--已经存在
# print(r.get('food'))  # mutton 取出键food对应的值



# 5.setnx(name, value)
# 设置值，只有name不存在时，执行设置操作（添加）

# print(r.setnx('fruit1','banana')) #fruit1不存在，输出为True



"""6.setex(name, time, value)
设置值参数：
time - 过期时间（数字秒 或 timedelta对象）
"""
# r.setex("fruit2", 5, "orange")
# time.sleep(5)
# print(r.get('fruit2'))  # 5秒后，取值就从orange变成None


"""
7.psetex(name, time_ms, value)
设置值参数：
time_ms - 过期时间（数字毫秒 或 timedelta对象）
"""
# r.psetex('fruit3',5000,'apple')
# time.sleep(5)
# print(r.get('fruit3'))


# 8.mset(*args, **kwargs)
# 批量设置值
# r.mget({'k1': 'v1', 'k2': 'v2'})
# r.mset(key1="hello",key2="world") # 这里k1 和k2 不能带引号 一次设置对个键值对
# print(r.mget("key1", "key2"))   # 一次取出多个键对应的值
# print(r.mget("k1"))
# print(r.mget("fruit", "fruit1", "fruit2", "k1", "k2"))  # 将目前redis缓存中的键对应的值批量取出来


# 10.getset(name, value)
# 设置新值并获取原来的值
# print(r.getset("food","barbecue"))# 设置的新值是barbecue 设置前的值是beef
# print(r.get('food'))    

"""
11.getrange(key, start, end)
获取子序列（根据字节获取，非字符）
参数:
name - Redis 的 name
start - 起始位置（字节）
end - 结束位置（字节）
"""
# r.set('cn_name','君惜大大')
# print(r.getrange('cn_name',0,2))    # 取索引号是0-2 前3位的字节 君 切片操作 （一个汉字3个字节 1个字母一个字节 每个字节8bit）

# print(r.getrange('cn_name',0,-1))   # 取所有的字节 君惜大大 切片操作

# r.set('en_name','junxi')    #字母
# print(r.getrange('en_name',0,2))
# print(r.getrange('en_name',0,-1))

"""
12.setrange(name, offset, value)
修改字符串内容，从指定字符串索引开始向后替换（新值太长时，则向后添加）
参数：
offset - 字符串的索引，字节（一个汉字三个字节）
value - 要设置的值
"""
# r.setrange('en_name',1,'ccc')
# print(r.get('en_name'))     # jccci 原始值是junxi 从索引号是1开始替换成ccc 变成 jccci


"""
13.setbit(name, offset, value)
对 name 对应值的二进制表示的位进行操作
参数：
name - redis的name
offset - 位的索引（将值变换成二进制后再进行索引）
value - 值只能是 1 或 0
注：如果在Redis中有一个对应： n1 = "foo"，
那么字符串foo的二进制表示为：01100110 01101111 01101111
所以，如果执行 setbit('n1', 7, 1)，则就会将第7位设置为1，
那么最终二进制则变成 01100111 01101111 01101111，即："goo"
"""
# source="陈思维"
# source='foo'
# for i in source:
#     num=ord(i)
#     print (bin(num).replace('b',''))

"""
14.getbit(name, offset)
获取name对应的值的二进制表示中的某位的值 （0或1）
"""
# print(r.getbit("foo1", 0)) # 0 foo1 对应的二进制 4个字节 32位 第0位是0还是1

"""
bitcount(key, start=None, end=None)
获取name对应的值的二进制表示中 1 的个数
参数：
key - Redis的name
start - 字节起始位置
end - 字节结束位置
"""
# print(r.get('foo'))
# print(r.bitcount('foo',0,1))



"""
16.bitop(operation, dest, *keys)
获取多个值，并将值做位运算，将最后的结果保存至新的name对应的值
参数：
operation - AND（并） 、 OR（或） 、 NOT（非） 、 XOR（异或）
dest - 新的Redis的name
*keys - 要查找的Redis的name
"""
# r.set("foo","1")  # 0110001
# r.set("foo1","2")  # 0110010
# print(r.mget("foo","foo1"))  # ['goo1', 'baaanew']
# print(r.bitop("AND","new","foo","foo1"))  # "new" 0 0110000
# print(r.mget("foo","foo1","new"))

# source='12'
# for i in source:
#     num=ord(i)
#     print(num)   # 打印每个字母字符或者汉字字符对应的ascii码值 f-102-0b100111-01100111
#     print(bin(num)) # 打印每个10进制ascii码值转换成二进制的值 0b1100110（0b表示二进制）
#     print (bin(num).replace('b',''))    # 将二进制0b1100110替换成01100110


"""
17.strlen(name)
返回name对应值的字节长度（一个汉字3个字节）
"""
# print(r.set('foo','goo1'))
# print(r.strlen('foo'))

"""
18.incr(self, name, amount=1)
自增 name 对应的值，当 name 不存在时，则创建 name＝amount，否则，则自增。
参数：
name - Redis的name
amount - 自增数（必须是整数）
"""
# r.set('foo',123)
# print(r.mget('foo','foo1','foo2','k1','k2'))
# r.incr('foo',amount=1)
# print(r.mget('foo','foo1','foo2','k1','k2'))

# r.set("visit:12306:totals", 34634)
# print(r.get("visit:12306:totals"))
# r.incr("visit:12306:totals")
# r.incr("visit:12306:totals")
# print(r.get("visit:12306:totals"))


"""
19.incrbyfloat(self, name, amount=1.0)
自增 n
参数：
name - Redis的name
amount - 自增数（浮点型）
"""
# r.set('foo1','123.0')
# r.set('foo2','221.0')
# print(r.mget('foo1','foo2'))
# r.incrbyfloat('foo1',amount=2.0)
# r.incrbyfloat('foo2',amount=3.0)
# print(r.mget('foo1','foo2'))


"""
20.decr(self, name, amount=1)
自减 name 对应的值，当 name 不存在时，则创建 name＝amount，否则，则自减。
参数：
name - Redis的name
amount - 自减数（整数)
"""
# r.decr('foo4',amount=3)
# r.decr('foo1',amount=1)
# print(r.mget('foo1','foo4'))


"""
21.append(key, value)
在redis name对应的值后面追加内容
参数：
key - redis的name
value - 要追加的字符串
"""
r.append('name','haha')
print(r.mget('name'))
