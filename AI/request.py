import requests
import json
import base64
#url = "http://47.102.118.1:8089/api/problem" + "?stuid=031802245 }"
#url = "http://47.102.118.1:8089/api/challenge/list"
#url = "http://47.102.118.1:8089/api/challenge/create"创建赛题
#/api/challenge/start/<challenge-uuid>
url="http://47.102.118.1:8089/api/challenge/start/082cabb6-e227-4dbb-b5c6-680a1e45cd1a"
body = { "teamid": 41,
    "token": "38f216cd-c9fb-47ac-8075-c37f650c6892"}
#headers = {'token' = 38f216cd-c9fb-47ac-8075-c37f650c6892'}
headers = {'content-type': "application/json"}
#data = json.dumps(body)
 # 发送get请求
response = requests.request("post",url,headers=headers,json=body)
#print(response.text)bed7baa0-d7b8-4aaa-b488-eb3ca7be46dc
#user_dic=response.text
user_dic=response.json()
#print(user_dic)
data = user_dic['data']
#print(data)
img=data['img']
stepre=data['step']
uuid=user_dic['uuid']
swap = data['swap']
image_data = base64.b64decode(img)#解码图片
print(swap)
print(stepre)
print(uuid)
# answer={
#     "uuid": "3f6b8193-d71c-4363-8e3e-b8c9739335aa",
#     "teamid": 41,
#     "token": "38f216cd-c9fb-47ac-8075-c37f650c6892",
#     "answer": {
#         "operations": "d",
#         "swap": [2,3]
#     }
# }

#print(img)
# # 获取返回的json数据
# user_dic = r.json()
# data = user_dic['img']
# stepre=user_dic['step']
# uuid=user_dic['uuid']
# swap = user_dic['swap']

