# import urllib.request

# url = 'http://www.douban.com'
# data = urllib.request.urlopen(url).read()
# data = data.decode('UTF-8')
# print(data)
# print(type(data))
# print(data.geturl())
# print(data.info())
# print(data.getcode())

# a='ch'
# b='in'
# c='a'
# q='m'
# w='a'
# e='n'
# print(a+b+c,q+w+e)

# def solution1(digits='129823249898923432432'):
	# value = []
	# for i in range(len(digits)):
		# if digits[i] == '9':
		    # value.append(''.join(digits[i:i+5]))
		# else:   
		    # pass
	# print(value)
	# return max(value)


# solution1()	


# 用gui生成一个计算bmi方法
from tkinter import *
import tkinter.messagebox as messagebox

def BMI(high,weigh):
    check = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
    for i in list(high):
        if i not in check:
            return ("参数输入有误，请输入数字。")

    for i in list(weigh):
        if i not in check:
            return ("参数输入有误，请输入数字。")

    if not high or not weigh:
        return None

    BMI =  float(weigh) / float(high) **2

    if BMI < 18.5 :
        return ('您的BMI指数为%.2f，您的身体情况属于过轻。' % BMI)
    elif BMI <= 25:
        return ('您的BMI指数为%.2f，您的身体情况属于正常。' % BMI)
    elif BMI <= 28:
        return ('您的BMI指数为%.2f，您的身体情况属于过重。' % BMI)
    elif BMI <= 32:
        return ('您的BMI指数为%.2f，您的身体情况属于肥胖。' % BMI)
    else:
        return ('您的BMI指数为%.2f，您的身体情况属于严重肥胖。' % BMI)

class Application(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.label1 = Label(self,text = '请输入您的身高:')
        self.label1.pack()
        self.nameInput1 = Entry(self)
        self.nameInput1.pack()
        self.label2 = Label(self,text = '请输入您的体重:')
        self.label2.pack()
        self.nameInput2 = Entry(self)
        self.nameInput2.pack()
        self.alertButton = Button(self,text='点击显示结果',command = self.result)
        self.alertButton.pack()

    def result(self):
        BMI_result = BMI(self.nameInput1.get(),self.nameInput2.get()) or '请输入您的参数'
        messagebox.showinfo("BMI转换结果",'%s' % BMI_result )

app = Application()
app.master.title("BMI转换器")
app.mainloop()