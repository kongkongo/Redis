import  redis
import time

pool=redis.ConnectionPool(host="127.0.0.1",port=6379,decode_responses=True)
r=redis.Redis(connection_pool=pool)


"""
Set操作，Set集合就是不允许重复的列表，本身是无序的。

有序集合，在集合的基础上，为每元素排序；元素的排序需要根据另外一个值来进行比较，所以，对于有序集合，每一个元素有两个值，即：值和分数，分数专门用来做排序。
"""

"""
1.新增
zadd(name, *args, **kwargs)  已取消这种写法
redis.zadd(zkey, {'smeagol': now})
"""

# r.zadd("zset1",n1=11,n2=22)
# r.zadd("zset1",{"n1":11,"n2":22})
# r.zadd("zset2",{'m1':22,'m2':44})
# print(r.zcard("zset1")) #集合的长度
# print(r.zcard("zset2")) #集合的长度
# print(r.zrange("zset1",0,-1))
# print(r.zrange("zset2",0,-1,withscores=True))    # 获取有序集合中所有元素和分数


"""
2.获取有序集合元素个数 类似于len
zcard(name)
获取name对应的有序集合元素的数量
"""
# print(r.zcard("zset1"))     #集合的长度



"""3.获取有序集合的所有元素
r.zrange( name, start, end, desc=False, withscores=False, score_cast_func=float)
按照索引范围获取name对应的有序集合的元素
参数：
name - redis的name
start - 有序集合索引起始位置（非分数）
end - 有序集合索引结束位置（非分数）
desc - 排序规则，默认按照分数从小到大排序
withscores - 是否获取元素的分数，默认只获取元素的值
score_cast_func - 对分数进行数据转换的函数
"""
# print(r.zrange("zset1",0,-1,withscores=True))

#从大到小排序(同zrange，集合是从大到小排序的)
#zrevrange(name, start, end, withscores=False, score_cast_func=float)
# print(r.zrevrange("zset1",0,-1))
# print(r.zrevrange("zset1",0,-1,withscores=True))    # 获取有序集合中所有元素和分数,分数倒序


"""
3-2 按照分数范围获取name对应的有序集合的元素
zrangebyscore(name, min, max, start=None, num=None, withscores=False, score_cast_func=float)
"""
# for i in range(1,30):
#     element='n'+str(i)
#     r.zadd("zset3",{element:i})
# print(r.zrangebyscore("zset3",1))
# for i in range(1, 30):
#    element = 'n' + str(i)
#    r.zadd("zset3", {'element':i})
# print(r.zrangebyscore("zset3", 15, 25)) # # 在分数是15-25之间，取出符合条件的元素
# print(r.zrangebyscore("zset3",12,22,withscores=True))    # 在分数是12-22之间，取出符合条件的元素（带分数）
# print(r.zrevrangebyscore("zset3", 22, 11, withscores=True)) # 在分数是22-11之间，取出符合条件的元素 按照



"""
分数倒序
3-4 获取所有元素--默认按照分数顺序排序
zscan(name, cursor=0, match=None, count=None, score_cast_func=float)
"""
# print(r.zscan("zset3"))


"""
3-5 获取所有元素--迭代器
zscan_iter(name, match=None, count=None,score_cast_func=float)
"""
# for i in r.zscan_iter("zset3"):
#    print(i)


"""
4.zcount(name, min, max)
获取name对应的有序集合中分数 在 [min,max] 之间的个数
"""
# print(r.zrange("zset3",0,-1,withscores=True))
# print(r.zcount("zset3",11,22))


"""
5.自增
zincrby(name, value, amount)
自增name对应的有序集合的 name 对应的分数
"""
# r.zincrby("zset3",'n2',amount=2)
# print(r.zrange('zset3',0,-1,withscores=True))



"""
6.获取值的索引号
zrank(name, value)
zrevrank(name, value)，从大到小排序。
"""
# print(r.zrank("zset3","n1"))
# print(r.zrank("zset3","n6"))

# print(r.zrevrank("zset3","n1"))



"""
7.删除--指定值删除
zrem(name, values)
删除name对应的有序集合中值是values的成员
"""
# r.zrem("zset3","n3")
# print(r.zrange("zset3",0,-1))

"""
8.删除--根据排行范围删除，按照索引号来删除
zremrangebyrank(name, min, max)
"""
# r.zremrangebyrank("zset3",11,22)
# print(r.zrange("zset3",0,-1,withscores=True))



"""
9.删除--根据分数范围删除
zremrangebyscore(name, min, max)
"""
# r.zremrangebyscore("zset3",11,22)
# print(r.zrange("zset3",0,-1,withscores=True))


"""
10.获取值对应的分数
zscore(name, value)
"""
print(r.zscore("zset3","n10"))

