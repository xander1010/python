from datetime import datetime

#当前时间
now = datetime.now()

print(now)
print(type(now))

#打印指定时间
dt = datetime(2015,4,19,12,30)
print(dt)

#把datetime转换为timestamp，对应epochtime的秒数
print(dt.timestamp()) #小数点后面为毫秒数

# epoch time 新纪元时间
# 1970年1月1日 00:00:00 UTC+00:00时区的时刻称为epoch time
# 相对于epoch time的秒数，称为timestamp（时间戳）。
# timestamp = 0 = 1970-1-1 00:00:00 UTC+0:00
# 对应的北京时间是：
# timestamp = 0 = 1970-1-1 08:00:00 UTC+8:00


t = 1429417800.0
# 使用datetime提供的fromtimestamp()方法将timestamp转换为datetime
print(datetime.fromtimestamp(t)) #本地时间

# 转换成utc时间
print(datetime.utcfromtimestamp(t))

print('################str转换为datetime#############')

# 字符串'%Y-%m-%d %H:%M:%S'规定了日期和时间部分的格式
cday = datetime.strptime('2015-6-1 18:19:59','%Y-%m-%d %H:%M:%S')
print(cday)


print('################datetime转换为str#############')
N = datetime.now()
print(now.strftime('%a,%b %d %H:%M'))

print('################datetime加减#############')
# 可以直接加减，但要导入timedelta类
from datetime import timedelta

now = datetime.now()
# 当前时间加10个小时
print(now + timedelta(hours=10))
# 当前时间减一天
print(now - timedelta(days=1))
# 当前时间+2天12小时
print(now + timedelta(days=2,hours=12))

print('################本地时间转换为UTC时间#############')

from datetime import timezone
tz_utc_8 = timezone(timedelta(hours=8))#创建时区utc+8:00
now = datetime.now()
print(now)
dt = now.replace(tzinfo=tz_utc_8)#强制设置为utc+8:00
print(dt)

print('################时区转换#############')
# 通过utcnow()拿到当前的UTC时间，再转换为任意时区的时间
#拿到UTC时间再强制转换成UTC+0:00
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)

#astimezone()将转换为北京时间
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)

# astimezone()将转换时区为东京时间:
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)

# astimezone()将bj_dt转换时区为东京时间:
tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt2)

# 时区转换的关键在于，拿到一个datetime时，要获知其正确的时区，
# 然后强制设置时区，作为基准时间

# 小结
# datetime表示的时间需要时区信息才能确定一个特定的时间，否则只能视为本地时间。
# 如果要存储datetime，最佳方法是将其转换为timestamp再存储，因为timestamp的值与时区完全无关


#练习：
# 假设你获取了用户输入的日期和时间如2015-1-21 9:01:30，
# 以及一个时区信息如UTC+5:00，均是str，请编写一个函数将其转换为timestamp：
print('*************练习**********************')

from datetime import datetime
import re
	
def to_timestamp(dt_str, tz_str):
	#正则表达式匹配tz_str中的小时
	x = re.match(r'UTC([\+|\-\d]+?):00',tz_str)
	#将获取的时区数转换为整数
	tz =int(x.group(1))
	# 创建时区utc+tz_str
	tz_utc = timezone(timedelta(hours=tz))
	# 将输入的时间转换为输入时区的datetime
	cday = datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S').replace(tzinfo=tz_utc)
	#返回时间戳
	return cday.timestamp()

#直接输入数值型的时候
def zhuan(dtt,utt):
	# 将输入的小时数转换为整数
	a = int(utt)
	# 创建输入小时数的时区
	ttutc = timezone(timedelta(hours=a))
	# 将输入的字符串时间转换为时间
	zhuanhuan = datetime.strptime(dtt,'%Y-%m-%d %H:%M:%S')
	#为输入的时间加上时区
	dttim = zhuanhuan.replace(tzinfo=ttutc)
	#返回时间戳
	return dttim.timestamp()

print(zhuan('2015-1-21 9:01:30','5'))
	

print(to_timestamp('2015-1-21 9:01:30','UTC+5:00'))










