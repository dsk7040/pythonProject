import time
#from telnetlib import EC

from selenium.webdriver.common.by import By
#from selenium.webdriver.support.wait import WebDriverWait
class Youtube_ad():

    def __init__(self, driver):
        self.driver = driver
        self.AdsGoogleLoginDiv_xpath = "//a[@id='AdsGoogleLogin']"

    def new_youtubead(self):
        self.driver.get("https://dev2.hypeddit.com/ads/create/youtube-growth-video")
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//a[@id='AdsGoogleLogin']").click()
        time.sleep(2)
        # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
        # (By.XPATH, self.AdsGoogleLoginDiv_xpath))).click()
