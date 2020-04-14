import sys
import codecs
import selenium
import requests
import time
import pyperclip
import mysql.connector
import os.path
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

url=sys.argv[1] #Input
print("What we crawled==> " + url)

filepath="success"
script=""

def obfuscate(first):
    ##########################난독화 해제 1차##############################
    driver.get("http://ddecode.com/hexdecoder/") #Hex Deobfuscation
    driver.find_element_by_name('text1').send_keys(first)
    driver.find_element_by_xpath('/html/body/div/pre/form/input').click() #unpack 버튼 클릭
    element=driver.find_element_by_xpath('/html/body/div/pre/textarea[2]')
    textarea=element.get_attribute("value")
    payload=str(textarea)
    pyperclip.copy(payload)
    second=pyperclip.paste()

    ##########################난독화 해제 2차##############################
    driver.get("https://www.strictly-software.com/unpack-javascript") #JsunPack Obfuscation
    driver.find_element_by_id('txtPacked').send_keys(second)
    driver.find_element_by_xpath('//*[@id="cmdUnpack"]').click() #unpack 버튼 클릭
    element=driver.find_element_by_xpath('//*[@id="txtUnpacked"]')
    textarea1=element.get_attribute("value")
    content=str(textarea1)

    ###########################시그니쳐 검출###############################
    conn = mysql.connector.connect(host='localhost', user='guest', password='1234', db='LIST', charset='utf8')
    cursor = conn.cursor()
    try:
        sql = 'SELECT * FROM SIGNATURE'
        cursor.execute(sql)
        result = cursor.fetchall()

        content=content.replace(" ","")
        content=content.replace("\t","")
        content=content.replace("\n","")

        for value in result:
            if list(value)[1] in content:
                attacktype=list(value)[0]
                target=list(value)[1]
                #mysql
                sql = 'INSERT INTO RESULT (ATTACKTYPE, TARGET) VALUES (%s, %s)'
                cursor.execute(sql, (attacktype, target))
                conn.commit()
    finally:
        conn.close()

##########################크롬드라이버 셋팅############################
options = Options()
options.binary_location = "/usr/bin/google-chrome"
options.add_argument('--no-sandbox')
options.add_argument('--headless')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('/usr/bin/chromedriver', chrome_options=options)#웹드라이버 위치 지정해줘라

##########################Full URL 획득###########################
driver.get("https://bitly.co.kr/") # blitly열어서 소스 가져오고
driver.find_element_by_name('url').send_keys(url) #url입력란에 입력
driver.find_element_by_xpath('//*[@id="about"]/div/div/div/form/button').click() #제출 버튼 클릭
html = driver.page_source # 제출한 결과페이지의 elements모두 가져오기
soup = BeautifulSoup(html, 'html.parser') # BeautifulSoup사용하기
notices = soup.select('#result > div > div > div > div:nth-of-type(1) > p:nth-of-type(3) > a') #fullUrl 선택하
tmp = repr(notices)#fullUrl 형변환(list->string)
extract_url = tmp.split('"')#split으로 url만 떼내기
url=extract_url[1]##############변수 url에 split한 url 저장(Full URL 획득)
Malicious_File=os.path.split(url)[1]###########디비에 저장할 확장자 변수로 받기
url=os.path.split(url)[0] #Full URL 획득

###############################Url 악성파일 검출################################
try:
    Malicious_FileExtension=Malicious_File.split('.')[1]
    Extension_List=['exe','jsp','php','aspx','bat','vbs']
    for i in Extension_List:
        if Malicious_FileExtension==i:
            AttackType="Drive By Download"
            break
        else:
            if i == 'vbs':
                url+="/"
                url+=Malicious_File
                AttackType="Others"
            else:
                continue
    conn = mysql.connector.connect(host='localhost', user='guest', password='1234', db='LIST', charset='utf8')
    cursor = conn.cursor()
    try:
        sql = """INSERT INTO RESULT (ATTACKTYPE, TARGET) VALUES (%s, %s)"""
        cursor.execute(sql, (AttackType, Malicious_File))
        conn.commit()
    finally:
        conn.close()

except IndexError as e:
    print("Safe")

#######################해당 URL 소스코드 출력#####################
req=requests.get(url)
source=req.text
file=codecs.open('success','w',encoding='utf-8') #success파일 생성
file.write(source)
file.close()

#########################File String Replace#########################
rep=codecs.open(filepath,'r')
content=rep.read()
content=content.replace(" ","")
content=content.replace("\t","")
req=codecs.open(filepath,'w',encoding='utf-8')

req.write(content)
req.close()
rep.close()

########################obfuscation Detect and Scan########################
with codecs.open(filepath,'r',encoding='utf-8') as file:
    lines=file.readlines()
with codecs.open(filepath,'w',encoding='utf-8') as file:
    for i in lines:
        if i.startswith("<script"):
            if "function(l,m)" not in i:
                file.write(i)
            else:
                script=i
                pyperclip.copy(script)
                first=pyperclip.paste()
                obfuscate(first)
        else:
            file.write(i)
    file.truncate()
###########################시그니쳐 검출###############################
try:
    conn = mysql.connector.connect(host='localhost', user='guest', password='1234', db='LIST', charset='utf8')
    cursor = conn.cursor()

    sql = 'SELECT * FROM SIGNATURE'
    cursor.execute(sql)
    result = cursor.fetchall()

    rep=codecs.open(filepath,'r')
    #made 1 Line
    tect=rep.read()
    tect=tect.replace("\"\n","")
    req=codecs.open(filepath,'w')
    req.write(tect)
    req.close()
    rep.close()

###위협코드 검출기
    tect=codecs.open(filepath,'r')
    for value in tect.readlines():
    #<noscript>#
        if value.startswith("<noscript>"):
            if 'height="0"' in value:
                attacktype="Threat Tag"
                target=value.replace("<","&lt;")
                sql = 'INSERT INTO RESULT (ATTACKTYPE, TARGET) VALUES (%s, %s)'
                cursor.execute(sql, (attacktype, target))
                conn.commit()
            elif 'height="1"' in value:
                attacktype="Threat Tag"
                target=value.replace("<","&lt;")
                #mysql
                sql = 'INSERT INTO RESULT (ATTACKTYPE, TARGET) VALUES (%s, %s)'
                cursor.execute(sql, (attacktype, target))
                conn.commit()
            else:
                continue
        else:
                continue
        #End#
        for value in result:
            if list(value)[1] in tect:
                attacktype=list(value)[0]
                target=list(value)[1]
                sql = 'INSERT INTO RESULT (ATTACKTYPE, TARGET) VALUES (%s, %s)'
                cursor.execute(sql, (attacktype, target))
                conn.commit()
            else:
                continue
finally:
    tect.close()
    conn.close()
    driver.close()#드라이버 닫고, 메모리에서 해제
    driver.quit()