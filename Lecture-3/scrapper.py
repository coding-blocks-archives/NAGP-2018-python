from selenium import webdriver

import time

import config

import os

from urllib import request

import Configration.conf

# pip install python-slugify
from slugify import slugify


# contact - anuj.garg@codingblocks.com
# handle - @KeenWarrior


class PluralSight:

    def __init__(self):
        self.browser = webdriver.Chrome("/Users/anuj/Desktop/py/Lecture-3/chromedriver")

        self.open("https://app.pluralsight.com/id")

        time.sleep(2)

        self.login()

    def formatter(self, line):
        res = ""

        for ch in line:
            if 'a' <= ch <= 'z':
                res += ch

            if 'A' <= ch <= 'Z':
                res += ch

            if '0' <= ch <= '9':
                res += ch

            if ch == " ":
                res += "-"

        return res

    def open(self, url):
        self.browser.get(url)

    def grabVideo(self, module, lecture):

        module = self.formatter(module)
        lecture = self.formatter(lecture)

        time.sleep(2)
        video = self.browser.find_element_by_tag_name("video").get_attribute("src")
        print("Starting to download")

        if not os.path.exists("downloads"):
            os.mkdir("downloads")

        if not os.path.exists("downloads/" + module):
            os.mkdir("downloads/" + module)

        request.urlretrieve(video, "downloads/" + module + "/" + lecture + ".mp4")

        print("Finished downloading")

    def login(self):

        username = self.browser.find_element_by_id("Username")
        password = self.browser.find_element_by_id("Password")
        login = self.browser.find_element_by_id("login")

        username.send_keys(config.ps_user)
        password.send_keys(config.ps_password)

        login.click()

    def showModules(self):

        modules = self.browser.find_elements_by_class_name("module")

        for module in modules:
            module_name = module.find_element_by_tag_name("h2").text

            if len(module.find_elements_by_tag_name("ul")) == 0:
                module.click()
                time.sleep(2)

            if len(module.find_elements_by_tag_name("ul")) > 0:
                lectures = module.find_element_by_tag_name("ul")

                for item in lectures.find_elements_by_tag_name("li"):
                    lecture_name = item.find_element_by_tag_name("h3").text
                    item.click()
                    time.sleep(2)
                    self.grabVideo(module_name, lecture_name)


if __name__ == "__main__":
    ps = PluralSight()

    # url = input("Please enter url : ")

    ps.open(
        "https://app.pluralsight.com/player?course=nodejs-express-web-applications&author=jonathan-mills&name=nodejs-express-web-applications-m1&clip=8&mode=live")

    time.sleep(2)

    ps.showModules()
