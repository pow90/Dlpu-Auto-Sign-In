import requests
api = "https://sc.ftqq.com/你的SCKEY.send"
title = "签到成功"
content = "已填写您有新型冠状病毒肺炎，提交成功。开玩笑的~~"
data = {
   "text" : title,
   "desp" : content
}
req = requests(api, data = data)
