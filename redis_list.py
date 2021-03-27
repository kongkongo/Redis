import redis
import time

pool=redis.ConnectionPool(host="127.0.0.1",port=6379,decode_responses=True)
r=redis.Redis(connection_pool=pool)


"""
1.增加（类似于list的append，只是这里是从左边新增加）--没有就新建
lpush(name,values)
"""
# r.lpush("list1",11,22,33)
# print(r.lrange("list1",0,-1))


"""
2.增加（从右边增加）--没有就新建
"""
# r.rpush("list2",11,22,33) #表示从右向左操作
# print(r.llen("list2"))
# print(r.lrange("list2",0,3))

"""
3.往已经有的name的列表的左边添加元素，没有的话无法创建
"""
# r.lpushx("list10",10)       # 这里list10不存在
# print(r.llen("list10"))     # 0
# print(r.lrange("list10",0,-1))  # []

# r.lpushx("list2",77)
# print(r.llen("list2"))
# print(r.lrange("list2",0,-1))


"""
4.往已经有的name的列表的右边添加元素，没有的话无法创建
"""
# r.rpushx("list2",99)
# print(r.llen("list2"))
# print(r.lrange("list2",0,-1))

"""
5.新增（固定索引号位置插入元素）
linsert(name, where, refvalue, value))
参数：
name - redis的name
where - BEFORE或AFTER
refvalue - 标杆值，即：在它前后插入数据
value - 要插入的数据
"""
# r.linsert("list2","before","11","00")
# print(r.lrange("list2",0,-1))



"""
6.修改（指定索引号进行修改）
r.lset(name, index, value)
对name对应的list中的某一个索引位置重新赋值
参数：
name - redis的name
index - list的索引位置
value - 要设置的值
"""
# r.lset("list2",0,-11)
# print(r.lrange("list2",0,-1))



"""
7.删除（指定值进行删除）
r.lrem(name, value, num)
在name对应的list中删除指定的值,参数：
name - redis的name
value - 要删除的值
num - num=0，删除列表中所有的指定值；
num=2 - 从前到后，删除2个, num=1,从前到后，删除左边第1个
num=-2 - 从后向前，删除2个
"""
# r.lrem("list2","-11",1)
# print(r.lrange("list2",0,-1))
# r.lrem("list2","99",-1)
# print(r.lrange("list2",0,-1))
# r.lrem("list2", "22", 0)    # 将列表中所有的"22"删除
# print(r.lrange("list2", 0, -1)) 


"""
8.删除并返回
lpop(name)
在name对应的列表的左侧获取第一个元素并在列表中移除，返回值则是第一个元素
更多：
rpop(name) 表示从右向左操作
"""
# r.lpop("list2")    # 删除列表最左边的元素，并且返回删除的元素
# print(r.lrange("list2", 0, -1))
# r.rpop("list2")    # 删除列表最右边的元素，并且返回删除的元素
# print(r.lrange("list2", 0, -1))


"""
9.删除索引之外的值
ltrim(name, start, end)
在name对应的列表中移除没有在start-end索引之间的值
参数：
name - redis的name
start - 索引的起始位置
end - 索引结束位置
"""

# r.ltrim("list2",0,2)    # 删除索引号是0-2之外的元素，值保留索引号是0-2的元素
# print(r.lrange("list2",0,-1))



"""
10.取值（根据索引号取值）
lindex(name, index)
"""
# print(r.lindex("list2",0))


"""
11.移动 元素从一个列表移动到另外一个列表
rpoplpush(src, dst)
从一个列表取出最右边的元素，同时将其添加至另一个列表的最左边,参数：
src - 要取数据的列表的 name
dst - 要添加数据的列表的 name
"""
# print(r.lrange("list2",0,-1))
# print(r.lrange("list1",0,-1))
# r.rpoplpush("list1","list2")
# print(r.lrange("list2",0,-1))



"""
12.移动 元素从一个列表移动到另外一个列表 可以设置超时
brpoplpush(src, dst, timeout=0)
从一个列表的右侧移除一个元素并将其添加到另一个列表的左侧,参数：
src - 取出并要移除元素的列表对应的name
dst - 要插入元素的列表对应的name
timeout - 当src对应的列表中没有数据时，阻塞等待其有数据的超时时间（秒），0 表示永远阻塞
"""
# print(r.lrange("list2",0,-1))
# print(r.lrange("list1",0,-1))
# r.brpoplpush("list1","list2",timeout=2)
# print(r.lrange("list2",0,-1))

"""
13.一次移除多个列表
blpop(keys, timeout)
将多个列表排列，按照从左到右去pop对应列表的元素
参数：
keys - redis的name的集合
timeout - 超时时间，当元素所有列表的元素获取完之后，阻塞等待列表内有数据的时间（秒）, 0 表示永远阻塞
更多：
r.brpop(keys, timeout) 同 blpop，将多个列表排列,按照从右像左去移除各个列表内的元素
"""
# r.lpush("list10",3,4,5)
# r.lpush("list11",3,4,5)
# while  True:
#     r.blpop(['list10','list11'],timeout=2)
#     print(r.lrange('list10',0,-1),r.lrange('list11',0,-1))


"""
14.自定义增量迭代
由于redis类库中没有提供对列表元素的增量迭代，如果想要循环name对应的列表的所有元素，那么就需要获取name对应的所有列表。
循环列表,但是，如果列表非常大，那么就有可能在第一步时就将程序的内容撑爆，所有有必要自定义一个增量迭代的功能：
"""

def list_iter(name):
    """
    自定义redis列表增量迭代
    :param name: redis中的name，即：迭代name对应的列表
    :return: yield 返回 列表元素
    """
    list_count=r.llen(name)
    for index in range(list_count):
        yield r.lindex(name,index)

#使用
for item in list_iter('list2'):
    print(item)