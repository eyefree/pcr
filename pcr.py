from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import csv
import pandas as pd

def scratch_pcr():
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

    with open("pcr.csv", 'w', encoding='UTF-8', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["时间", "标签", "事件", "内容"])
        contents = driver.find_elements_by_class_name("article_box")
        for content in contents:
            row = []
            article = content.text
            list = article.split()
            #插入时间
            row.append(list[0])
            #插入标签
            row.append(list[1])
            #插入事件
            row.append(list[2])
            #插入内容
            row.append("".join(list[3::]))
            writer.writerow(row)

    df = pd.read_csv("pcr.csv")
    df.to_excel("pcr.xlsx", 'sheet1')

    print("数据抓取完成!")
scratch_pcr()
            
