from selenium import webdriver
from selenium.webdriver.firefox.service import service, Service
import parser_libraries
from urllib.parse import urljoin
import os
import requests
from bs4 import BeautifulSoup
class Bungama():
  

    def __init__(self):
        self.base_url = "https://evergreenwinerytours.com.au/"


    def homeurl(self):
        global new_list
        screenshot_folder = "D:\\Project Screenshots\\computertalk"

        if os.path.exists(screenshot_folder):
            print("The folder already Exist")
        else:
            os.mkdir(screenshot_folder)
            print("Folder created")

        grab = requests.get(self.base_url)
        soup = BeautifulSoup(grab.text, "lxml")

        url_list = []
        for link in soup.find_all("a"):
            data = link.get('href')
            if data and data not in url_list:
                if self.base_url in data and "wp-content" not in data:
                    url_list.append(data)
        print(url_list)
        print("Home page Successfully ")

        self.inner_url = url_list
        length = len(self.inner_url)
        new_list = []
        for i in range(length):
            grab2 = requests.get(self.inner_url[i])
            soup2 = BeautifulSoup(grab2.text, "lxml")

            for link2 in soup2.find_all("a"):
                data2 = link2.get('href')
                if data2 and data2 not in new_list:
                    if self.base_url in data2 and "wp-content" not in data2:
                        new_list.append(data2)

        print(new_list)
        print("New URLs fetched successfully:")
        return new_list

# obj = Bungama()
# obj.homeurl()



