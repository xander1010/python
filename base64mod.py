import base64
base64.b64encode(b'binary\x00string')
base64.b64decode(b'YmluYXJ5AHN0cmluZw==')

# 标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，
# 所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_：
'''
>>> base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
b'abcd++//'
>>> base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
b'abcd--__'
>>> base64.urlsafe_b64decode('abcd--__')
b'i\xb7\x1d\xfb\xef\xff'
'''

# Base64是一种通过查表的编码方法，不能用于加密，
# 即使使用自定义的编码表也不行。

# Base64适用于小段内容的编码，比如数字证书签名、Cookie的内容等

# 由于=字符也可能出现在Base64编码中，但=用在URL、Cookie里面会造成歧义，
# 所以，很多Base64编码后会把=去掉

# 标准Base64:
'abcd' -> 'YWJjZA=='
# 自动去掉=:
'abcd' -> 'YWJjZA'

# 去掉=后怎么解码呢？因为Base64是把3个字节变为4个字节，所以，
# Base64编码的长度永远是4的倍数，因此，
# 需要加上=把Base64字符串的长度变为4的倍数，就可以正常解码了

'''
小结

Base64是一种任意二进制到文本字符串的编码方法，
常用于在URL、Cookie、网页中传输少量二进制数据
'''


# 练习：请写一个能处理去掉=的base64解码函数

def safe_base64_decode(s):
    while len(s)%4:
        s=s+b'='
    return base64.b64decode(s)

assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')