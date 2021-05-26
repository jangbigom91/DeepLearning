import requests
from bs4 import BeautifulSoup
import pandas

M = '&numOfRows=10&pageNo=1&stationName=측정소명&dataTerm=DAILY&ver=1.0'
key = 'zcMwE34ODFgJMnugYlzKk2qiqr%2BkvEOwbHd%2Brw%2FaDMktBXFrTUhxBnfopzPMrz5G4FWzm%2FPLqeGmfN1cCcqlQg%3D%3D'
url = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?serviceKey=' + key + M

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

ItemList = soup.findAll('item')

for item in ItemList:
    a = item.find('dataTime').text
    g = item.find('pm10Value').text
    i = item.find('pm25Value').text
    s = item.find('pm10Grade1h').text
    t = item.find('pm25Grade1h').text
    
    print('측정소 : 측정소명')
    print('측정시간 : '+a)
    print('미세먼지 농도 : '+ g + '㎍/㎥ (' + s + ')')
    print('초미세먼지 농도 : '+ i + '㎍/㎥ (' + t + ')')
    print('(좋음 : 1), (보통 : 2), (나쁨 : 3), (매우나쁨 : 4)')