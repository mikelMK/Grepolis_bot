import selenium
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.set_headless(headless=True)
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=r'/usr/bin/chromedriver')
driver.get("https://github.com/login")

username = driver.find_element_by_id("login_field")
password = driver.find_element_by_id("password")

username.send_keys("username")
password.send_keys("password")
time.sleep(1)

driver.find_element_by_name("commit").click()

print ("Headless Chrome Initialized")
