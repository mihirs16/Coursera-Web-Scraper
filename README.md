# Coursera-Web-Scraper
![](https://img.shields.io/github/forks/mihirs16/Coursera-Web-Scraper?style=for-the-badge)
![](https://img.shields.io/github/stars/mihirs16/Coursera-Web-Scraper?color=54A5B4&style=for-the-badge)
![](https://img.shields.io/github/issues-closed/mihirs16/Coursera-Web-Scraper?color=green&style=for-the-badge)
## Prerequisites
* Python (tested for 3.7 and above)
* [PhantomJs](https://phantomjs.org/) or any other headless browser for automation.
* [Selenium](https://selenium-python.readthedocs.io/) Web Driver for Python
* Other Libraries:
  * Pandas
  * Mutliprocessing

## Instructions
* Make sure you download PhantomJs (included in the dependency folder if you clone) and add it to your PATH.
* Clone the repository.
```git
git clone https://github.com/mihirs16/Coursera-Web-Scraper
```

* First run `coursera_scraper.py` to retrieve a list of all courses from the [Coursera course directory](https://www.coursera.org/directory).
```
python coursera_scraper.py
```

* Now run `coursera_deep_scraper.py` to retrieve the details of all the courses in the list.
```
python coursera_deep_scraper.py
```

* If met with the connection closed error, the Coursera.org website is blocking your request and thus the script is overreaching the allowed policy of the website. Please exercise and caution and respect.
## Disclaimer:-
<ol>
  <li>Data is all around us, but this doesn't mean we own it. Please respect the policies of Coursera and the website <a href="https://coursera.org">Coursera.org</a>. Please be respectful of the website and avoid spamming it with continuous zero delay or parallel requests. You can check the website's scraping policy <a href="https://www.coursera.org/robots.txt">here</a>.</li>
  <li>Since Coursera and all websites take measures to handle multiple parallel requests, one might face "Connection closed" during long period of scraping. You can continue the scraping by restarting the script, if left undisturbed, the script reads the courses scraped from the list of courses, and the courses left. Thus letting you continue from where you left off. (Once again reminding you to respect the website and it's policies).</li>
</ol>

## Dataset 
The Coursera Courses Dataset is uploaded [here](https://www.kaggle.com/mihirs16/coursera-course-data).
