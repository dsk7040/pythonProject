import time
import parser_libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from python_practice.websnaps_test import Bungama
import os
import pyautogui


class MyList:
    def getlink(self, final_list):
        f = FirefoxService("C:\\Users\\Baltech\\Downloads\\geckodriver-v0.34.0-win64\\geckodriver.exe")
        self.driver = webdriver.Firefox(service=f)
        self.mylist = final_list
        #print(self.mylist)
        length = len(self.mylist)
        for i in range(length):
            self.driver.get(self.mylist[i])
            self.driver.implicitly_wait(10)
            time.sleep(5)
            rename = self.mylist[i].replace(":", " ")
            image = rename.replace("/", "-")

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
            self.page_body = self.driver.find_element(By.TAG_NAME, "html")
            self.page_body.screenshot("D:\\Project Screenshots\\computertalk\\" + image + ".png")

        print("Image saved")

        self.driver.close()
        self.driver.quit()


obj2 = Bungama()
final_list = obj2.homeurl()
if final_list is not None:
    obj = MyList()
    obj.getlink(final_list)
    print("passed")
else:
    print("Error: homeurl() returned None")
# obj = MyList()
# obj.getlink(final_list)


