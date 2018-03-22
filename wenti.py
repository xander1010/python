# import urllib.request

# url = 'http://www.douban.com'
# data = urllib.request.urlopen(url).read()
# data = data.decode('UTF-8')
# print(data)
# print(type(data))
# print(data.geturl())
# print(data.info())
# print(data.getcode())

a='ch'
b='in'
c='a'
q='m'
w='a'
e='n'
print(a+b+c,q+w+e)

def solution1(digits='129823249898923432432'):
	value = []
	for i in range(len(digits)):
		if digits[i] == '9':
		    value.append(''.join(digits[i:i+5]))
		else:   
		    pass
	print(value)
	return max(value)


solution1()	