import itertools
import shutil
import json
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
from PIL import Image
import time
from module.firebase_connect import FIREBASE_URL
import csv
import tkinter
from tkinter import font
from module.common import callback1, callback2

# 參數設定
list1 = ['7-11', 'sogo', 'fami']
list2 = ['mac', 'mos burger', 'burger king']
list3 = ['mitsukoshi', 'da-huo', 'star-bucks']
list4 = list('ABCDE')
# ====================================================================

# ■ 資料組合工具 itertools.chain
c1 = itertools.chain(list1, list2, list3)
# print(c1, type(c1))
# print([c for c in c1])
# print([c for c in c1])  # this will empty
c2 = tuple(itertools.chain(list1, list2, list3))
# print([c for c in c2])
# print([c for c in c2])  # this wont empty
# ====================================================================

# ■ 資料排列組合工具 itertools.per有順序/com無關順序
per1 = tuple(itertools.permutations(list4, 2))
# print(len(per1))
# print(per1)
cob1 = tuple(itertools.combinations(list4, 2))
# print(len(cob1))
# print(cob1)
# ====================================================================

# ■ shutil 目錄管理
SOURCE = "./origin"
TARGET = "./copy"

# shutil.copytree(SOURCE, TARGET)  # 複製目錄，若已存在會噴錯
# shutil.rmtree(TARGET)  # 刪除目錄，若不存在會噴錯
# ====================================================================

# ■ json 轉換
# json(UTF8)/python(UTF16) =>中文會有編碼不同問題
x1 = [1, 2, 3, 'Hello', 4.0, {"name": 'Mark', "age": 43, "location": "台北"}, None, [4, 3, 2, 1]]

y1 = json.dumps(x1)  # 轉換為json
# print(type(y1), y1)  # str
# print(y1[:10])
z1 = json.loads(y1)  # 轉換回來
# print(type(z1), z1)  # list
# for z in z1:
#     print(z)
#     if isinstance(z, list):
#         for zz in z:
#             print("list content:", zz)
# ====================================================================

# ■ requests連線
URL = "https://bugzilla.mozilla.org/rest/bug/35"
response1 = requests.get(URL)
# print(response1.status_code, type(response1))   # 200 <class 'requests.models.Response'>
# print(type(response1.content))  # <class 'bytes'>
# print(type(response1.json()))  # <class 'dict'>
for k in response1.json():
    #     print(k)
    pass
bugs = response1.json()["bugs"]
for bug in bugs:
    #     print(bug)
    pass
# ====================================================================


# ■ 爬恆逸網站源碼
URL = "https://www.uuu.com.tw"
response1 = requests.get(URL)
# print(type(response1.content), len(response1.content))  # <class 'bytes'> 63099
soup = BeautifulSoup(response1.content, "html.parser")
courseList = soup.find('div', {'id': "course_list"})  # get element by tag/tag attr
# print(type(soup))  # <class 'bs4.BeautifulSoup'>
# print(soup.title.name)  # title
# print(soup.title.string.lstrip())  # 空白消除strip() lstrip()左空白 rstrip()右空白
# print("=%s=" % soup.title.string.strip())
# ====================================================================

# ■ BeautifulSoup 取得HTML網頁碼
for course in courseList:
    # print(type(course))
    # print(course)
    pass

courseLink = courseList.find_all('a')
for link in courseLink:
    # print(link.p)  # get tags<p> in tag('a')
    # print(link.p.getText())  # get tags<p> innerText in tag('a')
    # print("https://www.uuu.com.tw" + link.get('href'))  # get tag('a') attr
    pass
# ====================================================================

