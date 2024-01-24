from selenium import webdriver
from selenium.webdriver.firefox.service import service, Service
import os
import pyautogui


class MyList:
    def getlink(self):
        s = Service("C:\\Users\\Baltech\\Downloads\\geckodriver-v0.33.0-win64\\geckodriver.exe")
        self.driver = webdriver.Firefox(service=s)

    def get_data(self):
        self.mylist = ["https://hypeddit.com/login", "https://auswide.webdesignmelbourne.agency/"]
        length = len(self.mylist)
        for i in range(length):
            self.driver.get(self.mylist[i])

            self.driver.implicitly_wait(10)
            if os.path.exists("D:\\hypeddit"):
                print("The folder already Exist")
            else:
                os.mkdir("D:\\hypeddit")
                print("Folder created")

            sshot = pyautogui.screenshot()
            sshot.save("D:\hypeddit\\deep" + str(i) + ".png")
            print("Image saved")

        self.driver.close()
        self.driver.quit()

    # def directory(self):
    #
    #     if os.path.exists("D:\\Folder"):
    #         print("The folder already Exist")
    #     else:
    #         os.mkdir("D:\\Folder")
    #         print("Folder created")
    #
    #     sshot = pyautogui.screenshot()
    #     sshot.save("D:\Folder\image.png")
    #     print("Image saved")
    #
    #     self.driver.close()
    #     self.driver.quit()


obj = MyList()
obj.getlink()
obj.get_data()
# obj.directory()
