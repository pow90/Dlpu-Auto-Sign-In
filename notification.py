# coding=gbk
import requests
api = "https://sc.ftqq.com/你的SCKEY.send"
title = "签到成功"
content = "主人，签到成功啦！"
data = {
   "text" : title,
   "desp" : content
}
req = requests.post(api, data = data)
