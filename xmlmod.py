'''
举个例子，当SAX解析器读到一个节点时：
<a href="/">python</a>
会产生3个事件：

start_element事件，在读取<a href="/">时；
char_data事件，在读取python时；
end_element事件，在读取</a>时
'''

from xml.parsers.expat import ParserCreate

class DefaultSaxHandler(object):
	def start_element(self,name,attrs):
		print('sax:start_element: %s,attrs: %s'%(name,str(attrs)))
		
	def end_element(self,name):
		print('sax:end_element:%s '%name)
		
	def char_data(self,text):
		print('sax:char_data: %s'%text)
		
xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StarElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)

	k8sdev.api.tianbaows.com
	k8sdev.backend.tianbaows.com   1
	k8sdev.blackscreen.tianbaows.com  0
	k8sdev.ctriporder.tianbaows.com 
	k8sdev.farerule-service.tianbaows.com
	k8sdev.frontend.tianbaows.com  0
	k8sdev.metrics.tianbaows.com
	k8sdev.monitor-service.tianbaows.com
	k8sdev.orders.tianbaows.com  
	k8sdev.payment.tianbaows.com 
    k8sdev.s2b.tianbaows.com  0


	

