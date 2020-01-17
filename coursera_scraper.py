import urllib.request
import requests
import bs4
import thread

import pandas as pd
import numpy as np

from bs4 import BeautifulSoup
from selenium import webdriver

def scraper(start_page, end_page):
    lst_name = []
    lst_link = []

    for i in range(start_page, end_page+1):
        driver = webdriver.PhantomJS("C:/Users/Powerhouse/Desktop/Scrapping Coursera/dependency/phantomjs-2.1.1-windows/bin/phantomjs.exe")

        page_no = i
        url = 'https://www.coursera.org/directory/courses?page=' + str(page_no)

        driver.get(url)
        res = driver.execute_script("return document.documentElement.outerHTML")
        driver.quit()

        soup = BeautifulSoup(res, 'lxml')
        c_link = soup.findAll('a', {'class':'c-directory-link'}, href=True)

        for c in c_link:
            lst_name.append(c.getText())
            lst_link.append('https://coursera.org' + str(c['href']))
    
    data_dict = {'Name':lst_name, 'Link':lst_link}
    return data_dict

df = pd.DataFrame(scraper(1, 3))
print(df)
