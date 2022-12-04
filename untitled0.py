# 웹 사이트 접속 후 검색하기, 페이지 열기
# -*- coding: utf-8 -*-
 
import time
import datetime
from selenium import webdriver
 
# Chrome WebDriver를 이용해 Chrome을 실행한다.
 
 
# 오늘 날짜를 계산한다
d = str(datetime.datetime.now().day)  
m = str(datetime.datetime.now().month)
query = m + '월' + d + '일 멜론'
query2 = m + '월' + d + '일'
 
driver.get("https://www.youtube.com/results?search_query=" + query)
time.sleep(1)
 
# 검색된 내용 중 링크 텍스트에 "{month}월 {day}일" 이 포함된 것을 찾는다.
continue_link = driver.find_element_by_partial_link_text(query2)
 
# 해당 링크를 클릭한다.
continue_link.click()

