from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import csv
import pandas as pd
import urllib.request

def scratch_pcrImg():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get("https://priconne-redive.jp/news/")
    flag = True
    count = 1
    while(flag):
        try:
            driver.find_element_by_xpath("//*[@id='next']/a").click()
            print('第', count, '次')
            count += 1
            time.sleep(2)
        except NoSuchElementException:
            flag = False
            print('已经达到页面底部!')
    images = driver.find_elements_by_class_name("attachment-news-thumbnail")
    n = 0
    for image in images:
        src = image.get_attribute("src")
        urllib.request.urlretrieve(src, str(n) + '.jpg')
        n += 1

scratch_pcrImg()
