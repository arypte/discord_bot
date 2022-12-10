import datetime
import urllib
from bs4 import BeautifulSoup
import urllib.request as req

import ssl
context = ssl._create_unverified_context()
webpage = urllib.request.urlopen('https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=%EC%84%9C%EC%9A%B8%EB%82%A0%EC%94%A8',context=context)
soup = BeautifulSoup(webpage, 'html.parser')
temps = soup.find('div','temperature_text')
summary = soup.find('p','summary')

temper = []
if( temps.text.strip()[6] == '°' ) :
    temper = temps.text.strip()[5]
else :
    temper = temps.text.strip()[5] + temps.text.strip()[6] + temps.text.strip()[7]

s_r = summary.text.strip()[-2] + summary.text.strip()[-1]