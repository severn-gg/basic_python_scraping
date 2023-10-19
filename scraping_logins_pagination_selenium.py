#INSTALL SELENIUM BEFORE RUNNING THIS CODE
#pip3 install selenium
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import getpass
from selenium.common.exceptions import NoSuchElementException

#IF USING A RASPBERRY PI, FIRST INSTALL THIS OPTIMIZED CHROME DRIVER
#sudo apt-get install chromium-chromedriver
# browser_driver = Service('/usr/lib/chromium-browser/chromedriver')
page_to_scrape = webdriver.Chrome()
page_to_scrape.get("https://play.google.com/store/apps/details?id=com.app.cumobileonline&pli=1")

page_to_scrape.find_element(By.CLASS_NAME, "VfPpkd-vQzf8d").click()

time.sleep(3)

author = page_to_scrape.find_elements(By.CLASS_NAME, "X5PpBb")
date = page_to_scrape.find_elements(By.CLASS_NAME, "bp9Aid")
star = page_to_scrape.find_elements(By.CLASS_NAME, "iXRFPc")
comment = page_to_scrape.find_elements(By.CLASS_NAME, "h3YV2d")

file = open("scraped_quotes.csv", "w")
writer = csv.writer(file)

writer.writerow(["AUTHORS","Date","STAR","COMMENT"])
while True:
    author = page_to_scrape.find_elements(By.CLASS_NAME, "X5PpBb")
    date = page_to_scrape.find_elements(By.CLASS_NAME, "bp9Aid")
    star = page_to_scrape.find_elements(By.CLASS_NAME, "iXRFPc")
    comment = page_to_scrape.find_elements(By.CLASS_NAME, "h3YV2d")
    for quote, author in zip(author,date,star,comment):
        # print(quote.text + " - " + author.text)
        writer.writerow([author.text, date.text, star.text, comment.text])
    break
file.close()
