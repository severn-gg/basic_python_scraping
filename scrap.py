from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("user-data-dir=C:/Users/sever/AppData/Local/Google/Chrome/User Data")
driver = webdriver.Chrome(options=chrome_options)
driver.get("www.google.com")