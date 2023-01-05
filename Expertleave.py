import requests
import json
import re
import datetime 
import sys
from time import strftime
from image2str import *
cookies = {
'tenantId':'ZF_JGBM_000016',
'JSESSIONID':'D4CE1E417E62E3C37EC34CF64954FDC3'
}

def Json2keyvalue(file):
	with open(file) as f:
	  data = json.load(f)
	  
	str1=re.findall("(?<=\[').*?(?='\])",str(data.keys()))
	print(str1[0])
	data=data[str1[0]]
	a=data['headers']
	headers={a[0]['name']:a[0]['value']} 

	
	for i in range(1,len(a)):
		temp={a[i]['name']:a[i]['value']}
		headers.update(temp)
	return headers
def getExpertleaveid():
	form="""jsonParam=%5B%7B%22name%22%3A%22sEcho%22%2C%22value%22%3A%221%22%7D%2C%7B%22name%22%3A%22iColumns%22%2C%22value%22%3A%226%22%7D%2C%7B%22name%22%3A%22sColumns%22%2C%22value%22%3A%22%2C%2C%2C%2C%2C%22%7D%2C%7B%22name%22%3A%22iDisplayStart%22%2C%22value%22%3A0%7D%2C%7B%22name%22%3A%22iDisplayLength%22%2C%22value%22%3A%2225%22%7D%2C%7B%22name%22%3A%22mDataProp_0%22%2C%22value%22%3A%22begintime%22%7D%2C%7B%22name%22%3A%22bSortable_0%22%2C%22value%22%3A%22true%22%7D%2C%7B%22name%22%3A%22mDataProp_1%22%2C%22value%22%3A%22endtime%22%7D%2C%7B%22name%22%3A%22bSortable_1%22%2C%22value%22%3A%22true%22%7D%2C%7B%22name%22%3A%22mDataProp_2%22%2C%22value%22%3A%22submittime%22%7D%2C%7B%22name%22%3A%22bSortable_2%22%2C%22value%22%3A%22true%22%7D%2C%7B%22name%22%3A%22mDataProp_3%22%2C%22value%22%3A%22leaveReason%22%7D%2C%7B%22name%22%3A%22bSortable_3%22%2C%22value%22%3A%22true%22%7D%2C%7B%22name%22%3A%22mDataProp_4%22%2C%22value%22%3A%22isUse%22%7D%2C%7B%22name%22%3A%22bSortable_4%22%2C%22value%22%3A%22true%22%7D%2C%7B%22name%22%3A%22mDataProp_5%22%2C%22value%22%3A%22leaveid%22%7D%2C%7B%22name%22%3A%22bSortable_5%22%2C%22value%22%3A%22true%22%7D%2C%7B%22name%22%3A%22iSortCol_0%22%2C%22value%22%3A0%7D%2C%7B%22name%22%3A%22sSortDir_0%22%2C%22value%22%3A%22desc%22%7D%2C%7B%22name%22%3A%22iSortingCols%22%2C%22value%22%3A%221%22%7D%5D&search="""
	url="http://zfcg.czt.fujian.gov.cn/gpms/expertLeave/list"
	headers=Json2keyvalue('getExpertleaveidHeaders.json')
	resp=requests.post(url,form,headers=headers,cookies=cookies)
	text=json.loads(resp.text)
	List=[]
	for i in range(0,20):
		List.append(text['aaData'][i]['leaveid'])
	return List
def deleteExpertLeave(leaveid):
	headers=Json2keyvalue('deleteExpertLeaveHeaders.json')
	#print(headers)
	ret=[]
	url="http://zfcg.czt.fujian.gov.cn/gpms/expertLeave/del"
	for i in range(0,len(leaveid)):
		form = """id="""+leaveid[i]
	#print(form)
		resp=requests.post(url,form,headers=headers,cookies=cookies)
		ret.append(resp.text)
	#print(resp.headers)
	return ret
def addExpertleave(end_year,end_month,end_day,end_hour,end_minute):
	now=datetime.datetime.now().strftime("%Y-%m-%d+%H"+"""%%3A"""+"%M")
	headers=Json2keyvalue('addExpertleaveHeaders.json')
	url="http://zfcg.czt.fujian.gov.cn/gpms/expertLeave/addExpertLeave"
	Data="""begintime="""+now+"""&endtime="""+end_year+"-"+end_month+"-"+end_day+"""+"""+end_hour+"""%3A"""+end_minute+"""&leaveReason=%E8%AF%B7%E5%81%87"""
	##print(Data)
	resp=requests.post(url,Data,headers=headers,cookies=cookies)
	##print(resp.headers)
	return resp.text
def addExpertleaveOffset(offset):
	now=datetime.datetime.now().strftime("%Y-%m-%d+%H"+"""%%3A"""+"%M")
	Expire=(datetime.datetime.now()+datetime.timedelta(hours=offset)).strftime("%Y-%m-%d+%H"+"""%%3A"""+"%M")
	headers=Json2keyvalue('addExpertleaveHeaders.json')
	url="http://zfcg.czt.fujian.gov.cn/gpms/expertLeave/addExpertLeave"
	Data="""begintime="""+now+"""&endtime="""+Expire+"""&leaveReason=%E8%AF%B7%E5%81%87"""
	##print(Data)
	resp=requests.post(url,Data,headers=headers,cookies=cookies)
	##print(resp.headers)
	return resp.text
def autoSetCookies():
#	headers=Json2keyvalue('logopage.json')
#	url='http://zfcg.czt.fujian.gov.cn/gpms/'
#	resp=requests.get(url,headers=headers)
#	print(resp.cookies)
	headers=Json2keyvalue('1.json')
	##print(headers)
	url='http://zfcg.czt.fujian.gov.cn/gpms/supplierReg/captcha?t=1672841466417'	

	resp=requests.post(url,headers=headers)
	with open('picture.jpg',"wb") as f:
		f.write(resp.content)

	res=image2str('picture.jpg')

	print(res)
	headers=Json2keyvalue('2.json')
	url='http://zfcg.czt.fujian.gov.cn/gpms/user/logon'##未填写账户
	form="""port=zfcg.czt.fujian.gov.cn&loginType=&username=&password=6182d67a0cde17c018912a67e1ea5a3b&orgRoleCode=3&checkcode="""+res+"""&checkcodeNone="""
	resp=requests.post(url,form,headers=headers)
	return resp.text
	#with open('a.json',mode='w+') as f:
	 #f.write(resp.text)
	 #data = json.load(f)
	#print(data)
#addExpertleaveOffset(3)

#if sys.argv[1] is "0":
#print(addExpertleave("2022","12","26","1","17"))##请假申请 直到2022年12月26日1时17分为止
#if sys.argv[1] is "1":
	#leaveid=getExpertleaveid()
	#deleteExpertLeave(leaveid)
