from selenium import webdriver
from selenium.webdriver.firefox.service import service, Service
import os
import pyautogui


class MyList:
    def getlink(self):
        s = Service("C:\\Users\\Baltech\\Downloads\\geckodriver-v0.33.0-win64\\geckodriver.exe")
        self.driver = webdriver.Firefox(service=s)

    def get_data(self):
        self.mylist = ["https://hypeddit.com/", "https://www.bungamabattery.com.au/"]
        length = len(self.mylist)
        for i in range(length):
            self.driver.get(self.mylist[i])
            self.driver.implicitly_wait(10)

            deep = self.mylist[i].replace(":", " ")
            deep1 = deep.replace("/", "-")
            print(deep1)

            if os.path.exists("D:\\hypeddit\\" + deep1):
                print("The folder already Exist")
            else:
                os.mkdir("D:\\hypeddit\\" + deep1)
                print("Folder created")

            sshot = pyautogui.screenshot()
            sshot.save("D:\\hypeddit\\" + deep1 + "\\image" + str(i) + ".png")
            print("Image saved")

        self.driver.close()
        self.driver.quit()



obj = MyList()
obj.getlink()
obj.get_data()
