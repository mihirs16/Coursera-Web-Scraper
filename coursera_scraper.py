import urllib.request
import requests
import bs4
import os
import time
import warnings

import pandas as pd
import numpy as np

from multiprocessing import Pool
from bs4 import BeautifulSoup
from selenium import webdriver

def scraper(page):
    lst_name = []
    lst_link = []

    driver = webdriver.PhantomJS(os.getcwd() + "/dependency/phantomjs-2.1.1-windows/bin/phantomjs.exe")

    url = 'https://www.coursera.org/directory/courses?page=' + str(page)
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

warnings.simplefilter('ignore')
if __name__ == '__main__':
    start = time.time()

    choke = np.arange(1, 115, 10)[:-1]
    lst_name = []
    lst_link = []
    data_main = {'Name': lst_name, 'Link':lst_link}
    for i in choke:
        
        p = Pool(10)
        data = p.map(scraper, range(i, i+10))
        p.terminate()
        p.join()
        
        lst_name = []
        lst_link = []
        _data = {'Name': lst_name, 'Link':lst_link}
        for d in data:
            _data['Name'] += d['Name']
            _data['Link'] += d['Link']
        
        data_main['Name'] += _data['Name']
        data_main['Link'] += _data['Link']

    print(data_main)
    end = time.time()
    print(str(len(data_main['Name'])) + ' items in ' + str(end-start) + ' seconds')

    pd.DataFrame(data=data_main).to_csv('coursera-course-data.csv')