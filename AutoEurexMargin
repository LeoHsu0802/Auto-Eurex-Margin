#coding=utf-8
 
import os
import time
import requests

date=time.strftime("%M%S%H%d%m%y")
date_for_file=time.strftime("%Y%m%d%H")

path=r"EurexMargin\\"+time.strftime("%y%m")+"\\"

if not os.path.isdir(r"EurexMargin\\"):
	os.mkdir(r"EurexMargin\\")

if not os.path.isdir(path):
	os.mkdir(path)

file_name=("Eurex Margin_"+time.strftime("%Y")+time.strftime("%m")+time.strftime("%d")+".xls")
dls = "http://www.eurexclearing.com/blob/2535516/f12a6596be2256ffcd3a14bd0a5d9f21/data/MarginParametersEstimationCircular.xls"
resp = requests.get(dls)
output = open(path+file_name, 'wb')
output.write(resp.content)
output.close()
