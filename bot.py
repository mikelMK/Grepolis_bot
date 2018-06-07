
import selenium
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json

chrome_options = Options()
# chrome_options.set_headless(headless=True)
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=r'/usr/bin/chromedriver')
driver.get("https://github.com/login")

username = driver.find_element_by_id("login_field")
password = driver.find_element_by_id("password")

with open('data.txt') as json_file:  
    data = json.load(json_file)
    name = data['name']
    passw = data['pass']

username.send_keys(name)
password.send_keys(passw)
time.sleep(1)

driver.find_element_by_name("commit").click()

print ("Headless Chrome Initialized")
# driver.quit()
