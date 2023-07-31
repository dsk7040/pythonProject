import time
from selenium.webdriver.common.by import By
class Loudlinks():

    def __init__(self, driver):
        self.driver = driver

        self.select_music_xpath = "//button[@title='Please select music']"
        self.baller_tract_xpath = "//span[contains(text(),'Baller : [Spotify]')]"
        self.Next_button_xpath = "//div[@id='2']//a[@class='button button-primary select-gate-button']"
        self.Web_url_xpath = "//input[@id='content_link']"
        self.Create_id = "saveMusicBar"

    def Create_loudlink(self, weburl):
        self.driver.get("https://dev2.hypeddit.com/loudlinks/create")
        self.driver.implicitly_wait(2)
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.select_music_xpath).click()
        self.driver.find_element(By.XPATH, self.baller_tract_xpath).click()
        self.driver.find_element(By.XPATH, self.Next_button_xpath).click()
        self.driver.find_element(By.XPATH, self.Web_url_xpath).send_keys(weburl)
        self.driver.find_element(By.ID, self.Create_id).click()
        time.sleep(10)








