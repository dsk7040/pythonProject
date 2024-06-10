#Short Methods
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By

import os
import pyautogui


class BrowserAutomation():
    def __init__(self, browser_type):

        self.browser_type = browser_type
        self.driver = browser_type

    def start_browser(self):
        if self.browser_type == 'firefox':
            # Initialize Firefox WebDriver
            f = FirefoxService("C:\\Users\\Baltech\\Downloads\\geckodriver-v0.34.0-win64\\geckodriver.exe")
            self.driver = webdriver.Firefox(service=f)
            print("skip Firefox")

        elif self.browser_type == 'chrome':
            # Initialize Chrome WebDriver
            s = ChromeService("C:\\Users\\Baltech\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
            self.driver = webdriver.Chrome(service=s)
            print("Run Chrome")

        else:
            print("Invalid browser type specified")

        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        time.sleep(2)

    def open_website(self, url):
        self.driver.get(url)

#1) Get the data from list then hit the URLs
    def getlist_data(self):
        self.mydata = ["https://hypeddit.com/", "https://example.com/"]
        a = self.mydata[0]
        print(a)
        self.driver.get(a)
        self.driver.implicitly_wait(10)

#2)Create any folder and direct using this method
    def directory(self):

        if os.path.exists("D:\\Folder"):
            print("The folder already Exist")
        else:
            os.mkdir("D:\\Folder")
            print("Folder created")
#3) Take a screenshot and save in folder according to our pasth.
    def screenshot(self):
        sshot = pyautogui.screenshot()
        sshot.save("D:\Folder\image.png")
        print("Image saved")

#4) Page scroller function
    def pagescroll(self):
        print("scroller")
        self.driver.execute_script("window.scrollBy(0,1000)")
        time.sleep(3)
        self.driver.execute_script("window.scrollBy(1000,2000)")
        time.sleep(3)
        self.driver.execute_script("window.scrollBy(2000,document.body.scrollHeight)")
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0,500)")
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(500,0)")
        time.sleep(3)
