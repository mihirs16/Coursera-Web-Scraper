import urllib.request
import requests
import bs4
import os
import time
import warnings
import sys

import pandas as pd
import numpy as np

from multiprocessing import Pool
from bs4 import BeautifulSoup
from selenium import webdriver

sys.setrecursionlimit(25000)

def common_member(a, b):  
    c = [value for value in a if value in b]
    if c != []:
        return c[0]
    else:
        return 'None'

def deep_scraper(url):
    print(url)
    driver = webdriver.PhantomJS(os.getcwd() + "/dependency/phantomjs-2.1.1-windows/bin/phantomjs.exe")
    driver.get(url)
    res = driver.execute_script("return document.documentElement.outerHTML")
    driver.quit()

    soup = BeautifulSoup(res, 'lxml')

    name = soup.findAll('h1')
    if name != [] and name != None:

        name = name[0].getText()

        ratingContainer = soup.findAll('div', {'class':'courseRatingContainer_1g3e6m'})
        if ratingContainer != [] and ratingContainer != None:
            rating = ratingContainer[0].findAll('span')
            if rating != []:
                rating = rating[0].contents[1]
            else:
                rating = 'None'
        else:
            rating = 'None'

        _difLevel = soup.findAll('h4')
        difLevel = []
        for d in _difLevel:
            difLevel.append(d.getText())
        difLevel = common_member(difLevel, ['Beginner Level', 'Intermediate Level', 'Advanced Level'])

        tagContainer = soup.findAll('div', {'class':'BreadcrumbItem_1pp1zxi'})
        if len(tagContainer) > 3 and tagContainer != None:
            tags = [tagContainer[1].contents[0].getText(), tagContainer[2].contents[0].getText()]
        else:
            tags = 'None'

        data_dict = {'Name': name, 'Url': url, 'Rating': rating, 'Difficulty': difLevel, 'Tags': tags}

    else:
        data_dict = {'Name': 'None', 'Url': url, 'Rating': 'None', 'Difficulty': 'None', 'Tags': 'None'}
    #print(data_dict)
    return data_dict

if __name__ == '__main__':
    df = pd.read_csv('coursera-course-data.csv')
    df.columns = ['index', 'name', 'url']

    try:
        _df = pd.read_csv('coursera-couse-detail-data.csv')
        isEx = True
    except:
        isEx = False

    if(isEx):
        url = list(set(df.url)-set( _df.Url))
    else:
        url = df.url
    
    tot = len(url)
    print(tot)
    if tot >= 1:
        choke = np.arange(1, tot+1, 10)
        #choke = range(1, tot+1)
        data_dict = {'Name': [], 'Url': [], 'Rating': [], 'Difficulty': [], 'Tags': []}

        for i in choke:
            try:
                _df = pd.read_csv('coursera-couse-detail-data.csv')
                isEx = True
            except:
                isEx = False
            
            
            mul = 10
            p = Pool(mul)
            _data = p.map(deep_scraper, url[i:i+mul])
            p.terminate()
            p.join()

            _data = [deep_scraper(url[i])]
            _data_dict = {'Name': [], 'Url': [], 'Rating': [], 'Difficulty': [], 'Tags': []}
            for d in _data:
                _data_dict['Name'].append(d['Name'])
                _data_dict['Url'].append(d['Url'])
                _data_dict['Rating'].append(d['Rating'])
                _data_dict['Difficulty'].append(d['Difficulty'])
                _data_dict['Tags'].append(d['Tags'])


            print(_data_dict)
            if(isEx):
                pd.DataFrame(data=_data_dict).to_csv('coursera-couse-detail-data.csv', mode='a', header=False)
            else:
                pd.DataFrame(data=_data_dict).to_csv('coursera-couse-detail-data.csv')
    else:
        print('done')
        time.sleep(2)