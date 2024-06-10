import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService, Service
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from methods.short_methods import BrowserAutomation
from webdriver_manager.chrome import ChromeDriverManager

class Full_snap:

    def __init__(self):
        f = FirefoxService("C:\\Users\\Baltech\\Downloads\\geckodriver-v0.34.0-win64\\geckodriver.exe")
        self.driver = webdriver.Firefox(service=f)
        self.driver.get("https://evergreenwinerytours.com.au/")
        self.driver.implicitly_wait(5)
        #self.driver.set_window_size(1366, 1366)
        self.driver.maximize_window()

    def screenshot(self):
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
        # time.sleep(3)
        self.page_body = self.driver.find_element(By.TAG_NAME, "html")

        self.page_body.screenshot("D:\\Project Screenshots\\deep .png")
        print("Image saved")
        self.driver.close()
        self.driver.quit()

object = Full_snap()
object.screenshot()
# object.pagescroll()