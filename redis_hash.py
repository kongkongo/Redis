import redis
import time

pool = redis.ConnectionPool(host='127.0.0.1', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)

"""
1、单个增加--修改(单个取出)--没有就新增，有的话就修改
hset(name, key, value)
name对应的hash中设置一个键值对（不存在，则创建；否则，修改）
参数：
name - redis的name
key - name对应的hash中的key
value - name对应的hash中的value
注：hsetnx(name, key, value) 当name对应的hash中不存在当前key时则创建（相当于添加）
"""

# r.hset('hash1','k1','v1')
# r.hset('hash1','k2','v2')
# print(r.hkeys('hash1')) #取出hash中所有的key
# print(r.hget('hash1','k1')) # 单个取hash的key对应的值
# print(r.hmget('hash1','k1','k2'))   # 多个取hash的key对应的值
# r.hsetnx("hash1", "k2", "v3") # 只能新建
# print(r.hget("hash1", "k2"))

"""
2、批量增加（取出）
hmset(name, mapping)
在name对应的hash中批量设置键值对
参数：
name - redis的name
mapping - 字典，如：{'k1':'v1', 'k2': 'v2'}
"""
# r.hmset('hash2',{'k2':'v2','k3':'v3'})
# print(r.hget("hash2",'k2'))
# print(r.hmget("hash2", "k2", "k3"))  # 批量取出"hash2"的key-k2 k3对应的value --方式1
# print(r.hmget("hash2", ["k2", "k3"]))  # 批量取出"hash2"的key-k2 k3对应的value --方式2


"""
3、取出所有的键值对
"""
# print(r.hgetall("hash1"))



"""
4、得到所有键值对的格式 hash长度
获取name对应的hash中键值对的个数
"""
# print(r.hlen("hash1"))

"""
5、得到所有的keys（类似字典的取所有keys）
获取name对应的hash中所有的key的值
"""
# print(r.hkeys("hash1"))

"""
6、得到所有的value（类似字典的取所有value）
获取name对应的hash中所有的value的值
"""
# print(r.hvals("hash1"))


"""
7、判断成员是否存在（类似字典的in） 
hexists(name,key)   检查 name 对应的 hash 是否存在当前传入的 key
"""
# print(r.hexists("hash1","k4"))
# print(r.hexists("hash1","k1"))


"""
8.删除键值对
hdel(name,*keys)
"""
# print(r.hgetall('hash1'))
# r.hset("hash1","k2","v222")   # 修改已有的key k2
# r.hset("hash1","k11","v1")      # 新增键值对 k11
# r.hdel("hash1","k1")    # 删除一个键值对
# print(r.hgetall("hash1"))


"""
自增自减整数(将key对应的value--整数 自增1或者2，或者别的整数 负数就是自减)
hincrby(name, key, amount=1)
"""
# r.hset("hash1","k3",123)
# r.hincrby("hash1","k3",amount=-1)
# print(r.hgetall("hash1"))
# r.hincrby("hash1","k4",amount=1)
# print(r.hgetall("hash1"))


"""
10、自增自减浮点数(将key对应的value--浮点数 自增1.0或者2.0，或者别的浮点数 负数就是自减)
hincrbyfloat(name, key, amount=1.0)
"""
# r.hset("hash1","k5","1.0")
# r.hincrbyfloat("hash1","k5",amount=-1.0)
# print(r.hgetall("hash1"))
# r.hincrbyfloat("hash1","k6",amount=-1.0)
# print(r.hgetall("hash1"))


"""
11、取值查看--分片读取
hscan(name, cursor=0, match=None, count=None)
"""
# cursor1, data1 = r.hscan('hash1', cursor=0, match=None, count=None)
# print(r.hscan("hash1"))
# cursor2, data1 = r.hscan("hash1",cursor=cursor1,match=None,count=None)
# print(r.hscan("hash1"))


"""
12、hscan_iter(name, match=None, count=None)
利用yield封装hscan创建生成器，实现分批去redis中获取数据
"""
for item in r.hscan_iter("hash1"):
    print(item)
print(r.hscan_iter("hash1"))     # 生成器内存地址