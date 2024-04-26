import time

import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService, Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Full_snap:
    def screenshot(self):
        s = Service("C:\\Users\\Baltech\\Downloads\\geckodriver-v0.33.0-win64\\geckodriver.exe")
        self.driver = webdriver.Firefox(service=s)
        print("opened")
        self.driver.get("https://plendrive.com.au/")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        time.sleep(5)
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0,0)")
        time.sleep(3)
        self.page_body = self.driver.find_element(By.TAG_NAME, "body")
        self.page_body.screenshot("D:\\Project Screenshots\\studiozpt\\deep2 + .png")
        print("Image saved")
        # # self.page_body.screenshot("Image.png")

        self.driver.quit()

object = Full_snap()
object.screenshot()