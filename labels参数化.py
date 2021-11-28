import  requests
import unittest
import csv
import json
import numpy as np
from decimal import *
session = requests.Session()
#H:\test_samples\ocr\osd\OSDTEST\1.jpg 2018 9 14 7 25 52 0 北教学楼照南
'''data = {'TaskID': "1",
        'TaskType': 327705,
        'AnalysisRule': {"AlgParams": {"ResultImageDeclare": 0}},
        'RunAlways': "false",
        'ImageList': [{"ImageID": "1", "URI": "H:\test_samples\ocr\osd\OSDTEST\10.jpg"}]
        }
response = session.post("http://10.68.4.62:9100/AE/SyncTasks", json=data)
print(response.status_code)'''
file = open("labels.txt", "r")
f=open('labels.csv','w',encoding='utf-8',newline='' ) #文件名.csv’,‘w’,encoding=‘utf-8’"
csv_writer=csv.writer(f)
csv_writer.writerow(["图片","时间","地址"])
for x in file:
    a = x.split('.jpg')
    info1 = a[0] + ".jpg"
    data = a[1].split(" ")
    info3 = data[-1]
    info2 = a[1].replace(" ", "")
    info2 = info2.replace(info3, "")
    csv_writer.writerow([info1,info2,info3])
f.close()



def getstatus(url,i):
   # 准备参数2个
   data = {'TaskID': "1",
           'TaskType': 327705,
           'AnalysisRule': {"AlgParams":{"ResultImageDeclare":0}},
           'RunAlways':"false",
           'ImageList':[{"ImageID":i,"URI":url}]
           }
   response=session.post("http://10.68.4.97:9100/AE/SyncTasks",json=data)  #data=json.dumps(data)
   return  response

   #http://10.68.4.97:9100/AE/SyncTasks   10月14日接口地址
   # http://10.68.4.62:9100/AE/SyncTasks  10月13日接口地址
class PostAssert(unittest.TestCase):

   def test01(self):
    U'''测试接口json响应码'''
    num="1"
    counts=0
    success=0
    failure=0
    file = open("labels.txt", "r")
    for x in file:
       counts=counts+1
       a=x.split('.jpg')
       info1=a[0]+".jpg"  #.jpg之前为info1图片
       data=a[1].split(" ")
       info3=data[-1]  #最后一位空格之后的内容为地址
       info2=a[1].replace(" ","")
       info2=info2.replace(info3,"")#.jpg之后为info2+info3, 替换掉info3
       #info1=''   #传递空参数
       #info1=info1.replace("http://10.68.4.40/testset/data/app019/20210812/","http://10.68.4.40/testset/data/app019/20210812/")
       info1=info1[32:]
       info1="http://10.68.4.40/testset/data/app019/20210812/"+info1
       reponse=getstatus(i=num,url=info1)
       #print(reponse.status_code)
       comeout=str(reponse.json().get('TaskResult'))
       #print(comeout)
       INFOS2 = comeout[comeout.find("OSDTime") + 10:comeout.find("OSDAddr") - 3]  #返回的时间
       INFOS3=comeout[comeout.find("OSDAddr")+10:comeout.find("ImageID")-3] #返回的地址
       #print(INFOS2,INFOS3)
       #print('StatusCode:',reponse.status_code,'图片:',info1,'时间:',info2,'地址:',info3)

    print(counts,"wwww")

if __name__ == '__main__':
    unittest.main(verbosity=2)



