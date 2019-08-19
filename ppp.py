#-*- coding: UTF-8 -*-

import requests
from bs4 import BeautifulSoup
import urllib

#로그인 페이지 URL
login_url="http://192.168.129.129/member/index.asp"


#로그인 페이지에 필요한 파라미터
params = {'cmd':'loginok','id':'abc11','pwd':'1234'}

#url에 data(파라미터)를 넣어 post 방식으로 요청하여 결과값 response에 저장
response = requests.post(url=login_url, data=params,allow_redirects=False)

#response header에 Set-cookie를 수집 하여 session 변수에 저장
session= response.headers['Set-Cookie']
session_text=session.split(',')[1].split(';')[0]
#session_text = 'BHEJKHEBKHMLOBDBFEKKBGOO;'

#session 값을 header에 cookie로 저장하여 전달
headers={}
headers['COOKIE']=session_text.replace(' ','')

#자료를 조회할 URL을 url2에 저장
url2 = "http://192.168.129.129/security/1/index.asp"

#url2에 header를 첨부하여 get방식으로 호출 -> list_res에 응답값 저장
list_res = requests.get(url=url2,headers=headers)

#beautifulsoup를 통하여 html로 파싱
soup=BeautifulSoup(list_res.content,'html.parser')

# 모든 'a' Tag 수집하여 aa에 저장
aa = soup.find_all("a")

#aa 에 저장된 내용을 for문을 통하여 한줄 한줄 호출
for link in aa:
    if 'href' in link.attrs: #호출된 내용 중 href가 있을 경우만 아래의 ㄴ내용 ㅅ실행
        print link.attrs['href'] #호출된 내용 중 href 파라미터의 데이터만 출력
