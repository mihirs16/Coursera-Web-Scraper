# Coursera-Web-Scraper
![](https://img.shields.io/github/issues-closed/mihirs16/Coursera-Web-Scraper?color=green&style=for-the-badge)
![](https://img.shields.io/github/forks/mihirs16/Coursera-Web-Scraper?style=for-the-badge)
![](https://img.shields.io/github/stars/mihirs16/Coursera-Web-Scraper?color=54A5B4&style=for-the-badge)
## Prerequisites
* Python (tested for 3.7 and above)
* [PhantomJs](https://phantomjs.org/) or any other headless browser for automation.
* [Selenium](https://selenium-python.readthedocs.io/) Web Driver for Python
* Other Libraries:
  * Pandas
  * Mutliprocessing

## Instructions
<ol>
  <li>Make sure PhantomJs is copied into the dependency folder. (You can also use a browser of your choice. More details <a href="https://towardsdatascience.com/web-scraping-using-selenium-python-8a60f4cf40ab">here</a>)</li>
  <li>Run coursera_scraper.py to scrape and save the list of coursera courses and their URLs mentioned in the <a href="https://www.coursera.org/directory/courses">Coursera Directory</a>.</li>
  <li>Run coursera_deep_scraper.py to scrape and save the details of all courses from the list of courses previously scraped.</li> 
</ol>

## Disclaimer:-
<ol>
  <li>Data is all around us, but this doesn't mean we own it. Please respect the policies of Coursera and the website <a href="https://coursera.org">Coursera.org</a>. Please be respectful of the website and avoid spamming it with continuous zero delay or parallel requests. You can check the website's scraping policy <a href="https://www.coursera.org/robots.txt">here</a>.</li>
  <li>Since Coursera and all websites take measures to handle multiple parallel requests, one might face "Connection closed" during long period of scraping. You can continue the scraping by restarting the script, if left undisturbed, the script reads the courses scraped from the list of courses, and the courses left. Thus letting you continue from where you left off. (Once again reminding you to respect the website and it's policies).</li>
</ol>

Uploaded Datasets:- <br>
https://www.kaggle.com/mihirs16/coursera-course-data
