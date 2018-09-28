from selenium import webdriver

import os

import time

options = webdriver.ChromeOptions()
# options.add_argument("headless")
options.add_argument("window-size=400x400")

cdriver = webdriver.Chrome("/Users/anuj/Desktop/py/Lecture-2/chromedriver", options=options)

def get(driver, url):
    driver.get(url)

def login(driver, user, passwd):
    username = driver.find_element_by_id("Username")
    password = driver.find_element_by_id("Password")

    username.send_keys(user)
    password.send_keys(passwd)

    login = driver.find_element_by_id("login")

    login.click()


get(cdriver, "https://app.pluralsight.com/id")

time.sleep(2)

login(cdriver, os.environ.get('PS_USER'), os.environ.get('PS_PASS'))

time.sleep(2)

get(cdriver, "https://app.pluralsight.com/player?course=selenium")

