import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class loginf():
    def flipcart(self):
        # self.driver = driver
        s = Service("C:\\Users\\Baltech\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
        driver = webdriver.Chrome(service=s)
        driver.get("https://www.flipkart.com/")
        driver.implicitly_wait(5)
        driver.maximize_window()
        time.sleep(5)
        driver.find_element(By.XPATH, "//a[@href='/account/login?ret=/']").click()
        time.sleep(5)
        driver.close()
        driver.quit()

object = loginf()
object.flipcart()