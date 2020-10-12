import requests
import base64
url = "http://47.102.118.1:8089/api/problem" + "?stuid=031802245 }"
 # 发送get请求
r = requests.get(url)
#获取返回的json数据
user_dic = r.json()
data = user_dic['img']
step=user_dic['step']
uuid=user_dic['uuid']
swap = user_dic['swap']
image_data = base64.b64decode(data)#解码图片
