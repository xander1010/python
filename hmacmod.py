import hmac
message = b'Hello,world!'
key = b'secret'
h = hmac.new(key,message,digestmod = 'MD5')
print(h.hexdigest)



# 练习:
# 将上一节的salt改为标准的hmac算法，验证用户口令：

import hmac, random

class User(object):
    def __init__(self, username, password):
        self.username = username
        self.key = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = hmac_md5(self.key, password)

db = {}

def hmac_md5(key, s):
    return hmac.new(key.encode('utf-8'), s.encode('utf-8'), 'MD5').hexdigest()

def register(username, password):
    db[username] = User(username, password)
    return True

def login(username, password):
    user = db[username]
    return user.password == hmac_md5(user.key, password)

assert register('michael', '123456')
assert register('bob', 'abc999')
assert register('alice', 'alice2008')
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')
print(db)


# 其他写法及测试：
"""
#需求：根据用户输入的登录名和口令模拟用户注册，计算更安全的MD5，实现用户登录的验证
#用到的类和函数：
    类： User(object)：用户注册类
    函数：get_md5(s)：返回md5后的字符串
         login(username, password)：用户登录检测函数

"""
# -*- coding: utf-8 -*-
import hmac, random

def hmac_md5(key, s):
    """
    #hm3.md5加密密码
    :param s:密码
    :param key:需要加在密码中的key
    :return: 返回md5后的字符串
    """
    return hmac.new(key.encode('utf-8'), s.encode('utf-8'), 'MD5').hexdigest()

class UserRegistered(object):
    """
    #用户注册类：获取用户注册信息给密码加上登录名和“盐”
    #随机生成“盐”，并且将其保存在db_salt
    #给用户注册输入的密码加盐,并保存在db中
    #函数：
        __init__(self, username, password):获取注册信息，调用函数：userReg()
        userReg()：检查注册用户名是否以存在，存在返回：'Username has already been registered!'，
                    不存在返回：'Reg ok'，调用userSalt()
        userSalt():随机生成“盐”，并且将用户名和密码加盐保存
    """
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def userReg(self):
        """
        #检查注册用户名是否以存在
        :return: 用户名不存在数据库。输出ok,存在输出:Username has already been registered!
        """
        if self.username not in db:
            self.userSalt()
            return 'Reg ok'

        else:
            return 'Username has already been registered!'

    def userSalt(self):
        """
        #随机生成“盐”，并且将用户名和密码加盐保存
        :return: 无
        """
        salt=''.join(chr(random.randint(48,122)) for i in range(20))
        db_salt[self.username]=salt
        db[self.username]=self.username+self.password


class UserLogin(object):
    """
    #用户登录类，检查用户登录，返回登录成功或失败以及失败的原因
    #函数：__init__(self,username,password):拿取用户登录信息，调用userLogin()
         userLogin()：检查注册用户名是否以存在,若存在则检查输入密码是否和数据库中对应。
                        用户名不存在数据库。输出'Please register first!',存在且匹配输出:'Success!'
    """
    def __init__(self,username,password):
        self.username=username
        self.password=password
        # self.userLogin()

    def userLogin(self):
        """
        #检查注册用户名是否以存在,若存在则检查输入密码是否和数据库中对应。

        :return: 用户名不存在数据库。输出'Please register first!',
                存在且匹配输出:'Success!'
        """
        if self.username not in db:
            return 'Please register first!'
        else:#                db_salt[self.username]=salt
                            # db[self.username]=self.password+salt+self.username
            if hmac_md5(db_salt[self.username],self.username+self.password)==hmac_md5(db_salt[self.username],db[self.username]):
                return 'Success!'
            else:
                return 'Please cheack again!'


#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
#数据库
db = {}   #保存注册信息
db_salt={}#保存用户名对应的随机加密值

# 以上的单元测试：

# -*- coding: utf-8 -*-
"""
测试md5加密的用户注册和登录功能
"""
import unittest
from unittest.test import suite

from md5_code import  UserRegistered,UserLogin
class TestUserRegistered(unittest.TestCase):

    def test_1_reg(self):
        #检查未注册数据返回
        for username,password in db_test_right.items():
            # print(username,':\t',password)
            self.assertEqual(UserRegistered(username,password).userReg(),'Reg ok')
        #检查已注册数据返回
        for username,password in db_test_false.items():
            # print(username,':\t',password)
            self.assertEqual(UserRegistered(username,password).userReg(), 'Username has already been registered!')

    def test_2_log(self):
        for username,password in db_test_right.items():
            # print(username,':\t',password)
            self.assertEqual(UserLogin(username,password).userLogin(),'Success!')
        #检查已注册数据返回
        for username,password in db_test_false.items():
            # print(username,':\t',password)
            self.assertEqual(UserLogin(username,password).userLogin(), 'Please cheack again!')


#-------------------------------------------------------
#-------------------------------------------------------

db_test_right = {'michael': '123456','bob': 'abc999','alice':'alice2008'}
db_test_false={'michael': '1234567','bob':'12 3456','alice':'Alice2008'}
if __name__ == '__main__':
    unittest.main()