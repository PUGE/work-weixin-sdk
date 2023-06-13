import json
from wechat_sdk import *

we = WeChatEnterprise()
we.__init__(agentid="你的应用id", corpsecret="你的应用secret")
# 发送应用消息
data = we.send_msg_to_user('asdasd')
# 其他方法类似， 注意是否有这个权限调用这些接口
print(data)
    