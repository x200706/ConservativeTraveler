import json
import os
import requests as req

# 先問使用者要從哪邊到哪邊旅行'w'
print('請輸入你的出發地～')
start = input('起點：')
print('請輸入你的目的地～')
end = input('終點：')

# 開json
url = "https://dev.virtualearth.net/REST/v1/Routes/Transit?wayPoint.1=" + start + "&wayPoint.2=" + end + "&key=" + os.environ[
    'BINGMAPAPIKEY']
res = req.get(url)
# 轉json_str為dict
json_obj = res.json()
# 輸入想搜尋的key
target_key = 'travelDuration'


# 遞迴搜尋
def search_key(json_obj, target_key, target_value_arr):
  # 最外層會先遇到字典吧，先寫字典的判斷
  if isinstance(json_obj, dict):
    for k, v in json_obj.items():
      if k == target_key:
        target_value_arr.append(v)
      elif isinstance(v, (dict, list)):
        # 這是說如果解析，key不是我們要搜尋的，就繼續查找，看型態是物件還是陣列
        search_key(v, target_key, target_value_arr)
  elif isinstance(json_obj, list):  # 如果解析到陣列就分析陣列每個元素
    for node in json_obj:
      search_key(node, target_key, target_value_arr)


# 輸出結果
target_value_arr = []
search_key(json_obj, target_key, target_value_arr)  # sec
# print(target_value_arr)
min = max(target_value_arr) / 60
print('共花', min, '分')
