import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import service, Service
from python_practice.geturls_list import bungama
import os
import pyautogui


class MyList:
    def getlink(self, final_list):
        s = Service("C:\\Users\\Baltech\\Downloads\\geckodriver-v0.33.0-win64\\geckodriver.exe")
        self.driver = webdriver.Firefox(service=s)

    #def get_data(self):
        self.mylist = final_list
        #print(self.mylist)
        length = len(self.mylist)
        for i in range(length):
            self.driver.get(self.mylist[i])
            self.driver.implicitly_wait(10)
            time.sleep(5)
            deep = self.mylist[i].replace(":", " ")
            deep1 = deep.replace("/", "-")

            # if os.path.exists("D:\\bungamabattery\\" + deep1):
            #     print("The folder already Exist")
            # else:
            #     os.mkdir("D:\\bungamabattery\\" + deep1)
            #     print("Folder created")
            # self.width = 1366
            # #self.height = 768
            # self.driver.set_window_size(self.width, self.height)
            # self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
            # time.sleep(2)
            # self.driver.execute_script("window.scrollTo(0,0)")
            # time.sleep(3)
            self.page_body = self.driver.find_element(By.TAG_NAME, "body")

            self.page_body.screenshot("D:\\Project Screenshots\\valuedge2\\" + deep1 + ".png")
            # sshot = pyautogui.screenshot()
            # #sshot.save("D:\\bungamabattery\\" + deep1 + "\\deep1" + str(i) + ".png")
            # sshot.save("D:\\New Screenshots\\Maintenance\\" + deep1 + ".png")
        print("Image saved")

        self.driver.close()
        self.driver.quit()


obj2 = bungama()
final_list = obj2.homeurl()
obj = MyList()
obj.getlink(final_list)
#obj.get_data()

print("passed")