# ■ Image.open抓取圖片 存至本地端
DIR = "./images/"  # 存檔位置
imgUrlList = courseList.find_all('img')  # 抓取course_list下所有圖片
for imgLink in imgUrlList:
    imgUrl = 'https://www.uuu.com.tw/' + imgLink.get('src')  # 該圖片網址
    originalImage = Image.open(urlopen(imgUrl))
    filename = imgUrl.split('/')[-1]  # 取得檔名
    # originalImage.save(DIR + filename)  # 存檔

    # 圖片編輯
    # 調整長/2, 寬/2 (//為除為整數)
    halfSize = (originalImage.size[0] // 2, originalImage.size[1] // 2)
    halfImage = originalImage.resize(halfSize, Image.ANTIALIAS)
    # 旋轉
    rot1 = halfImage.transpose(Image.ROTATE_90)
    rot2 = halfImage.rotate(45)  # 任意角度
# ====================================================================

# ■ FireBase
# ▼ put新增資料，會覆寫舊資料
# o1 = "hello world"
# r1 = requests.put(FIREBASE_URL % "db_1027_1", json=o1)
# print(r1.status_code, r1.json())
# o2 = "你好，世界"
# r2 = requests.put(FIREBASE_URL % "db_1027_2", json=o2)
# print(r2.status_code, r2.json())

# ▼ post會在中間層另外建新的key，所以不會蓋掉舊的
# o3 = "try post"
# r3 = requests.post(FIREBASE_URL % "db_1027_3", json=[o3, o3, o3])
# print(r3.status_code, r3.json())

# ▼ get data (.json會轉為py物件)
# g1 = requests.get(FIREBASE_URL % "db_1027_1")
# print(type(g1.content), g1.content)  # <class 'bytes'> b'"hello world"'
# print(type(g1.json()), g1.json())  # <class 'str'> hello world

# ▼ 更新 patch，若原物件型態不同則會蓋掉，若可以push list等就會以upsert形式更新
# o4 = {'0': "apple", "3": "甜甜圈", "10": "jacky"}
# r1 = requests.patch(FIREBASE_URL % "db_1027_2", json=o4)

# ▼ 刪除 delete
dbs = ["db_1027_1", "db_1027_2"]
for db in dbs:
    # requests.delete(FIREBASE_URL % "")  # 刪除全部
    # response1 = requests.delete(FIREBASE_URL % db)
    # print(response1.status_code, response1.json())
    pass
# ====================================================================

# ■ clone file
FILENAME = 'others/Python_Introduction'
W1 = 'others/clone_pyIntro_1'
W2 = 'others/clone_pyIntro_2'

# ▼ 讀取檔案
# file1 = open(FILENAME, encoding='UTF-8')
# content_string1 = file1.read()
# print(type(content_string1), len(content_string1))
# print(content_string1[:10])
# file1.close()

# ▼ 讀取檔案，會自行關閉檔案
# with open(FILENAME, encoding='UTF-8') as file2:
#     content_string2 = file2.read()
#     print(type(content_string2), len(content_string2))
#     print(content_string2[:10])

# ▼ 寫檔w，增加內容a
# file3 = open(W1, 'w', encoding='UTF-8')
# file3.write(content_string1)
# file3.close()

# ▼ 寫檔w，增加內容a
# with open(W2, 'w', encoding='UTF-8') as file4:
#     file4.write(content_string2)
# with open(W2, 'a', encoding='UTF-8') as file4:
#     file4.write(content_string2)
# ====================================================================

# ■ c讀CSV檔
sampleFile = open('others/demoCsv.csv', encoding="utf-8")  # 若原檔編碼有不同，須設定encode，否則decode會有錯
sampleReader = csv.reader(sampleFile)
sampleData = list(sampleReader)
#
# print(type(sampleData))
# for row in sampleData:
#     print(row)
#     for col in row:
#         print(col)
# sampleFile.close()
# ====================================================================

# ■ tkinter 應用程式設計圖形化介面 obj.pack()將物件加入介面
# for f in font.families():  # 取得字型列表
#     print(f)

# ▼ 呼叫方法
top = tkinter.Tk()
font1 = font.Font(family="Linux Libertine G", size=36)
button1 = tkinter.Button(top, text='button1', font=font1, command=callback1)
button2 = tkinter.Button(top, text="button2", font=font1, command=callback2)
button2.pack()
button1.pack()

# ▼ 呼叫方法，並使用變數
label1 = tkinter.Label(top, text="", font=font1)
label2 = tkinter.Label(top, text="", font=font1)
counter = 0
l1 = [0]


def printTimes():
    global counter  # 若mutable值要作修改，需以global設置
    message = "button3 is clicked %d times"
    label1.config(text=message % counter)
    counter += 1


def printTimes2():
    message = "button4 is clicked %d times"
    label2.config(text=message % l1[0])
    l1[0] += 1


label1.pack()
tkinter.Button(top, text='button3', font=font1, command=printTimes).pack()
label2.pack()
tkinter.Button(top, text="button4", font=font1, command=printTimes2).pack()


# ▼ 呼叫方法，並對移到message1上時偵測滑鼠動向
label3 = tkinter.Label(top, text="", font=font1)


def observe1(event):
    label3.config(text="move to (%d,%d)" % (event.x, event.y))
    print(event)


label3.pack()
message1 = tkinter.Message(top, text="status", font=font1)
message1.bind('<Motion>', observe1)
message1.pack()

# 大小控制
# top.minsize(400, 200)
# top.maxsize(400, 200)
# top.mainloop()  # 啟動介面,監控
# ====================================================================

# ■ tkinter 應用程式設計圖形化介面 obj.pack()將物件加入介面


def getVolumn(s):
    label.config(text=message % int(s))


message = "value=%d"
top2 = tkinter.Tk()
font1 = font.Font(family="Linux Libertine G", size=36)
label = tkinter.Label(top2, text=message % 0, font=font1)
scale1 = tkinter.Scale(top2, label='volume', orient='h', from_=0, to=100, font=font1, command=getVolumn)
label.pack()
scale1.pack()
top2.minsize(600, 200)
top2.maxsize(600, 200)
top2.mainloop()

# ====================================================================
