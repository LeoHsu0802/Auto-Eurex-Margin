#coding=utf-8
 
import os
import time
import requests

#創建日期
date=time.strftime("%M%S%H%d%m%y")
date_for_file=time.strftime("%Y%m%d%H")
#存檔路徑
path=r"EurexMargin\\"+time.strftime("%y%m")+"\\"
#若無該路徑，則創建一個
if not os.path.isdir(r"EurexMargin\\"):
	os.mkdir(r"EurexMargin\\")

if not os.path.isdir(path):
	os.mkdir(path)
#檔名為 Eurex Margin_" 今日 年月日
file_name=("Eurex Margin_"+time.strftime("%Y")+time.strftime("%m")+time.strftime("%d")+".xls")
#取得檔案
dls = "http://www.eurexclearing.com/blob/2535516/f12a6596be2256ffcd3a14bd0a5d9f21/data/MarginParametersEstimationCircular.xls"
resp = requests.get(dls)
output = open(path+file_name, 'wb')
output.write(resp.content)
output.close()
