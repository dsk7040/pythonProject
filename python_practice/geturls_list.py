from selenium import webdriver
from selenium.webdriver.firefox.service import service, Service
import os
import pyautogui
import requests
from bs4 import BeautifulSoup
class bungama():
  

    def __init__(self):
        self.new_list = None
        self.url_list = None

    def homeurl(self):

        # s = Service("C:\\Users\\Baltech\\Downloads\\geckodriver-v0.33.0-win64\\geckodriver.exe")
        # self.driver = webdriver.Firefox(service=s)
        # new_list = []
        global new_list
        self.urls = "https://valuedge.com.au/"

        if os.path.exists("D:\\Project Screenshots\\valuedge2"):
            print("The folder already Exist")
        else:
            os.mkdir("D:\\Project Screenshots\\valuedge2")
            print("Folder created")

        grab = requests.get(self.urls)
        soup = BeautifulSoup(grab.text, "lxml")

        url_list = []
        for link in soup.find_all("a"):
            data = link.get('href')
            if data not in url_list:
                if self.urls in data:
                    url_list.append(data)

        #print(url_list)
        print("Home page Successfully ")

        self.inner_url = url_list
        length = len(self.inner_url)
        new_list = []
        for i in range(length):
            grab2 = requests.get(self.inner_url[i])
            soup2 = BeautifulSoup(grab2.text, "lxml")


            for link2 in soup2.find_all("a"):
                data2 = link2.get('href')
                if data2 not in new_list:
                    if self.urls in data2:
                        new_list.append(data2)
            #print(self.inner_url[i])
            #print(new_list)
        print("New list Successfully ")

        return new_list

# obj = bungama()
# obj.homeurl()



