from tkinter import *
import tkinter.messagebox as messagebox  #as代表命名别称


class Application(Frame):
	def __init__(self,master=None):
		Frame.__init__(self,master)
		self.pack()
		self.shuru()
		self.createWidgets()
		
		
	def createWidgets(self):
		self.helloLabel = Label(self,text='click to quit')
		self.helloLabel.pack()
		self.quitButton = Button(self,text='Quit',command=self.quit)
		self.quitButton.pack()
	
	def shuru(self):
		self.nameInput = Entry(self)
		self.nameInput.pack()
		self.alertButton = Button(self,text='hello',command=self.hello)
		self.alertButton.pack()
	
	def hello(self):
		name = self.nameInput.get() or 'world'
		messagebox.showinfo('Message','Hello,%s'%name)

	
app = Application()

app.master.title('Hello world')

app.mainloop()