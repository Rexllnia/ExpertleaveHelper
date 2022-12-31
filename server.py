import json
from sanic import Sanic
from Expertleave import *

app=Sanic('qqbot')
base_path="/onoebot/keyword/"
##{"post_type":"message","message_type":"private"...raw_message":"到底滚滚滚"}
@app.websocket('/qqbot/')
async def qqbot(request,ws):
	mode=0
	while True :
		data =await ws.recv()
		data =json.loads(data)
		print(json.dumps(data))
		if data.get('message_type')=='private' and data.get('raw_message'):
			raw_message =data['raw_message']
			if mode==1:
				if raw_message=='5':			
					leaveid=getExpertleaveid()
					ret = {'action':'send_private_msg',
						'params':{
							'user_id':328626536,
							'message':leaveid
						} 
					}
					await ws.send(json.dumps(ret))
					msg=deleteExpertLeave(leaveid)[0]
					ret = {'action':'send_private_msg',
						'params':{
							'user_id':328626536,
							'message':msg
						} 
					}

					await ws.send(json.dumps(ret))
					raw_message = ''	
					mode=0
				else:
					msg='当前请假未作废 发送5作废'
					ret = {'action':'send_private_msg',
						'params':{
							'user_id':328626536,
							'message':msg
						} 
					}

					await ws.send(json.dumps(ret))
					raw_message = ''	
					mode=1
			elif mode==0:
				if raw_message =='1':
					msg=addExpertleaveOffset(1)
					ret = {'action':'send_private_msg',
						'params':{
							'user_id':328626536,
							'message':msg
						} 
					}
					await ws.send(json.dumps(ret))
					raw_message = ''	
					mode=1
				elif raw_message =='2':
					
					msg=addExpertleaveOffset(2)
					ret = {'action':'send_private_msg',
						'params':{
							'user_id':328626536,
							'message':msg
						} 
					}
					await ws.send(json.dumps(ret))
					raw_message = ''	
					mode=1
				elif raw_message =='3':
					msg=addExpertleaveOffset(3)
					ret = {'action':'send_private_msg',
						'params':{
							'user_id':328626536,
							'message':msg
						} 
					}
					await ws.send(json.dumps(ret))
					raw_message = ''	
					mode=1					
				elif raw_message =='4':
					msg=addExpertleaveOffset(3)
					ret = {'action':'send_private_msg',
						'params':{
							'user_id':328626536,
							'message':msg
						} 
					}
					await ws.send(json.dumps(ret))
					raw_message = ''	
					mode=1
				else:
					mode=0
					msg='选择请假时间\n1请假1小时\n2请假2小时\n3请假3小时\n4请假4小时\n5请假作废'
				#msg=addExpertleave("2022","12","26","1","17")
					ret = {'action':'send_private_msg',
						'params':{
							'user_id':328626536,
							'message':msg
						} 
					}
					await ws.send(json.dumps(ret))

			
if __name__ =='__main__':
	app.run(debug=True,port=7777,auto_reload=True)
			
