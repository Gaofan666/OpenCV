import time

# 1.获取当前时间戳（1970.1.1到现在经过的秒数）
print(time.time())

# 2.时间元组(年，月，日，时，分，秒，一周的第几天，一年的第几天，夏令时)
print(time.localtime())
# 通过元组操作获取时间 时间戳-->时间元组
tuple_time = time.localtime()
for i in tuple_time:
    print(i)
print(tuple_time[1])

# 通过类操作获取时间
print(type(tuple_time))
print(tuple_time.tm_year)
print(time.struct_time)

# 时间元组-->时间戳
print(time.mktime(tuple_time))

# 时间元组 --> str
str_time01 = time.strftime("%y-%m-%d %H-%M-%S", tuple_time)
print(str_time01)
str_time02 = time.strftime("%Y-%m-%d %H-%M-%S", tuple_time)
print(str_time02)

# str-->时间元组
tuple_time2 = time.strptime(str_time02,"%Y-%m-%d %H-%M-%S")
print(tuple_time2)
