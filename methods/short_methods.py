#Short Methods
import os
import pyautogui
#1) Get the data from list then hit the URLs
class getlist_data():

    def get_data(self):
        self.mydata = ["https://hypeddit.com/", "https://example.com/"]
        a = self.mydata[0]
        print(a)
        self.driver.get(a)
        self.driver.implicitly_wait(10)

obj = getlist_data()
obj.get_data()

#2)Create any folder and direct using this method

class folder():

    def directory(self):

        if os.path.exists("D:\\Folder"):
            print("The folder already Exist")
        else:
            os.mkdir("D:\\Folder")
            print("Folder created")

obj = folder()
obj.directory()


#3) Take a screenshot and save in folder according to our pasth.

class snap():

    def screenshot(self):
        sshot = pyautogui.screenshot()
        sshot.save("D:\Folder\image.png")
        print("Image saved")

obj = snap()
obj.screenshot()