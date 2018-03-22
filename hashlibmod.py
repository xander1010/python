import hashlib


# 如果数据量很大，可以分块多次调用update()，最后计算的结果是一样的：
md5 = hashlib.md5()
md5.update('how to use md5 in '.encode('utf-8'))
md5.update('python hashlib?'.encode('utf-8'))
print(md5.hexdigest())


# 另一种常见的摘要算法是SHA1，调用SHA1和调用MD5完全类似：
sha1 = hashlib.sha1()
sha1.update('how to use md5 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())

# SHA1的结果是160 bit字节，通常用一个40位的16进制字符串表示。

# 比SHA1更安全的算法是SHA256和SHA512，不过越安全的算法不仅越慢，
# 而且摘要长度更长

# 小结

# 摘要算法在很多地方都有广泛的应用。要注意摘要算法不是加密算法，
# 不能用于加密（因为无法通过摘要反推明文），只能用于防篡改，
# 但是它的单向计算特性决定了可以在不存储明文口令的情况下验证用户口令



#练习 ：
'''
# 根据用户输入的口令，计算出存储在数据库中的MD5口令：

# def calc_md5(password):
    # pass
# 存储MD5的好处是即使运维人员能访问数据库，也无法获知用户的明文口令。

# 设计一个验证用户登录的函数，根据用户输入的口令是否正确，返回True或False
'''
import hashlib

db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}

def login(user, password):
    password = calc_md5(password)
    if user in db:
        if db[user] == password:
            print('True')
        else:
            print('False')
    else:
        print('user False')
    return None

def calc_md5(password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    return md5.hexdigest()


# 练习2：
'''
# 根据用户输入的登录名和口令模拟用户注册，计算更安全的MD5：

db = {}

def register(username, password):
    db[username] = get_md5(password + username + 'the-Salt')
# 然后，根据修改后的MD5算法实现用户登录的验证：	
'''

import hashlib
import random

def get_md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()

class User(object):
    def init(self, username, password):
        self.username = username
        self.salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = get_md5(password + self.salt)

db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}

def login(username, password):
    user = db[username]
    return user.password == get_md5(password + user.salt)

def register(username, password):
    db[username] = User(username, password)