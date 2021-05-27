# import time
# from selenium import webdriver

# 웹드라이버 설치
# driver = webdriver.Chrome('/C:/Users/ad/Documents/GitHub/DeepLearning/chromedriver')

# driver.get('http://www.google.com') # 구글 접속
# time.sleep(2) # 2초간 동작 확인

# search_box = driver.find_element_by_name('q')
# search_box.send_keys('ChromeDriver')
# search_box.submit()

# time.sleep(2)
# driver.quit() # 종료

# 오스카 2020 수상장 명단 크롤링(안됨)
import time
import pandas as pd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager   # pip install webdriver-manager
from bs4 import BeautifulSoup

#크롬 가상브라우저 실행
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://oscar.go.com/winners')
time.sleep(1)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

category = soup.select('bls-winners-list > ul > li > div.winners-list__info > a')
movie = soup.select('bls-winners-list > ul > li > div.winners-list__info > h3 > a')
producer = soup.select('bls-winners-list > ul > li > div.winners-list__info > p')

oscars_2020 = []
for item in zip(category, movie, producer):
    oscars_2020.append(
        {
            'category' : item[0].text,
            'movie' : item[1].text,
            'producer' : item[2].text   
        }
    )

data = pd.DataFrame(oscars_2020)
print(data)

data.to_csv('oscars_2020.csv')

driver.quit()